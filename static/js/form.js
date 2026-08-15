// Form manipulation functions
let experienceCount = 0;
let educationCount = 0;
let skillCount = 0;
let languageCount = 0;
let certificationCount = 0;

function addExperience() {
    const container = document.getElementById('experienceContainer');
    const id = experienceCount++;
    
    const html = `
        <div class="form-section nested" id="experience-${id}">
            <button type="button" class="btn btn-danger btn-small float-right" onclick="removeElement('experience-${id}')">
                <i class="fas fa-trash"></i> Remove
            </button>
            <h3>Work Experience ${id + 1}</h3>
            <div class="form-row">
                <div class="form-group">
                    <label>Company</label>
                    <input type="text" name="experiences[${id}].company" placeholder="Company Name" required>
                </div>
                <div class="form-group">
                    <label>Position</label>
                    <input type="text" name="experiences[${id}].position" placeholder="Job Title" required>
                </div>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label>Start Date</label>
                    <input type="text" name="experiences[${id}].start_date" placeholder="Jan 2020" required>
                </div>
                <div class="form-group">
                    <label>End Date</label>
                    <input type="text" name="experiences[${id}].end_date" placeholder="Present">
                </div>
            </div>
            <div class="form-group">
                <label>
                    <input type="checkbox" name="experiences[${id}].current"> Currently working here
                </label>
            </div>
            <div class="form-group full-width">
                <label>Achievements (one per line)</label>
                <textarea name="experiences[${id}].description" rows="3" placeholder="Bullet point 1&#10;Bullet point 2&#10;Bullet point 3"></textarea>
            </div>
        </div>
    `;
    
    container.insertAdjacentHTML('beforeend', html);
}

function addEducation() {
    const container = document.getElementById('educationContainer');
    const id = educationCount++;
    
    const html = `
        <div class="form-section nested" id="education-${id}">
            <button type="button" class="btn btn-danger btn-small float-right" onclick="removeElement('education-${id}')">
                <i class="fas fa-trash"></i> Remove
            </button>
            <h3>Education ${id + 1}</h3>
            <div class="form-row">
                <div class="form-group">
                    <label>School/University</label>
                    <input type="text" name="education[${id}].school" placeholder="University Name" required>
                </div>
                <div class="form-group">
                    <label>Degree</label>
                    <input type="text" name="education[${id}].degree" placeholder="Bachelor of Science" required>
                </div>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label>Field of Study</label>
                    <input type="text" name="education[${id}].field" placeholder="Computer Science" required>
                </div>
                <div class="form-group">
                    <label>Graduation Date</label>
                    <input type="text" name="education[${id}].graduation_date" placeholder="May 2019" required>
                </div>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label>GPA (optional)</label>
                    <input type="text" name="education[${id}].gpa" placeholder="3.8">
                </div>
                <div class="form-group">
                    <label>Honors (optional)</label>
                    <input type="text" name="education[${id}].honors" placeholder="Magna Cum Laude, Dean's List">
                </div>
            </div>
        </div>
    `;
    
    container.insertAdjacentHTML('beforeend', html);
}

function addSkill() {
    const container = document.getElementById('skillsContainer');
    const id = skillCount++;
    
    const html = `
        <div class="form-section nested" id="skill-${id}">
            <button type="button" class="btn btn-danger btn-small float-right" onclick="removeElement('skill-${id}')">
                <i class="fas fa-trash"></i> Remove
            </button>
            <h3>Skill Category ${id + 1}</h3>
            <div class="form-row">
                <div class="form-group full-width">
                    <label>Category Name</label>
                    <input type="text" name="skills[${id}].category" placeholder="e.g., Backend, Frontend, Tools" required>
                </div>
            </div>
            <div class="form-group full-width">
                <label>Skills (comma-separated)</label>
                <input type="text" name="skills[${id}].skills" placeholder="Python, Django, PostgreSQL" required>
            </div>
        </div>
    `;
    
    container.insertAdjacentHTML('beforeend', html);
}

function addLanguage() {
    const container = document.getElementById('languagesContainer');
    const id = languageCount++;
    
    const html = `
        <div class="form-row nested" id="language-${id}">
            <div class="form-group">
                <label>Language</label>
                <input type="text" name="languages.${id}.language" placeholder="English" required>
            </div>
            <div class="form-group">
                <label>Proficiency</label>
                <select name="languages.${id}.proficiency" required>
                    <option value="">Select...</option>
                    <option value="Native">Native</option>
                    <option value="Fluent">Fluent</option>
                    <option value="Intermediate">Intermediate</option>
                    <option value="Basic">Basic</option>
                </select>
            </div>
            <div class="form-group">
                <button type="button" class="btn btn-danger btn-small" onclick="removeElement('language-${id}')">
                    <i class="fas fa-trash"></i> Remove
                </button>
            </div>
        </div>
    `;
    
    container.insertAdjacentHTML('beforeend', html);
}

