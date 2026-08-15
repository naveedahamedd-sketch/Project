# Contributing to Resume Generator

Thank you for your interest in contributing to Resume Generator! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what's best for the community

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/resume-generator.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
5. Install dependencies: `pip install -r requirements.txt`

## Development Workflow

1. Create a new branch for your feature: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Write or update tests
4. Run tests: `python -m pytest tests/`
5. Commit with clear messages: `git commit -m "Add feature description"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Create a Pull Request

## Coding Standards

- Follow PEP 8 style guide
- Use type hints where possible
- Write docstrings for functions and classes
- Keep functions focused and small
- Add comments for complex logic

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for >80% code coverage
- Test both happy path and edge cases

## Pull Request Process

1. Update README.md if needed
2. Update CHANGELOG.md with your changes
3. Ensure CI/CD tests pass
4. Request review from maintainers
5. Address review feedback
6. Merge once approved

## Reporting Issues

When reporting bugs, include:
- Python version
- OS and version
- Exact error message
- Steps to reproduce
- Expected vs actual behavior

## Feature Requests

- Describe the use case clearly
- Provide examples or mockups
- Consider backwards compatibility
- Check for similar existing features

## Questions?

Feel free to open a discussion issue or contact the maintainers.

Happy coding! 🎉
