from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(score, skills, missing):
    file_path = "report.pdf"
    doc = SimpleDocTemplate(file_path)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph(f"Resume Score: {score}%", styles["Heading1"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"Skills Found: {', '.join(skills)}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"Missing Skills: {', '.join(missing)}", styles["Normal"]))

    doc.build(elements)

    return file_path