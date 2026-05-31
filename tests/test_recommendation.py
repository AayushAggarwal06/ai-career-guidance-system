from utils.recommendation import (
    get_recommended_courses,
    get_certifications,
    generate_skill_suggestions
)

from utils.skill_gap import (
    analyze_skill_gap,
    get_priority_skills
)


student = {
    "Programming_Skill": 2,
    "DBMS_Knowledge": 2,
    "Computer_Networks": 2,
    "Mathematics_Statistics": 3,
    "Web_Development": 2,
    "App_Development": 1,
    "Data_Analysis": 3,
    "Cybersecurity": 1,
    "Cloud_DevOps": 1,
    "UI_UX_Design": 2,
    "Testing_Debugging": 2,
    "Problem_Solving": 4,
    "Analytical_Thinking": 4,
    "Creativity": 3,
    "Communication_Skill": 4,
    "Leadership": 2,
    "Teamwork": 4
}

career = "Data Analyst"

# Skill gap analysis
gap_report = analyze_skill_gap(
    student,
    career
)

priority_skills = get_priority_skills(
    gap_report
)

# Recommendations
courses = get_recommended_courses(
    career
)

certifications = get_certifications(
    career
)

suggestions = generate_skill_suggestions(
    priority_skills
)

print("\nRecommended Courses:")
for c in courses:
    print("-", c)

print("\nRecommended Certifications:")
for c in certifications:
    print("-", c)

print("\nSkill Improvement Suggestions:")
for s in suggestions:
    print("-", s)