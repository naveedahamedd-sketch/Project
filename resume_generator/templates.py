"""
Resume templates and styling options
"""

from enum import Enum
from typing import Dict, Any


class ResumeTemplate(Enum):
    """Available resume templates"""
    PROFESSIONAL = "professional"
    MODERN = "modern"
    ACADEMIC = "academic"
    CREATIVE = "creative"


class TemplateConfig:
    """Template configuration and styling"""
    
    TEMPLATES: Dict[ResumeTemplate, Dict[str, Any]] = {
        ResumeTemplate.PROFESSIONAL: {
            "name": "Professional",
            "description": "Classic professional resume style",
            "colors": {
                "primary": "#000000",
                "secondary": "#333333",
                "accent": "#0066cc",
            },
            "fonts": {
                "body": "Helvetica",
                "heading": "Helvetica-Bold",
            },
            "spacing": {
                "section_gap": 12,
                "item_gap": 6,
            }
        },
        ResumeTemplate.MODERN: {
            "name": "Modern",
            "description": "Contemporary resume with sidebars",
            "colors": {
                "primary": "#2c3e50",
                "secondary": "#34495e",
                "accent": "#3498db",
            },
            "fonts": {
                "body": "Helvetica",
                "heading": "Helvetica-Bold",
            },
            "spacing": {
                "section_gap": 14,
                "item_gap": 8,
            }
        },
        ResumeTemplate.ACADEMIC: {
            "name": "Academic",
            "description": "Academic and research-focused resume",
            "colors": {
                "primary": "#1a1a1a",
                "secondary": "#4a4a4a",
                "accent": "#006600",
            },
            "fonts": {
                "body": "Times-Roman",
                "heading": "Times-Bold",
            },
            "spacing": {
                "section_gap": 12,
                "item_gap": 6,
            }
        },
        ResumeTemplate.CREATIVE: {
            "name": "Creative",
            "description": "Creative and colorful resume design",
            "colors": {
                "primary": "#ff6b6b",
                "secondary": "#4ecdc4",
                "accent": "#ffe66d",
            },
            "fonts": {
                "body": "Helvetica",
                "heading": "Helvetica-Bold",
            },
            "spacing": {
                "section_gap": 16,
                "item_gap": 10,
            }
        },
    }

    @classmethod
    def get_template(cls, template: ResumeTemplate) -> Dict[str, Any]:
        """Get template configuration"""
        return cls.TEMPLATES.get(template, cls.TEMPLATES[ResumeTemplate.PROFESSIONAL])

    @classmethod
    def list_templates(cls) -> list:
        """List all available templates"""
        return [
            {
                "id": template.value,
                "name": config["name"],
                "description": config["description"],
            }
            for template, config in cls.TEMPLATES.items()
        ]


# Sample resume sections text
SECTION_TEMPLATES = {
    "summary": """Experienced {job_title} with {years}+ years of expertise in {skills}. 
Passionate about {passion} and dedicated to delivering high-quality solutions.""",
    
    "achievement": """• {achievement}
• {achievement}
• {achievement}""",
    
    "bullet_point": "• {description}",
}
