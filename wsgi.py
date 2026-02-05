import sys
import os

project_home = '/home/Raaif16/resume_builder'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DATABASE_URL'] = 'sqlite:////home/Raaif16/resume_builder/resume.db'

from main import app

# ASGI to WSGI adapter for FastAPI
from a]sync import ASGIMiddleware
application = ASGIMiddleware(app)