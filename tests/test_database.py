from database.db_manager import (
    initialize_database,
    save_prediction,
    get_prediction_history
)


initialize_database()

save_prediction(
    student_name="Aayush",
    gpa=8.5,
    predicted_career=
        "Machine Learning Engineer",

    priority_skills={
        "Programming_Skill":
            {"gap": 3}
    },

    courses=[
        "Machine Learning Basics",
        "Python for Data Science"
    ]
)

history = get_prediction_history()

print("\nPrediction History:\n")

for row in history:
    print(row)