---
title: Resume Builder
emoji: 📄
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: mit
---

# Resume Builder API

A FastAPI-based resume builder application that allows you to:
- Create employee profiles with skills, education, and projects
- Generate PDF resumes

## API Endpoints

- `POST /employee` - Create a new employee profile
- `GET /resume/{employee_name}` - Generate and download a PDF resume
- `GET /docs` - Swagger UI documentation
