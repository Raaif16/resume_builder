from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_resume(employee, skills, projects):
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
    pdf.drawString(x, y, f"{employee.email} | {employee.phone}")
    y -= 30

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x, y, "Summary")
    y -= 20

    pdf.setFont("Helvetica", 10)
    pdf.drawString(x, y, employee.summary)
    y -= 30

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x, y, "Technical Skills")
    y -= 20

    pdf.setFont("Helvetica", 10)
    for skill in skills:
        pdf.drawString(x, y, f"- {skill.skill}")
        y -= 20
    y -= 10

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x, y, "Projects")
    y -= 20

    pdf.setFont("Helvetica", 10)
    for project in projects:
        pdf.drawString(x, y, project.project_name)
        y -= 20
        pdf.drawString(x + 25, y, f"Role: {project.role}")
        y -= 20
        pdf.drawString(x + 25, y, project.description)
        y -= 30
    pdf.save()
    return file_name