function addCertification() {
    const container = document.getElementById('certificationsContainer');
    const id = certificationCount++;
    
    const html = `
        <div class="form-row nested" id="certification-${id}">
            <div class="form-group full-width">
                <input type="text" name="certifications.${id}" placeholder="Certification Name" required>
                <button type="button" class="btn btn-danger btn-small" onclick="removeElement('certification-${id}')">
                    <i class="fas fa-trash"></i> Remove
                </button>
            </div>
        </div>
    `;
    
    container.insertAdjacentHTML('beforeend', html);
}

function removeElement(id) {
    const element = document.getElementById(id);
    if (element) {
        element.remove();
    }
}

// Form submission
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('resumeForm');
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            submitResume();
        });
    }
});

function submitResume() {
    const form = document.getElementById('resumeForm');
    const formData = new FormData(form);
    
    // Parse form data into structured object
    const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        phone: formData.get('phone'),
        location: formData.get('location'),
        website: formData.get('website') || null,
        linkedin: formData.get('linkedin') || null,
        github: formData.get('github') || null,
        summary: formData.get('summary') || null,
        experiences: parseMultipleFields(form, 'experiences'),
        education: parseMultipleFields(form, 'education'),
        skills: parseSkills(form),
        languages: parseLanguages(form),
        certifications: parseCertifications(form),
        projects: []
    };
    
    // Show loading state
    const submitBtn = form.querySelector('button[type="submit"]');
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Creating...';
    
    fetch('/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            showNotification('Resume created successfully!', 'success');
            setTimeout(() => {
                window.location.href = '/dashboard';
            }, 1500);
        } else {
            showNotification('Error: ' + result.error, 'error');
        }
    })
    .catch(error => {
        showNotification('Error: ' + error, 'error');
    })
    .finally(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<i class="fas fa-save"></i> Create Resume';
    });
}

function parseMultipleFields(form, fieldName) {
    const items = [];
    const inputs = form.querySelectorAll(`[name*="${fieldName}["]`);
    
    // Group by index
    const grouped = {};
    inputs.forEach(input => {
        const match = input.name.match(/\[(\d+)\]\.(\w+)/);
        if (match) {
            const index = match[1];
            const key = match[2];
            
            if (!grouped[index]) grouped[index] = {};
            
            if (key === 'description' || key === 'honors') {
                grouped[index][key] = input.value.split('\n').filter(v => v.trim());
            } else if (key === 'current') {
                grouped[index][key] = input.checked;
            } else {
                grouped[index][key] = input.value;
            }
        }
    });
    
    return Object.values(grouped);
}

function parseSkills(form) {
    const skills = [];
    const inputs = form.querySelectorAll('[name*="skills["]');
    
    const grouped = {};
    inputs.forEach(input => {
        const match = input.name.match(/skills\[(\d+)\]\.(\w+)/);
        if (match) {
            const index = match[1];
            const key = match[2];
            
            if (!grouped[index]) grouped[index] = {};
            
            if (key === 'skills') {
                grouped[index][key] = input.value.split(',').map(s => s.trim()).filter(s => s);
            } else {
                grouped[index][key] = input.value;
            }
        }
    });
    
    return Object.values(grouped);
}

function parseLanguages(form) {
    const languages = {};
    let index = 0;
    
    while (true) {
        const langInput = form.querySelector(`[name="languages.${index}.language"]`);
        const profInput = form.querySelector(`[name="languages.${index}.proficiency"]`);
        
        if (!langInput || !profInput) break;
        
        if (langInput.value && profInput.value) {
            languages[langInput.value] = profInput.value;
        }
        index++;
    }
    
    return languages;
}

function parseCertifications(form) {
    const certifications = [];
    let index = 0;
    
    while (true) {
        const certInput = form.querySelector(`[name="certifications.${index}"]`);
        if (!certInput) break;
        
        if (certInput.value) {
            certifications.push(certInput.value);
        }
        index++;
    }
    
    return certifications;
}

function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i>
        ${message}
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}
