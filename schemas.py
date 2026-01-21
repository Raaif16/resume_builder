from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ProjectBase(BaseModel):
    project_name: str
    role: str
    description: str

class SkillBase(BaseModel):
    skill: str

class EducationBase(BaseModel):
    degree: str
    institution: str
    year_of_passing: int

class PersonalBase(BaseModel):
    dob: date
    gender: str
    address: str

class EmployeeCreate(BaseModel):
    name: str
    email: str
    phone: str
    summary: str
    personal: PersonalBase
    education: EducationBase
    skills: List[SkillBase]
    projects: List[ProjectBase]
