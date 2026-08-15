# Web Interface Guide

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Starting the Web Server

#### Windows
```bash
run_web.bat
```

#### Linux/Mac
```bash
bash run_web.sh
```

#### Manual Start
```bash
python app.py
```

Once started, open your browser and navigate to:
```
http://localhost:5000
```

## Features Overview

### 🏠 Home Page (`/`)
- Overview of Resume Generator features
- Quick start options
- Feature highlights
- Links to create new resume or view dashboard

### 📊 Dashboard (`/dashboard`)
The dashboard is your resume management hub where you can:

- **View All Resumes** - See all your created resumes at a glance
- **Quick Actions** - For each resume:
  - 👁️ **View** - See resume details
  - ✏️ **Edit** - Modify resume information
  - 📥 **Download PDF** - Export as PDF file
  - 🗑️ **Delete** - Remove resume

### ✍️ Create Resume (`/create`)
Comprehensive form to create a new resume with sections for:

1. **Personal Information**
   - Full Name (required)
   - Email (required)
   - Phone Number (required)
   - Location (required)
   - Website (optional)
   - LinkedIn Profile (optional)
   - GitHub Profile (optional)

2. **Professional Summary**
   - Brief overview of your professional background
   - Highlight key strengths and career goals

3. **Work Experience**
   - Add multiple jobs
   - Company name
   - Job title/position
   - Start and end dates
   - Current employment checkbox
   - Detailed achievements (bullet points)

4. **Education**
   - School/University
   - Degree
   - Field of Study
   - Graduation date
   - GPA (optional)
   - Honors (optional)

5. **Skills**
   - Organize by category (e.g., Backend, Frontend, Tools)
   - Comma-separated skill list
   - Add multiple skill categories

6. **Languages**
   - Language name
   - Proficiency level (Native, Fluent, Intermediate, Basic)
   - Add multiple languages

7. **Certifications**
   - Professional certifications and credentials
   - Add multiple certifications

### 👁️ View Resume (`/resume/<filename>`)
Professional resume preview featuring:

- Contact information display
- Professional summary
- Work experience with dates
- Education details
- Skills organized by category
- Languages and proficiency
- Certifications list
- Beautiful, printer-friendly formatting

**Actions Available:**
- ← Back to Dashboard
- ✏️ Edit Resume
- 📥 Download as PDF

### ✏️ Edit Resume (`/resume/<filename>/edit`)
Update existing resume information:

- All personal contact details can be updated
- Professional summary can be edited
- Navigate back to dashboard to save

### 📄 PDF Export

Generate professional PDF resumes suitable for job applications:

- **One-Click Download** - Download directly from view or dashboard
- **Professional Formatting** - Proper fonts and spacing
- **Print-Ready** - Optimized for printing
- **ATS-Friendly** - Clean, parseable format
- **Auto-Named** - Downloads with your name

## Usage Examples

### Creating Your First Resume

1. Click "Create New Resume" button
2. Fill in your personal information
3. Add your professional summary
4. Add work experience entries
5. Add education details
6. Add your skills by category
7. Add any certifications
8. Click "Create Resume"
9. You'll be redirected to the dashboard

### Downloading Your Resume as PDF

1. Go to Dashboard
2. Find your resume
3. Click the download button (📥)
4. Resume will download as PDF to your Downloads folder

### Editing Your Resume

1. Go to Dashboard
2. Find your resume
3. Click the edit button (✏️)
4. Modify your information
5. Click "Save Changes"

### Deleting a Resume

1. Go to Dashboard
2. Find your resume
3. Click the delete button (🗑️)
4. Confirm deletion in the popup

## Tips & Tricks

### Best Practices

1. **Professional Summary**
   - Keep it concise (2-3 sentences)
   - Highlight your key strengths
   - Tailor to the job you're applying for

2. **Work Experience**
   - Use action verbs (Led, Managed, Developed, etc.)
   - Quantify achievements when possible
   - Start with most recent job

3. **Skills Organization**
   - Group related skills by category
   - Put most relevant skills first
   - Use industry-standard terminology

4. **Education**
   - Include relevant coursework if applicable
   - Add honors and achievements
   - Include GPA if 3.5 or higher

### Content Tips

- **Be Specific** - Instead of "Improved system", say "Improved system performance by 40%"
- **Action-Oriented** - Start bullet points with action verbs
- **Customized** - Tailor each resume version to the job posting
- **Keep It Current** - Update your resume regularly
- **Proofread** - Check for typos and grammar errors

## File Organization

Resume files are automatically saved in the `resumes/` directory as:
```
resumes/
├── john_doe_20240815_120000.json
├── john_doe_20240815_120000.pdf
├── jane_smith_20240815_110000.json
└── jane_smith_20240815_110000.pdf
```

## Troubleshooting

### Issue: "Cannot connect to localhost:5000"

**Solution:**
1. Ensure the web server is running
2. Check that port 5000 is not in use
3. Try restarting the server

### Issue: Changes not saving

**Solution:**
1. Ensure you clicked "Save Changes" button
2. Check browser console for errors (F12)
3. Try refreshing the page

### Issue: PDF not generating

**Solution:**
1. Ensure reportlab is installed: `pip install reportlab`
2. Check that resume has all required fields
3. Try downloading again

### Issue: File not found error

**Solution:**
1. Clear browser cache
2. Go back to dashboard
3. Try accessing resume again

## Performance Tips

- **Use Chrome/Firefox** for best performance
- **Clear Browser Cache** if experiencing issues
- **Save Multiple Versions** for different job applications
- **Regular Backups** - Download PDF copies regularly

## Security Notes

- All resumes are stored locally on your machine
- Data is not sent to external servers (offline-first)
- Use HTTPS if deploying to production
- Protect your resume files

## Keyboard Shortcuts

- `Ctrl+S` - Save form (if implemented)
- `Escape` - Cancel form
- `Tab` - Navigate form fields
- `Enter` - Submit form

## API Endpoints

For advanced users, these API endpoints are available:

- `GET /` - Home page
- `GET /dashboard` - Resume list
- `GET /create` - Create form
- `POST /create` - Submit new resume
- `GET /resume/<filename>` - View resume
- `GET /resume/<filename>/preview` - JSON preview
- `GET /resume/<filename>/pdf` - Download PDF
- `GET /resume/<filename>/edit` - Edit form
- `POST /resume/<filename>/edit` - Update resume
- `DELETE /resume/<filename>` - Delete resume

## Getting Help

For issues or questions:
1. Check README.md for general information
2. Review this guide for common tasks
3. Open an issue on GitHub
4. Check the project's FAQ

---

**Happy resume building! 🚀**
