import json


# ==========================================
# LOAD CAREER KNOWLEDGE BASE
# ==========================================

JSON_PATH = "data/career_skills.json"

with open(JSON_PATH, "r") as f:
    career_data = json.load(f)


# ==========================================
# COURSE RECOMMENDATION
# ==========================================

def get_recommended_courses(predicted_career):
    """
    Return recommended courses
    for predicted career
    """

    return career_data[predicted_career][
        "recommended_courses"
    ]


# ==========================================
# CERTIFICATION RECOMMENDATION
# ==========================================

def get_certifications(predicted_career):
    """
    Return certifications
    for predicted career
    """

    return career_data[predicted_career][
        "certifications"
    ]


# ==========================================
# PERSONALIZED SKILL IMPROVEMENT
# ==========================================

def generate_skill_suggestions(priority_skills):
    """
    Generate personalized suggestions
    based on skill gaps
    """

    suggestions = []

    skill_advice = {

        "Programming_Skill":
            "Practice coding regularly using Python and problem-solving platforms.",

        "DBMS_Knowledge":
            "Improve database concepts and SQL query writing.",

        "Computer_Networks":
            "Strengthen networking fundamentals and protocols.",

        "Mathematics_Statistics":
            "Improve statistics and logical reasoning fundamentals.",

        "Web_Development":
            "Build mini frontend/backend web projects.",

        "App_Development":
            "Practice mobile app development using modern frameworks.",

        "Data_Analysis":
            "Work with datasets and practice data analysis techniques.",

        "Cybersecurity":
            "Learn security fundamentals and ethical hacking basics.",

        "Cloud_DevOps":
            "Learn cloud platforms and DevOps fundamentals.",

        "UI_UX_Design":
            "Practice wireframing and user-centered design.",

        "Testing_Debugging":
            "Practice software testing and debugging methods.",

        "Problem_Solving":
            "Improve aptitude and coding problem-solving ability.",

        "Analytical_Thinking":
            "Practice analytical case studies and reasoning exercises.",

        "Creativity":
            "Improve creativity through design and brainstorming tasks.",

        "Communication_Skill":
            "Practice presentations and communication skills.",

        "Leadership":
            "Participate in team activities and leadership roles.",

        "Teamwork":
            "Work on collaborative projects to improve teamwork."
    }

    for skill in priority_skills.keys():

        if skill in skill_advice:
            suggestions.append(
                skill_advice[skill]
            )

    return suggestions