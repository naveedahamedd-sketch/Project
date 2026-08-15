"""Tests for Resume class"""

import json
import tempfile
from pathlib import Path
from resume_generator.resume import Resume, ContactInfo, Experience, Education, Skill


def test_create_resume():
    """Test creating a basic resume"""
    contact = ContactInfo(
        name="John Doe",
        email="john@example.com",
        phone="555-1234",
        location="New York, NY"
    )
    resume = Resume(contact)
    
    assert resume.contact_info.name == "John Doe"
    assert resume.contact_info.email == "john@example.com"


def test_add_experience():
    """Test adding work experience"""
    contact = ContactInfo(
        name="John Doe",
        email="john@example.com",
        phone="555-1234",
        location="New York, NY"
    )
    resume = Resume(contact)
    
    exp = Experience(
        company="Tech Inc",
        position="Engineer",
        start_date="2020",
        end_date="2024",
        description=["Built features", "Led team"]
    )
    resume.add_experience(exp)
    
    assert len(resume.experiences) == 1
    assert resume.experiences[0].company == "Tech Inc"


def test_resume_to_json():
    """Test converting resume to JSON"""
    contact = ContactInfo(
        name="John Doe",
        email="john@example.com",
        phone="555-1234",
        location="New York, NY"
    )
    resume = Resume(contact)
    resume.set_summary("Test summary")
    
    json_str = resume.to_json()
    data = json.loads(json_str)
    
    assert data["contact_info"]["name"] == "John Doe"
    assert data["summary"] == "Test summary"


def test_resume_save_and_load():
    """Test saving and loading resume from JSON"""
    contact = ContactInfo(
        name="John Doe",
        email="john@example.com",
        phone="555-1234",
        location="New York, NY"
    )
    resume = Resume(contact)
    resume.set_summary("Test summary")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = Path(tmpdir) / "resume.json"
        resume.save_json(str(filepath))
        
        loaded_resume = Resume.from_json(str(filepath))
        assert loaded_resume.contact_info.name == "John Doe"
        assert loaded_resume.summary == "Test summary"


if __name__ == "__main__":
    test_create_resume()
    test_add_experience()
    test_resume_to_json()
    test_resume_save_and_load()
    print("All tests passed!")
