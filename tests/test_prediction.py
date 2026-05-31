from utils.predict import predict_career


student = {
    "GPA": 8.2,
    "Programming_Skill": 8,
    "DBMS_Knowledge": 7,
    "Computer_Networks": 5,
    "Mathematics_Statistics": 9,
    "Web_Development": 4,
    "App_Development": 3,
    "Data_Analysis": 9,
    "Cybersecurity": 2,
    "Cloud_DevOps": 3,
    "UI_UX_Design": 2,
    "Testing_Debugging": 5,
    "Problem_Solving": 8,
    "Analytical_Thinking": 9,
    "Creativity": 5,
    "Communication_Skill": 7,
    "Leadership": 5,
    "Teamwork": 7,
    "Preferred_Work_Type":
        "Analytical",
    "Work_Style":
        "Team"
}

prediction = predict_career(
    student
)

print("\nPredicted Career:")
print(prediction)