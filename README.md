# Resume Generator

A professional Python CLI tool for generating beautiful, formatted resumes in multiple formats.

## Features

- ✨ **Easy Resume Creation** - Interactive CLI for building resumes
- 📄 **PDF Generation** - Convert resumes to professional PDF format
- 💾 **JSON Storage** - Store resume data in structured JSON format
- 🎨 **Multiple Templates** - Choose from professional, modern, academic, and creative styles
- 🌐 **Multi-format Support** - Support for JSON, PDF, and more formats
- 📱 **Contact Management** - Manage contact info, emails, phone, websites, and social links
- 🏢 **Work Experience** - Track employment history with descriptions
- 🎓 **Education** - Include education details with honors and GPA
- 💼 **Skills Management** - Organize skills by categories
- 📚 **Projects** - Showcase portfolio projects
- 🏆 **Certifications** - Add professional certifications
- 🌍 **Languages** - Include language proficiencies

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### From Source

1. Clone the repository:
```bash
git clone https://github.com/yourusername/resume-generator.git
cd resume-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install the package in development mode:
```bash
pip install -e .
```

## Quick Start

### Web Interface (Recommended)

The easiest way to create resumes is using the web interface:

```bash
python app.py
```

Then open your browser and go to `http://localhost:5000`

The web interface provides:
- 🖥️ **User-friendly interface** - No command-line knowledge required
- 📝 **Form-based resume creation** - Fill out intuitive forms
- 👁️ **Live preview** - See your resume as you type
- 📥 **Download PDF** - Export your resume as PDF
- 💾 **Save multiple versions** - Keep different resume versions
- 🔄 **Edit anytime** - Update your resumes whenever needed

### Command-Line Interface (CLI)

For command-line users:

#### Create a Sample Resume
```bash
python Main.py init-template
```
This creates a `sample_resume.json` file with example data.

### Create a New Resume
```bash
python Main.py create --name "Your Name" --email "you@example.com" --phone "123-456-7890" --location "City, State"
```

### Generate PDF
```bash
python Main.py generate-pdf sample_resume.json --output my_resume.pdf
```

### View Resume in Terminal
```bash
python Main.py view sample_resume.json
```

## Usage

### Command-Line Interface

#### Initialize Sample Resume
Creates a fully populated sample resume for reference:
```bash
python Main.py init-template
```

#### Create a Resume
```bash
python Main.py create [OPTIONS]

Options:
  --name TEXT          Your full name
  --email TEXT         Your email address
  --phone TEXT         Your phone number
  --location TEXT      Your location
  --output TEXT        Output file path (default: resume.json)
```

#### Generate PDF from JSON
```bash
python Main.py generate-pdf <resume_file> [OPTIONS]

Options:
  --output TEXT        Output PDF file path (default: resume.pdf)
```

#### View Resume
```bash
python Main.py view <resume_file>
```

#### Convert Resume Format
```bash
python Main.py convert <input_file> <output_file>
```

### Web Interface

The web interface provides a user-friendly way to create and manage resumes.

#### Start the Web Server

```bash
python app.py
```

Then open your browser and navigate to `http://localhost:5000`

#### Features

- **Home Page** - Overview of features and quick start options
- **Dashboard** - View all your saved resumes
  - View resume details
  - Edit existing resumes
  - Download as PDF
  - Delete resumes
- **Create Resume** - Form-based resume creation
  - Personal information (name, email, phone, location, social links)
  - Professional summary
  - Work experience (multiple entries)
  - Education (multiple entries)
  - Skills (categorized)
  - Languages (with proficiency levels)
  - Certifications
- **View Resume** - Pretty formatted resume display
- **Edit Resume** - Update resume information anytime
- **PDF Export** - Download resume as professional PDF

#### Web Interface Routes

- `/` - Home page
- `/dashboard` - View all resumes
- `/create` - Create new resume
- `/resume/<filename>` - View resume
- `/resume/<filename>/edit` - Edit resume
- `/resume/<filename>/pdf` - Download PDF
- `/resume/<filename>/delete` - Delete resume

### Python API

```python
from resume_generator.resume import Resume, ContactInfo, Experience, Education, Skill
from resume_generator.pdf_generator import PDFGenerator

# Create contact information
contact = ContactInfo(
    name="John Doe",
    email="john@example.com",
    phone="+1-234-567-8900",
    location="San Francisco, CA"
)

# Create resume
resume = Resume(contact)

# Add professional summary
resume.set_summary("Experienced developer with passion for building great products")

# Add work experience
exp = Experience(
    company="Tech Corp",
    position="Senior Engineer",
    start_date="Jan 2020",
    end_date="Present",
    current=True,
    description=[
        "Led development of core platform",
        "Mentored junior developers"
    ]
)
resume.add_experience(exp)

# Add education
edu = Education(
    school="State University",
    degree="Bachelor of Science",
    field="Computer Science",
    graduation_date="May 2019",
    gpa="3.8"
)
resume.add_education(edu)

# Add skills
skills = Skill(
    category="Backend",
    skills=["Python", "Django", "PostgreSQL"]
)
resume.add_skill(skills)

# Save as JSON
resume.save_json("my_resume.json")

# Generate PDF
generator = PDFGenerator()
generator.generate(resume, "my_resume.pdf")
```

