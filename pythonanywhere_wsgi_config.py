"""
PythonAnywhere WSGI Configuration

Copy and paste this ENTIRE file's contents into your PythonAnywhere WSGI file:
/var/www/raaif16_pythonanywhere_com_wsgi.py
"""

import sys
import os

# Add your project to the path
project_home = '/home/Raaif16/resume_builder'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set database URL to SQLite (free tier compatible!)
os.environ['DATABASE_URL'] = 'sqlite:////home/Raaif16/resume_builder/resume.db'

# Import FastAPI app
from main import app

# PythonAnywhere needs WSGI, but FastAPI is ASGI
# Using the built-in adapter
application = app
