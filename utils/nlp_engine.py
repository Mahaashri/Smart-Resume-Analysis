import re
from PyPDF2 import PdfReader

# -----------------------------
# Role Based Required Skills
# -----------------------------

ROLE_SKILLS = {

    "fswd": {
        "frontend": ["html", "css", "javascript", "react", "angular", "vue"],
        "backend": ["python", "java", "node.js", "php", "flask", "django"],
        "database": ["sql", "mysql", "postgresql", "mongodb"],
        "tools": ["git"]
    },

    "cloud": {
        "cloud_platform": ["aws", "azure", "gcp"],
        "networking": ["vpc", "subnet", "load balancer"],
        "scripting": ["python", "bash"],
        "tools": ["terraform", "cloudformation"]
    },

    "devops": {
        "ci_cd": ["jenkins", "github actions"],
        "containers": ["docker", "kubernetes"],
        "cloud": ["aws"],
        "tools": ["terraform", "ansible", "linux", "git"]
    }
}

# -----------------------------
# Extract Resume Text
# -----------------------------

def extract_text_from_pdf(filepath):
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.lower()


# -----------------------------
# Detect Role From JD
# -----------------------------

def detect_role(job_description):

    jd = job_description.lower()

    if "full stack" in jd or "frontend" in jd:
        return "fswd"

    elif "cloud engineer" in jd:
        return "cloud"

    elif "devops" in jd:
        return "devops"

    else:
        return "fswd"   # default


# -----------------------------
# Extract Career Objective
# -----------------------------

def extract_career_objective(text):

    match = re.search(r"career objective(.*?)(skills|education|projects)", text, re.DOTALL)
    if match:
        return match.group(1)
    return ""


# -----------------------------
# Extract Skills Section
# -----------------------------

def extract_skills_section(text):

    match = re.search(r"skills(.*?)(education|projects|experience)", text, re.DOTALL)
    if match:
        return match.group(1)
    return ""


# -----------------------------
# Compare Resume vs Role
# -----------------------------

def analyze_resume(filepath, job_description):

    resume_text = extract_text_from_pdf(filepath)

    role = detect_role(job_description)
    required_skills = ROLE_SKILLS[role]

    objective_text = extract_career_objective(resume_text)
    skills_text = extract_skills_section(resume_text)

    missing_skills = {}
    matched_count = 0
    total_required = 0

    for category, skills in required_skills.items():

        missing_skills[category] = []

        for skill in skills:
            total_required += 1

            if skill in skills_text or skill in resume_text:
                matched_count += 1
            else:
                missing_skills[category].append(skill)

    score = int((matched_count / total_required) * 100)

    return role, score, missing_skills