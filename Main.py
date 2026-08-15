#!/usr/bin/env python3
"""
Resume Generator CLI - Main Entry Point
A command-line tool to generate professional resumes in multiple formats
"""

import sys
import argparse
from resume_generator.cli import main

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
