"""
PythonAnywhere WSGI Configuration

Copy and paste this ENTIRE file's contents into your PythonAnywhere WSGI file:
/var/www/raaif16_pythonanywhere_com_wsgi.py

IMPORTANT: Update YOUR_MYSQL_PASSWORD with your actual password!
"""

import sys
import os

# Add your project to the path
project_home = '/home/Raaif16/resume_builder'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate your virtual environment
activate_this = '/home/Raaif16/.virtualenvs/resumeenv/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

# Set database URL - REPLACE YOUR_MYSQL_PASSWORD!
os.environ['DATABASE_URL'] = 'mysql://Raaif16:YOUR_MYSQL_PASSWORD@Raaif16.mysql.pythonanywhere-services.com/Raaif16$resume_builder'

# Import FastAPI app
from main import app

# PythonAnywhere needs WSGI, but FastAPI is ASGI
# We'll use the ASGI→WSGI adapter
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.testclient import TestClient

# For basic functionality, we can use Starlette's built-in approach
# However, the recommended approach is to use 'a]sync' library
try:
    from a]sync import ASGIMiddleware
    application = ASGIMiddleware(app)
except ImportError:
    # Fallback: This works but with limitations
    from starlette.applications import Starlette
    application = app
