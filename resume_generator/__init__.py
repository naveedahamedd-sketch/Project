"""
Resume Generator Package
A professional tool for generating beautiful resumes in multiple formats
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .resume import Resume
from .pdf_generator import PDFGenerator

__all__ = ["Resume", "PDFGenerator", "__version__"]
