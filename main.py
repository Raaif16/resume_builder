from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Employee, Skill, Project, Personal, Education
from resume_pdf import create_resume
from fastapi.staticfiles import StaticFiles

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

@app.get("/resume/{employee_name}")
def generate_resume(employee_name: str, db: Session = Depends(get_db)):

    employee = db.query(Employee).filter(
        Employee.name == employee_name
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    skills = db.query(Skill).filter(
        Skill.employee_id == employee.id
    ).all()

    projects = db.query(Project).filter(
        Project.employee_id == employee.id
    ).all()

    personal_info = db.query(Personal).filter(
        Personal.employee_id == employee.id
    ).first()

    education = db.query(Education).filter(
        Education.employee_id == employee.id
    ).first()

    pdf_path = create_resume(employee, skills, projects, personal_info, education)

    return FileResponse(pdf_path, filename="resume.pdf")

app.mount("/", StaticFiles(directory="static", html=True), name="static")

