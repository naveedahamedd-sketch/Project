"""
PDF Generation module using ReportLab
"""

from typing import Optional
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from .resume import Resume


class PDFGenerator:
    """Generate PDF resumes from Resume objects"""

    def __init__(self, pagesize=letter, font_name="Helvetica"):
        """
        Initialize PDF generator
        
        Args:
            pagesize: Page size (letter or A4)
            font_name: Default font name
        """
        self.pagesize = pagesize
        self.font_name = font_name
        self.styles = self._create_styles()

    def _create_styles(self):
        """Create custom paragraph styles"""
        styles = getSampleStyleSheet()
        
        # Custom title style
        styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#1a1a1a'),
            spaceAfter=6,
            alignment=TA_CENTER,
            fontName=self.font_name,
            fontNameBold=f'{self.font_name}-Bold',
        ))
        
        # Custom heading style
        styles.add(ParagraphStyle(
            name='SectionHeading',
            parent=styles['Heading2'],
            fontSize=12,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=8,
            spaceBefore=8,
            fontName=self.font_name,
            fontNameBold=f'{self.font_name}-Bold',
            borderColor=colors.HexColor('#34495e'),
            borderWidth=0.5,
            borderPadding=4,
        ))
        
        return styles

    def generate(self, resume: Resume, filename: str) -> None:
        """
        Generate PDF from resume
        
        Args:
            resume: Resume object to convert to PDF
            filename: Output filename
        """
        doc = SimpleDocTemplate(
            filename,
            pagesize=self.pagesize,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch,
        )
        
        story = []
        
        # Header with contact info
        story.append(self._create_header(resume))
        story.append(Spacer(1, 0.2*inch))
        
        # Professional Summary
        if resume.summary:
            story.append(Paragraph("PROFESSIONAL SUMMARY", self.styles['SectionHeading']))
            story.append(Paragraph(resume.summary, self.styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
        
        # Experience
        if resume.experiences:
            story.append(Paragraph("EXPERIENCE", self.styles['SectionHeading']))
            for exp in resume.experiences:
                story.append(self._create_experience_entry(exp))
            story.append(Spacer(1, 0.1*inch))
        
        # Education
        if resume.education:
            story.append(Paragraph("EDUCATION", self.styles['SectionHeading']))
            for edu in resume.education:
                story.append(self._create_education_entry(edu))
            story.append(Spacer(1, 0.1*inch))
        
        # Skills
        if resume.skills:
            story.append(Paragraph("SKILLS", self.styles['SectionHeading']))
            for skill_cat in resume.skills:
                skill_text = f"<b>{skill_cat.category}:</b> {', '.join(skill_cat.skills)}"
                story.append(Paragraph(skill_text, self.styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
        
        # Languages
        if resume.languages:
            story.append(Paragraph("LANGUAGES", self.styles['SectionHeading']))
            for lang, proficiency in resume.languages.items():
                story.append(Paragraph(f"{lang} - {proficiency}", self.styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
        
        # Certifications
        if resume.certifications:
            story.append(Paragraph("CERTIFICATIONS", self.styles['SectionHeading']))
            for cert in resume.certifications:
                story.append(Paragraph(f"• {cert}", self.styles['Normal']))
        
        # Build PDF
        doc.build(story)
        print(f"PDF resume generated: {filename}")

    def _create_header(self, resume: Resume) -> Paragraph:
        """Create header with contact information"""
        contact = resume.contact_info
        header_lines = [contact.name]
        
        # Add contact details
        contact_details = []
        if contact.email:
            contact_details.append(contact.email)
        if contact.phone:
            contact_details.append(contact.phone)
        if contact.location:
            contact_details.append(contact.location)
        if contact.website:
            contact_details.append(contact.website)
        if contact.linkedin:
            contact_details.append(f"LinkedIn: {contact.linkedin}")
        if contact.github:
            contact_details.append(f"GitHub: {contact.github}")
        
        header = f"""
        <b><font size=16>{contact.name}</font></b><br/>
        <font size=10>{' | '.join(contact_details)}</font>
        """
        
        return Paragraph(header, self.styles['CustomTitle'])

    def _create_experience_entry(self, experience) -> Paragraph:
        """Create formatted experience entry"""
        text = f"""
        <b>{experience.position}</b> at {experience.company}<br/>
        <i>{experience.format_dates()}</i><br/>
        {'<br/>'.join(f'• {desc}' for desc in experience.description)}
        """
        return Paragraph(text, self.styles['Normal'])

    def _create_education_entry(self, education) -> Paragraph:
        """Create formatted education entry"""
        text = f"""
        <b>{education.degree} in {education.field}</b><br/>
        {education.school} | Graduated: {education.graduation_date}
        """
        if education.gpa:
            text += f"<br/>GPA: {education.gpa}"
        
        return Paragraph(text, self.styles['Normal'])
