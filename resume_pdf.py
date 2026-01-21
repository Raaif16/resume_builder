from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from textwrap import wrap

def create_resume(employee, skills, projects, personal_info, education):
    file_name = "resume.pdf"
    pdf = canvas.Canvas(file_name, pagesize=A4)

    width, height = A4
    x = 40
    y = 800

    pdf.setFont("Times-Bold", 20)
    pdf.drawCentredString(width/2, y, "Curriculum Vitae")
    y -= 20

    pdf.line(x, y, width - x, y) 
    y -= 30

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(x, y, employee.name)
    y -= 20
    
    pdf.setFont("Helvetica", 10)
    pdf.drawString(x + 5, y, employee.email)
    y -= 15
    pdf.drawString(x + 5, y, employee.phone)
    y -= 30

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x, y, "Personal Information")
    y -= 20

    pdf.setFont("Helvetica", 10)
    pdf.drawString(x + 5, y, f"D.O.B: {personal_info.dob}")
    y -= 15
    pdf.drawString(x + 5, y, f"Address: {personal_info.address}")
    y -= 15
    pdf.drawString(x + 5, y, f"Gender: {personal_info.gender}")
    y -= 30

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x, y, "Career Objective")
    y -= 20

    pdf.setFont("Helvetica", 10)
    max_chars = 110
    lines = wrap(employee.summary, max_chars)

    for line in lines:
        pdf.drawString(x + 5, y, line)
        y -= 14
    y -= 16

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x, y, "Education")
    y -= 20

    pdf.setFont("Helvetica", 10)
    pdf.drawString(x + 5, y, f"Degree: {education.degree}")
    y -= 15
    pdf.drawString(x + 5, y, f"Institution: {education.institution}")
    y -= 15
    pdf.drawString(x + 5, y, f"Year Of Passing: {education.year_of_passing}")
    y -= 30

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x, y, "Technical Skills")
    y -= 20

    pdf.setFont("Helvetica", 10)
    for skill in skills:
        pdf.drawString(x + 5, y, f"- {skill.skill}")
        y -= 20
    y -= 10

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x, y, "Projects")
    y -= 20

    pdf.setFont("Helvetica", 10)
    for project in projects:
        pdf.drawString(x + 5, y, project.project_name)
        y -= 20
        pdf.drawString(x + 25, y, f"Role: {project.role}")
        y -= 20

        max_chars = 110
        lines = wrap(project.description, max_chars)

        for line in lines:
            pdf.drawString(x + 25, y, line)
            y -= 14
        y -= 16

    pdf.save()
    return file_name
