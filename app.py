"""
Flask Web Application for Resume Generator
"""

import os
import json
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
from werkzeug.utils import secure_filename
from resume_generator.resume import Resume, ContactInfo, Experience, Education, Skill, Project
from resume_generator.pdf_generator import PDFGenerator

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESUME_FOLDER'] = 'resumes'

# Create necessary directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESUME_FOLDER'], exist_ok=True)


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    """Dashboard showing all resumes"""
    resumes = []
    resume_path = Path(app.config['RESUME_FOLDER'])
    
    if resume_path.exists():
        for file in resume_path.glob('*.json'):
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    resumes.append({
                        'name': file.stem,
                        'filename': file.name,
                        'contact_name': data.get('contact_info', {}).get('name', 'Unknown'),
                        'created_at': data.get('created_at', '')
                    })
            except:
                pass
    
    return render_template('dashboard.html', resumes=resumes)


@app.route('/create', methods=['GET', 'POST'])
def create():
    """Create new resume"""
    if request.method == 'GET':
        return render_template('create.html')
    
    try:
        data = request.get_json()
        
        # Create contact info
        contact_info = ContactInfo(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            location=data.get('location'),
            website=data.get('website'),
            linkedin=data.get('linkedin'),
            github=data.get('github')
        )
        
        resume = Resume(contact_info)
        
        # Add summary if provided
        if data.get('summary'):
            resume.set_summary(data.get('summary'))
        
        # Add experiences
        for exp_data in data.get('experiences', []):
            exp = Experience(
                company=exp_data.get('company'),
                position=exp_data.get('position'),
                start_date=exp_data.get('start_date'),
                end_date=exp_data.get('end_date'),
                current=exp_data.get('current', False),
                description=exp_data.get('description', [])
            )
            resume.add_experience(exp)
        
        # Add education
        for edu_data in data.get('education', []):
            edu = Education(
                school=edu_data.get('school'),
                degree=edu_data.get('degree'),
                field=edu_data.get('field'),
                graduation_date=edu_data.get('graduation_date'),
                gpa=edu_data.get('gpa'),
                honors=edu_data.get('honors', [])
            )
            resume.add_education(edu)
        
        # Add skills
        for skill_data in data.get('skills', []):
            skill = Skill(
                category=skill_data.get('category'),
                skills=skill_data.get('skills', [])
            )
            resume.add_skill(skill)
        
        # Add projects
        for proj_data in data.get('projects', []):
            proj = Project(
                title=proj_data.get('title'),
                description=proj_data.get('description'),
                technologies=proj_data.get('technologies', []),
                link=proj_data.get('link'),
                date=proj_data.get('date')
            )
            resume.add_project(proj)
        
        # Add languages
        for lang, proficiency in data.get('languages', {}).items():
            resume.add_language(lang, proficiency)
        
        # Add certifications
        for cert in data.get('certifications', []):
            resume.add_certification(cert)
        
        # Save resume
        filename = secure_filename(contact_info.name.lower().replace(' ', '_'))
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filepath = os.path.join(app.config['RESUME_FOLDER'], f'{filename}_{timestamp}.json')
        
        resume.save_json(filepath)
        
        return jsonify({
            'success': True,
            'message': 'Resume created successfully!',
            'resume_id': os.path.basename(filepath)
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/resume/<filename>')
def view_resume(filename):
    """View resume details"""
    try:
        filepath = os.path.join(app.config['RESUME_FOLDER'], secure_filename(filename))
        
        if not os.path.exists(filepath):
            return redirect(url_for('dashboard'))
        
        resume = Resume.from_json(filepath)
        return render_template('view_resume.html', resume=resume, filename=filename)
    
    except Exception as e:
        return redirect(url_for('dashboard'))


@app.route('/resume/<filename>/preview')
def preview_resume(filename):
    """Preview resume as JSON"""
    try:
        filepath = os.path.join(app.config['RESUME_FOLDER'], secure_filename(filename))
        
        if not os.path.exists(filepath):
            return jsonify({'error': 'Resume not found'}), 404
        
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        return jsonify(data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/resume/<filename>/pdf')
def download_pdf(filename):
    """Download resume as PDF"""
    try:
        filepath = os.path.join(app.config['RESUME_FOLDER'], secure_filename(filename))
        
        if not os.path.exists(filepath):
            return jsonify({'error': 'Resume not found'}), 404
        
        resume = Resume.from_json(filepath)
        
        # Generate PDF
        pdf_filename = os.path.splitext(filename)[0] + '.pdf'
        pdf_path = os.path.join(app.config['RESUME_FOLDER'], pdf_filename)
        
        generator = PDFGenerator()
        generator.generate(resume, pdf_path)
        
        return send_file(pdf_path, as_attachment=True, download_name=pdf_filename)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/resume/<filename>/edit', methods=['GET', 'POST'])
def edit_resume(filename):
    """Edit existing resume"""
    try:
        filepath = os.path.join(app.config['RESUME_FOLDER'], secure_filename(filename))
        
        if not os.path.exists(filepath):
            return redirect(url_for('dashboard'))
        
        if request.method == 'GET':
            with open(filepath, 'r') as f:
                resume_data = json.load(f)
            
            return render_template('edit_resume.html', resume_data=resume_data, filename=filename)
        
        # Handle POST request (update resume)
        data = request.get_json()
        
        # Load existing resume
        resume = Resume.from_json(filepath)
        
        # Update contact info
        resume.contact_info.name = data.get('name', resume.contact_info.name)
        resume.contact_info.email = data.get('email', resume.contact_info.email)
        resume.contact_info.phone = data.get('phone', resume.contact_info.phone)
        resume.contact_info.location = data.get('location', resume.contact_info.location)
        resume.contact_info.website = data.get('website')
        resume.contact_info.linkedin = data.get('linkedin')
        resume.contact_info.github = data.get('github')
        
        # Update summary
        resume.summary = data.get('summary')
        
        # Update experiences, education, skills, etc.
        resume.experiences = []
        for exp_data in data.get('experiences', []):
            exp = Experience(**exp_data)
            resume.add_experience(exp)
        
        resume.education = []
        for edu_data in data.get('education', []):
            edu = Education(**edu_data)
            resume.add_education(edu)
        
        resume.skills = []
        for skill_data in data.get('skills', []):
            skill = Skill(**skill_data)
            resume.add_skill(skill)
        
        # Save updated resume
        resume.save_json(filepath)
        
        return jsonify({'success': True, 'message': 'Resume updated successfully!'})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/resume/<filename>/delete', methods=['DELETE'])
def delete_resume(filename):
    """Delete a resume"""
    try:
        filepath = os.path.join(app.config['RESUME_FOLDER'], secure_filename(filename))
        
        if not os.path.exists(filepath):
            return jsonify({'error': 'Resume not found'}), 404
        
        os.remove(filepath)
        
        # Also remove associated PDF if it exists
        pdf_path = os.path.splitext(filepath)[0] + '.pdf'
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
        
        return jsonify({'success': True, 'message': 'Resume deleted successfully!'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/templates')
def get_templates():
    """Get available resume templates"""
    templates = [
        {'id': 'professional', 'name': 'Professional', 'description': 'Classic professional style'},
        {'id': 'modern', 'name': 'Modern', 'description': 'Contemporary design'},
        {'id': 'academic', 'name': 'Academic', 'description': 'Research-focused layout'},
        {'id': 'creative', 'name': 'Creative', 'description': 'Colorful and unique design'},
    ]
    return jsonify(templates)


@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
