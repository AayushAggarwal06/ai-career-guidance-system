import json


# ==========================================
# LOAD CAREER KNOWLEDGE BASE
# ==========================================

JSON_PATH = "data/career_skills.json"

with open(JSON_PATH, "r") as f:
    career_data = json.load(f)


# ==========================================
# GAP SEVERITY FUNCTION
# ==========================================

def get_gap_severity(gap):

    if gap <= 2:
        return "Low"

    elif gap <= 5:
        return "Medium"

    else:
        return "High"


# ==========================================
# SKILL GAP ANALYSIS
# ==========================================

def analyze_skill_gap(student_data, predicted_career):
    """
    Compare student skills with
    required skills of predicted career
    """

    career_info = career_data[predicted_career]

    required_skills = career_info["required_skills"]

    skill_gap_report = {}

    for skill, required_value in required_skills.items():

        student_value = student_data.get(skill, 0)

        gap = max(0, required_value - student_value)

        severity = get_gap_severity(gap)

        skill_gap_report[skill] = {
            "student_score": student_value,
            "required_score": required_value,
            "gap": gap,
            "severity": severity
        }

    return skill_gap_report


# ==========================================
# FILTER IMPORTANT GAPS
# ==========================================

def get_priority_skills(skill_gap_report):
    """
    Return only Medium & High gap skills
    """

    priority_skills = {}

    for skill, details in skill_gap_report.items():

        if details["severity"] in ["Medium", "High"]:

            priority_skills[skill] = details

    return priority_skills