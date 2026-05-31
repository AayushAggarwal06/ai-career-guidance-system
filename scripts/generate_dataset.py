import json
import random
import pandas as pd

# -----------------------------
# CONFIGURATION
# -----------------------------

TOTAL_SAMPLES = 3000
NOISE_LEVEL = 0.12  # 12% noise
OUTPUT_PATH = "data/synthetic_dataset.csv"
JSON_PATH = "data/career_skills.json"

# Preferred work type choices
WORK_TYPES = ["Technical", "Analytical", "Creative"]
WORK_STYLES = ["Individual", "Team"]


# -----------------------------
# LOAD CAREER KNOWLEDGE BASE
# -----------------------------

with open(JSON_PATH, "r") as f:
    career_data = json.load(f)

career_roles = list(career_data.keys())
samples_per_role = TOTAL_SAMPLES // len(career_roles)


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def add_noise(value):
    """
    Adds controlled randomness/noise
    """
    if random.random() < NOISE_LEVEL:
        variation = random.randint(-3, 3)
        value += variation

    return max(1, min(10, value))


def generate_gpa(skill_scores):
    """
    GPA loosely based on overall skill strength
    """
    avg_skill = sum(skill_scores) / len(skill_scores)

    gpa = round(random.uniform(
        max(5.0, avg_skill - 2),
        min(10.0, avg_skill)
    ), 2)

    return gpa


def generate_student(career_name, career_info):
    student = {}

    required_skills = career_info["required_skills"]

    skill_values = []

    # Generate realistic skill scores
    for skill, benchmark in required_skills.items():

        lower = max(1, benchmark - 2)
        upper = min(10, benchmark + 1)

        score = random.randint(lower, upper)

        score = add_noise(score)

        student[skill] = score
        skill_values.append(score)

    # GPA generation
    student["GPA"] = generate_gpa(skill_values)

    # Preference Features
    if random.random() < 0.8:
        student["Preferred_Work_Type"] = career_info["preferred_work_type"]
    else:
        student["Preferred_Work_Type"] = random.choice(WORK_TYPES)

    if random.random() < 0.8:
        student["Work_Style"] = career_info["work_style"]
    else:
        student["Work_Style"] = random.choice(WORK_STYLES)

    # Target Label
    student["Career_Role"] = career_name

    return student


# -----------------------------
# DATASET GENERATION
# -----------------------------

dataset = []

for career in career_roles:
    career_info = career_data[career]

    for _ in range(samples_per_role):
        student = generate_student(career, career_info)
        dataset.append(student)

# Shuffle dataset
random.shuffle(dataset)

# Convert to DataFrame
df = pd.DataFrame(dataset)

# Reorder columns
column_order = [
    "GPA",
    "Programming_Skill",
    "DBMS_Knowledge",
    "Computer_Networks",
    "Mathematics_Statistics",
    "Web_Development",
    "App_Development",
    "Data_Analysis",
    "Cybersecurity",
    "Cloud_DevOps",
    "UI_UX_Design",
    "Testing_Debugging",
    "Problem_Solving",
    "Analytical_Thinking",
    "Creativity",
    "Communication_Skill",
    "Leadership",
    "Teamwork",
    "Preferred_Work_Type",
    "Work_Style",
    "Career_Role"
]

df = df[column_order]

# Save CSV
df.to_csv(OUTPUT_PATH, index=False)

# -----------------------------
# SUCCESS MESSAGE
# -----------------------------

print("\n✅ Dataset Generated Successfully!")
print(f"📁 Saved at: {OUTPUT_PATH}")
print(f"📊 Total Samples: {len(df)}")
print(f"🧠 Career Roles: {len(career_roles)}")
print(f"📌 Samples per Role: {samples_per_role}")

print("\nFirst 5 Rows:")
print(df.head())