from sqlalchemy import Column, Integer, String, Text
from db import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    summary = Column(Text)


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    skill = Column(String)


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    project_name = Column(String)
    role = Column(String)
    description = Column(Text)
