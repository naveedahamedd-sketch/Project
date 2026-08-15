"""
Core Resume class for managing resume data
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any
from datetime import datetime
import json


@dataclass
class ContactInfo:
    """Contact information section"""
    name: str
    email: str
    phone: str
    location: str
    website: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None


@dataclass
class Experience:
    """Work experience entry"""
    company: str
    position: str
    start_date: str
    end_date: str
    description: List[str] = field(default_factory=list)
    current: bool = False

    def format_dates(self) -> str:
        """Format date range for display"""
        end = "Present" if self.current else self.end_date
        return f"{self.start_date} - {end}"


@dataclass
class Education:
    """Education entry"""
    school: str
    degree: str
    field: str
    graduation_date: str
    gpa: Optional[str] = None
    honors: Optional[List[str]] = field(default_factory=list)


@dataclass
class Skill:
    """Skill entry with category"""
    category: str
    skills: List[str] = field(default_factory=list)


@dataclass
class Project:
    """Personal/Portfolio project"""
    title: str
    description: str
    technologies: List[str] = field(default_factory=list)
    link: Optional[str] = None
    date: Optional[str] = None


class Resume:
    """Main Resume class for managing all resume data"""

    def __init__(self, contact_info: ContactInfo):
        """
        Initialize a resume with contact information
        
        Args:
            contact_info: ContactInfo object with personal details
        """
        self.contact_info = contact_info
        self.experiences: List[Experience] = []
        self.education: List[Education] = []
        self.skills: List[Skill] = []
        self.projects: List[Project] = []
        self.summary: Optional[str] = None
        self.certifications: List[str] = []
        self.languages: Dict[str, str] = {}  # language: proficiency
        self.created_at = datetime.now()

    def add_experience(self, experience: Experience) -> None:
        """Add work experience"""
        self.experiences.append(experience)

    def add_education(self, education: Education) -> None:
        """Add education entry"""
        self.education.append(education)

    def add_skill(self, skill: Skill) -> None:
        """Add skill category"""
        self.skills.append(skill)

    def add_project(self, project: Project) -> None:
        """Add portfolio project"""
        self.projects.append(project)

    def add_certification(self, certification: str) -> None:
        """Add certification"""
        self.certifications.append(certification)

    def add_language(self, language: str, proficiency: str) -> None:
        """Add language proficiency"""
        self.languages[language] = proficiency

    def set_summary(self, summary: str) -> None:
        """Set professional summary"""
        self.summary = summary

    def to_dict(self) -> Dict[str, Any]:
        """Convert resume to dictionary"""
        return {
            "contact_info": asdict(self.contact_info),
            "summary": self.summary,
            "experience": [asdict(exp) for exp in self.experiences],
            "education": [asdict(edu) for edu in self.education],
            "skills": [asdict(skill) for skill in self.skills],
            "projects": [asdict(proj) for proj in self.projects],
            "certifications": self.certifications,
            "languages": self.languages,
            "created_at": self.created_at.isoformat(),
        }

    def to_json(self, pretty: bool = True) -> str:
        """Convert resume to JSON string"""
        return json.dumps(self.to_dict(), indent=2 if pretty else None)

    def save_json(self, filepath: str) -> None:
        """Save resume as JSON file"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.to_json())
        print(f"Resume saved to {filepath}")

    @classmethod
    def from_json(cls, filepath: str) -> "Resume":
        """Load resume from JSON file"""
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        contact = ContactInfo(**data["contact_info"])
        resume = cls(contact)
        resume.summary = data.get("summary")
        
        for exp in data.get("experience", []):
            resume.add_experience(Experience(**exp))
        
        for edu in data.get("education", []):
            resume.add_education(Education(**edu))
        
        for skill in data.get("skills", []):
            resume.add_skill(Skill(**skill))
        
        for proj in data.get("projects", []):
            resume.add_project(Project(**proj))
        
        for cert in data.get("certifications", []):
            resume.add_certification(cert)
        
        for lang, prof in data.get("languages", {}).items():
            resume.add_language(lang, prof)
        
        return resume

    def __str__(self) -> str:
        """String representation of resume"""
        lines = [
            f"Resume for {self.contact_info.name}",
            "=" * 50,
            f"Email: {self.contact_info.email}",
            f"Phone: {self.contact_info.phone}",
            f"Location: {self.contact_info.location}",
        ]
        
        if self.summary:
            lines.extend(["\nPROFESSIONAL SUMMARY", "-" * 30, self.summary])
        
        if self.experiences:
            lines.extend(["\nEXPERIENCE", "-" * 30])
            for exp in self.experiences:
                lines.append(f"{exp.position} at {exp.company} ({exp.format_dates()})")
        
        if self.education:
            lines.extend(["\nEDUCATION", "-" * 30])
            for edu in self.education:
                lines.append(f"{edu.degree} in {edu.field} from {edu.school}")
        
        if self.skills:
            lines.extend(["\nSKILLS", "-" * 30])
            for skill_cat in self.skills:
                lines.append(f"{skill_cat.category}: {', '.join(skill_cat.skills)}")
        
        return "\n".join(lines)
