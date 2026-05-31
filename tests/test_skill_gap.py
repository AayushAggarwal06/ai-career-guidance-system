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

predicted_career = "Data Analyst"

gap_report = analyze_skill_gap(
    student,
    predicted_career
)

priority_skills = get_priority_skills(
    gap_report
)

print("\nPriority Skill Gaps:\n")

for skill, details in priority_skills.items():
    print(
        f"{skill}: "
        f"Gap={details['gap']} "
        f"({details['severity']})"
    )