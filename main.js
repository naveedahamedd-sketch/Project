// Main JavaScript file

// Notification styling
const style = document.createElement('style');
style.textContent = `
    .notification {
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        border-radius: 4px;
        color: white;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        display: flex;
        align-items: center;
        gap: 0.75rem;
        z-index: 1000;
        animation: slideIn 0.3s ease-out;
    }
    
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    .notification-success {
        background-color: #27ae60;
    }
    
    .notification-error {
        background-color: #e74c3c;
    }
    
    .notification-info {
        background-color: #3498db;
    }
    
    .float-right {
        float: right;
        margin-left: auto;
    }
    
    .nested {
        background-color: #f8f9fa;
        padding: 1rem !important;
        border-left: 4px solid #3498db;
        margin-bottom: 1rem !important;
    }
`;
document.head.appendChild(style);

// Smooth scroll for links
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Form helper functions
function formatFormData(form) {
    const formData = new FormData(form);
    const data = {};
    
    formData.forEach((value, key) => {
        if (key.includes('[')) {
            // Handle nested fields
            const match = key.match(/(\w+)\[(\d+)\]\.(\w+)/);
            if (match) {
                const [, arrayName, index, fieldName] = match;
                if (!data[arrayName]) data[arrayName] = [];
                if (!data[arrayName][index]) data[arrayName][index] = {};
                data[arrayName][index][fieldName] = value;
            }
        } else {
            data[key] = value;
        }
    });
    
    return data;
}

// Active nav link
function setActiveNavLink() {
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

setActiveNavLink();

// Responsive menu toggle
function toggleMenu() {
    const menu = document.querySelector('.nav-menu');
    if (menu) {
        menu.classList.toggle('active');
    }
}

// Print functionality
function printResume() {
    window.print();
}

// Export to JSON
function exportJSON(data, filename) {
    const jsonString = JSON.stringify(data, null, 2);
    const blob = new Blob([jsonString], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename + '.json';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
}
