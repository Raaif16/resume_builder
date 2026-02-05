"""
WSGI entry point for PythonAnywhere deployment.

Instructions:
1. In PythonAnywhere Web tab, edit the WSGI configuration file
2. Replace its contents with the code that imports from this file
3. See pythonanywhere_wsgi_config.py for the exact code to paste
"""
import sys
import os

# Add project directory to Python path
project_home = '/home/Raaif16/resume_builder'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set the database URL for PythonAnywhere MySQL
# Replace YOUR_PASSWORD with your actual MySQL password from PythonAnywhere
os.environ.setdefault(
    'DATABASE_URL',
    'mysql://Raaif16:YOUR_PASSWORD@Raaif16.mysql.pythonanywhere-services.com/Raaif16$resume_builder'
)

# Import the FastAPI app
from main import app
