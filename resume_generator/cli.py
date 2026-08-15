"""
Command-Line Interface for Resume Generator
"""

import click
import sys
import os
from pathlib import Path
from .resume import Resume, ContactInfo, Experience, Education, Skill, Project
from .pdf_generator import PDFGenerator
from colorama import Fore, Style, init

init(autoreset=True)


@click.group()
def cli():
    """Resume Generator - Create professional resumes with ease"""
    pass


@cli.command()
@click.option('--name', prompt='Full Name', help='Your full name')
@click.option('--email', prompt='Email', help='Your email address')
@click.option('--phone', prompt='Phone', help='Your phone number')
@click.option('--location', prompt='Location', help='Your location')
@click.option('--output', default='resume.json', help='Output file path')
def create(name, email, phone, location, output):
    """Create a new resume"""
    contact_info = ContactInfo(
        name=name,
        email=email,
        phone=phone,
        location=location
    )
    
    resume = Resume(contact_info)
    resume.save_json(output)
    click.echo(f"{Fore.GREEN}✓ Resume created successfully!{Style.RESET_ALL}")
    click.echo(f"Saved to: {output}")


@cli.command()
@click.argument('resume_file', type=click.Path(exists=True))
@click.option('--output', default='resume.pdf', help='Output PDF file path')
def generate_pdf(resume_file, output):
    """Generate PDF from a resume JSON file"""
    try:
        resume = Resume.from_json(resume_file)
        generator = PDFGenerator()
        generator.generate(resume, output)
        click.echo(f"{Fore.GREEN}✓ PDF generated successfully!{Style.RESET_ALL}")
        click.echo(f"Saved to: {output}")
    except FileNotFoundError:
        click.echo(f"{Fore.RED}✗ Resume file not found: {resume_file}{Style.RESET_ALL}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"{Fore.RED}✗ Error generating PDF: {e}{Style.RESET_ALL}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('resume_file', type=click.Path(exists=True))
def view(resume_file):
    """View resume content in terminal"""
    try:
        resume = Resume.from_json(resume_file)
        click.echo(resume)
    except FileNotFoundError:
        click.echo(f"{Fore.RED}✗ Resume file not found: {resume_file}{Style.RESET_ALL}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"{Fore.RED}✗ Error reading resume: {e}{Style.RESET_ALL}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def convert(input_file, output_file):
    """Convert between resume formats (JSON to JSON)"""
    try:
        resume = Resume.from_json(input_file)
        resume.save_json(output_file)
        click.echo(f"{Fore.GREEN}✓ Resume converted successfully!{Style.RESET_ALL}")
        click.echo(f"Saved to: {output_file}")
    except Exception as e:
        click.echo(f"{Fore.RED}✗ Error converting resume: {e}{Style.RESET_ALL}", err=True)
        sys.exit(1)


@cli.command()
def init_template():
    """Create a sample resume template"""
    sample_contact = ContactInfo(
        name="John Doe",
        email="john.doe@example.com",
        phone="+1-234-567-8900",
        location="San Francisco, CA",
        website="https://johndoe.com",
        linkedin="https://linkedin.com/in/johndoe",
        github="https://github.com/johndoe"
    )
    
    resume = Resume(sample_contact)
    
    # Add summary
    resume.set_summary(
        "Experienced software engineer with 5+ years of expertise in full-stack development. "
        "Passionate about creating scalable applications and mentoring junior developers."
    )
    
    # Add experience
    exp1 = Experience(
        company="Tech Company Inc.",
        position="Senior Software Engineer",
        start_date="Jan 2021",
        end_date="Present",
        current=True,
        description=[
            "Led development of microservices architecture serving 1M+ users",
            "Mentored 3 junior engineers and conducted code reviews",
            "Improved API performance by 40% through optimization"
        ]
    )
    resume.add_experience(exp1)
    
    exp2 = Experience(
        company="StartUp Corp",
        position="Junior Software Engineer",
        start_date="Jun 2018",
        end_date="Dec 2020",
        description=[
            "Developed and maintained web applications using Django and React",
            "Implemented automated testing increasing code coverage to 85%",
            "Collaborated with product team to deliver features on time"
        ]
    )
    resume.add_experience(exp2)
    
    # Add education
    edu = Education(
        school="University of Technology",
        degree="Bachelor of Science",
        field="Computer Science",
        graduation_date="May 2018",
        gpa="3.8/4.0",
        honors=["Magna Cum Laude", "Dean's List"]
    )
    resume.add_education(edu)
    
    # Add skills
    skills_backend = Skill(
        category="Backend",
        skills=["Python", "Django", "Node.js", "PostgreSQL", "MongoDB"]
    )
    resume.add_skill(skills_backend)
    
    skills_frontend = Skill(
        category="Frontend",
        skills=["React", "Vue.js", "JavaScript", "TypeScript", "CSS"]
    )
    resume.add_skill(skills_frontend)
    
    skills_tools = Skill(
        category="Tools & DevOps",
        skills=["Docker", "Kubernetes", "Git", "AWS", "CI/CD"]
    )
    resume.add_skill(skills_tools)
    
    # Add project
    project = Project(
        title="Open Source Project",
        description="Contributed to major open-source project",
        technologies=["Python", "JavaScript"],
        link="https://github.com/example",
        date="2020-2021"
    )
    resume.add_project(project)
    
    # Add languages
    resume.add_language("English", "Native")
    resume.add_language("Spanish", "Fluent")
    
    # Add certification
    resume.add_certification("AWS Certified Solutions Architect")
    resume.add_certification("Certified Kubernetes Administrator")
    
    resume.save_json("sample_resume.json")
    click.echo(f"{Fore.GREEN}✓ Sample resume template created!{Style.RESET_ALL}")
    click.echo("Saved to: sample_resume.json")


def main():
    """Main entry point"""
    if len(sys.argv) == 1:
        cli(['--help'])
        return 0
    return cli()