## Resume JSON Structure

```json
{
  "contact_info": {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+1-234-567-8900",
    "location": "San Francisco, CA",
    "website": "https://example.com",
    "linkedin": "https://linkedin.com/in/johndoe",
    "github": "https://github.com/johndoe"
  },
  "summary": "Professional summary text...",
  "experience": [
    {
      "company": "Company Name",
      "position": "Job Title",
      "start_date": "Jan 2020",
      "end_date": "Present",
      "current": true,
      "description": ["Achievement 1", "Achievement 2"]
    }
  ],
  "education": [
    {
      "school": "University Name",
      "degree": "Degree",
      "field": "Field of Study",
      "graduation_date": "May 2019",
      "gpa": "3.8",
      "honors": ["Honor 1", "Honor 2"]
    }
  ],
  "skills": [
    {
      "category": "Category Name",
      "skills": ["Skill 1", "Skill 2"]
    }
  ],
  "projects": [
    {
      "title": "Project Name",
      "description": "Project description",
      "technologies": ["Tech 1", "Tech 2"],
      "link": "https://project.link",
      "date": "2021"
    }
  ],
  "certifications": ["Certification 1", "Certification 2"],
  "languages": {
    "English": "Native",
    "Spanish": "Fluent"
  }
}
```

## Templates

The resume generator supports multiple templates:

1. **Professional** - Classic professional style (default)
2. **Modern** - Contemporary design with accent colors
3. **Academic** - Research-focused layout
4. **Creative** - Colorful and unique design

## Project Structure

```
resume-generator/
├── Main.py                 # CLI entry point
├── app.py                  # Flask web application
├── requirements.txt        # Python dependencies
├── setup.py               # Package setup configuration
├── README.md              # This file
├── CONTRIBUTING.md        # Contribution guidelines
├── .gitignore             # Git ignore rules
├── .vscode/
│   └── settings.json      # VS Code settings
├── resume_generator/
│   ├── __init__.py        # Package initialization
│   ├── resume.py          # Core Resume class
│   ├── pdf_generator.py   # PDF generation module
│   ├── cli.py             # Command-line interface
│   └── templates.py       # Template configurations
├── templates/             # Flask HTML templates
│   ├── index.html         # Home page
│   ├── dashboard.html     # Resume dashboard
│   ├── create.html        # Create resume form
│   ├── view_resume.html   # Resume preview
│   ├── edit_resume.html   # Edit resume form
│   ├── 404.html           # Error page
│   └── 500.html           # Server error page
├── static/                # Static files
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   └── js/
│       ├── main.js        # Main JavaScript
│       └── form.js        # Form handling
├── uploads/               # Uploaded files directory
├── resumes/               # Saved resume files
└── tests/
    ├── __init__.py
    └── test_resume.py     # Unit tests
```

## Dependencies

- **Flask** - Web framework
- **reportlab** - PDF generation
- **Pillow** - Image processing
- **PyYAML** - YAML parsing
- **jinja2** - Template engine (included with Flask)
- **click** - CLI framework
- **colorama** - Colored terminal output
- **Werkzeug** - WSGI utilities

## Testing

Run the test suite:
```bash
python -m pytest tests/
```

Or run tests directly:
```bash
python tests/test_resume.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

## Roadmap

- [x] Web interface for resume builder
- [ ] Add YAML resume format support
- [ ] Add docx format generation
- [ ] Resume templates customization
- [ ] Job application tracking feature
- [ ] Resume parsing from PDF
- [ ] LinkedIn integration
- [ ] ATS optimization suggestions
- [ ] Syntax highlighting in terminal
- [ ] Resume versioning
- [ ] Dark mode UI
- [ ] Drag-and-drop resume sections
- [ ] Export to Google Docs

## Changelog

### Version 1.1.0 (Web Interface)
- Added Flask web application
- Professional web UI with responsive design
- Dashboard for managing multiple resumes
- Form-based resume creation
- Live resume preview
- Edit resume functionality
- Beautiful styling with CSS
- Form validation and error handling

### Version 1.0.0
- Initial release
- Basic resume creation and management
- PDF generation
- JSON storage format
- Multiple templates support
- CLI interface

---

**Made with ❤️ for your career success**
