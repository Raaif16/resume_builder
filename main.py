from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from db import SessionLocal
from models import Employee, Skill, Project
from resume_pdf import create_resume

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

@app.get("/resume/{employee_id}")
def generate_resume(employee_id: str, db: Session = Depends(get_db)):

    employee = db.query(Employee).filter(
        Employee.employee_id == employee_id
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    skills = db.query(Skill).filter(
        Skill.employee_id == employee.id
    ).all()

    projects = db.query(Project).filter(
        Project.employee_id == employee.id
    ).all()

    pdf_path = create_resume(employee, skills, projects)

    return FileResponse(pdf_path, filename="resume.pdf")
