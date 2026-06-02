import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.predict import predict_career
from utils.skill_gap import (
    analyze_skill_gap,
    get_priority_skills
)

from utils.recommendation import (
    get_recommended_courses,
    get_certifications,
    generate_skill_suggestions
)

from database.db_manager import (
    initialize_database,
    save_prediction,
    get_prediction_history,
    clear_prediction_history
)


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🎯",
    layout="wide"
)

# Initialize database
initialize_database()


# ==========================================
# HEADER
# ==========================================

st.markdown("""
<h1 style='text-align: center;
color: #4CAF50;'>
🎯 AI-Driven Smart Career
Guidance System
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align: center;
color: gray;'>
Smart Career Prediction with
Skill Gap Analysis
</h4>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown("""
# 🎯 Career Guidance System
""")

st.sidebar.info(
    """
    ### About Project

    This AI-powered system predicts
    suitable technology careers based
    on student skills, GPA, work
    preferences and provides:

    ✅ Career Prediction

    ✅ Skill Gap Analysis

    ✅ Recommended Courses

    ✅ Certifications

    ✅ Personalized Suggestions
    """
)

st.sidebar.markdown("---")

st.sidebar.success(
    "Developed for MCA Major Project"
)


# ==========================================
# INPUT SECTION
# ==========================================

st.header("Student Skill Assessment")

student_name = st.text_input(
    "Student Name",
    placeholder="Enter your name"
)

col1, col2 = st.columns(2)

with col1:

    gpa = st.slider(
        "GPA",
        min_value=0.0,
        max_value=10.0,
        value=7.0,
        step=0.1
    )

    programming_skill = st.slider(
        "Programming Skill", 1, 10, 5
    )

    dbms_knowledge = st.slider(
        "DBMS Knowledge", 1, 10, 5
    )

    computer_networks = st.slider(
        "Computer Networks", 1, 10, 5
    )

    mathematics_statistics = st.slider(
        "Mathematics & Statistics", 1, 10, 5
    )

    web_development = st.slider(
        "Web Development", 1, 10, 5
    )

    app_development = st.slider(
        "App Development", 1, 10, 5
    )

    data_analysis = st.slider(
        "Data Analysis", 1, 10, 5
    )

    cybersecurity = st.slider(
        "Cybersecurity", 1, 10, 5
    )

    cloud_devops = st.slider(
        "Cloud & DevOps", 1, 10, 5
    )


with col2:

    ui_ux_design = st.slider(
        "UI/UX Design", 1, 10, 5
    )

    testing_debugging = st.slider(
        "Testing & Debugging", 1, 10, 5
    )

    problem_solving = st.slider(
        "Problem Solving", 1, 10, 5
    )

    analytical_thinking = st.slider(
        "Analytical Thinking", 1, 10, 5
    )

    creativity = st.slider(
        "Creativity", 1, 10, 5
    )

    communication_skill = st.slider(
        "Communication Skill", 1, 10, 5
    )

    leadership = st.slider(
        "Leadership", 1, 10, 5
    )

    teamwork = st.slider(
        "Teamwork", 1, 10, 5
    )

    preferred_work_type = st.selectbox(
        "Preferred Work Type",
        [
            "Technical",
            "Analytical",
            "Creative"
        ]
    )

    work_style = st.selectbox(
        "Work Style",
        [
            "Individual",
            "Team"
        ]
    )


st.markdown("---")



# ==========================================
# ANALYZE BUTTON
# ==========================================

analyze_button = st.button(
    "🔍 Analyze Career",
    use_container_width=True
)

# Persist analysis state
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# Prevent duplicate database saves
if "prediction_saved" not in st.session_state:
    st.session_state.prediction_saved = False

if analyze_button:
    st.session_state.analyzed = True
    st.session_state.prediction_saved = False


if st.session_state.analyzed:

    # Create Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "🎯 Career Prediction",
        "📊 Skill Gap",
        "📚 Recommendations",
        "🕒 History"
    ])

    # ======================================
    # INPUT DATA
    # ======================================

    student_data = {

        "GPA": gpa,

        "Programming_Skill":
            programming_skill,

        "DBMS_Knowledge":
            dbms_knowledge,

        "Computer_Networks":
            computer_networks,

        "Mathematics_Statistics":
            mathematics_statistics,

        "Web_Development":
            web_development,

        "App_Development":
            app_development,

        "Data_Analysis":
            data_analysis,

        "Cybersecurity":
            cybersecurity,

        "Cloud_DevOps":
            cloud_devops,

        "UI_UX_Design":
            ui_ux_design,

        "Testing_Debugging":
            testing_debugging,

        "Problem_Solving":
            problem_solving,

        "Analytical_Thinking":
            analytical_thinking,

        "Creativity":
            creativity,

        "Communication_Skill":
            communication_skill,

        "Leadership":
            leadership,

        "Teamwork":
            teamwork,

        "Preferred_Work_Type":
            preferred_work_type,

        "Work_Style":
            work_style
    }

    # ======================================
    # PREDICTION
    # ======================================

    predicted_career = predict_career(
        student_data.copy()
    )
    
    # Save prediction only once
    if not st.session_state.prediction_saved:

        courses = get_recommended_courses(
            predicted_career
        )

        save_prediction(
            student_name=
                student_name
                if student_name
                else "Unknown",

            gpa=gpa,

            predicted_career=
                predicted_career,

            priority_skills=
                {},

            courses=courses
        )

        st.session_state.prediction_saved = True

    skill_gap_report = (
        analyze_skill_gap(
            student_data,
            predicted_career
        )
    )

    priority_skills = (
        get_priority_skills(
            skill_gap_report
        )
    )

    # ======================================
    # TAB 1 - CAREER PREDICTION
    # ======================================

    with tab1:

        st.markdown(f"""
        <div style="
        background-color:#1E3A5F;
        padding:20px;
        border-radius:15px;
        text-align:center;
        margin-top:10px;
        margin-bottom:20px;
        ">

        <h2 style="color:white;">
        🎯 Recommended Career
        </h2>

        <h1 style="color:#4CAF50;">
        {predicted_career}
        </h1>

        </div>
        """, unsafe_allow_html=True)

        col_metric1, col_metric2 = st.columns(2)

        with col_metric1:
            st.metric(
                "Student GPA",
                gpa
            )

        with col_metric2:
            st.metric(
                "Recommended Career",
                predicted_career
            )

    # ======================================
    # TAB 2 - SKILL GAP
    # ======================================

    with tab2:

        st.subheader(
            "📊 Skill Gap Analysis"
        )

        if priority_skills:

            gap_table = []

            for skill, details in (
                priority_skills.items()
            ):

                gap_table.append({

                    "Skill":
                        skill.replace(
                            "_", " "
                        ),

                    "Your Score":
                        details[
                            "student_score"
                        ],

                    "Required":
                        details[
                            "required_score"
                        ],

                    "Gap":
                        details["gap"],

                    "Severity":

                        "🔴 High"
                        if details[
                            "severity"
                        ] == "High"

                        else "🟡 Medium"
                        if details[
                            "severity"
                        ] == "Medium"

                        else "🟢 Low"
                })

            st.dataframe(
                pd.DataFrame(
                    gap_table
                ),
                use_container_width=True,
                hide_index=True
            )

        else:
            st.success(
                "Excellent! "
                "No major skill gaps found."
            )

        # GRAPH

        st.markdown("---")

        st.subheader(
            "📈 Skill Comparison Analysis"
        )

        if priority_skills:

            skills = []
            student_scores = []
            required_scores = []

            for skill, details in (
                priority_skills.items()
            ):

                skills.append(
                    skill.replace(
                        "_", " "
                    )
                )

                student_scores.append(
                    details[
                        "student_score"
                    ]
                )

                required_scores.append(
                    details[
                        "required_score"
                    ]
                )

            fig, ax = plt.subplots(
                figsize=(10, 5)
            )

            x = range(len(skills))
            width = 0.4

            ax.bar(
                [i - width / 2 for i in x],
                student_scores,
                width=width,
                label="Your Score"
            )

            ax.bar(
                [i + width / 2 for i in x],
                required_scores,
                width=width,
                label="Required Score"
            )

            ax.set_xticks(x)

            ax.set_xticklabels(
                skills,
                rotation=45,
                ha="right"
            )

            ax.set_ylabel(
                "Skill Score"
            )

            ax.set_title(
                "Student vs Required Skills"
            )

            ax.legend()

            st.pyplot(fig)

    # ======================================
    # TAB 3 - RECOMMENDATIONS
    # ======================================

    with tab3:

        col3, col4 = st.columns(2)

        with col3:

            st.subheader(
                "📚 Recommended Courses"
            )

            courses = (
                get_recommended_courses(
                    predicted_career
                )
            )

            for course in courses:
                st.write(
                    f"✅ {course}"
                )

        with col4:

            st.subheader(
                "🏆 Certifications"
            )

            certifications = (
                get_certifications(
                    predicted_career
                )
            )

            for cert in certifications:
                st.write(
                    f"🎖️ {cert}"
                )

        st.markdown("---")

        st.subheader(
            "💡 Personalized Suggestions"
        )

        suggestions = (
            generate_skill_suggestions(
                priority_skills
            )
        )

        if suggestions:

            for suggestion in (
                suggestions
            ):
                st.write(
                    f"👉 {suggestion}"
                )


    # ======================================
    # TAB 4 - HISTORY
    # ======================================

    with tab4:

        st.subheader(
            "🕒 Prediction History"
        )

        if st.button(
            "🗑️ Clear Prediction History"
        ):

            clear_prediction_history()

            st.success(
                "Prediction history cleared!"
            )

            st.rerun()

        history = (
            get_prediction_history()
        )

        if history:

            history_df = pd.DataFrame(
                history,
                columns=[
                    "Student Name",
                    "Predicted Career",
                    "GPA",
                    "Timestamp"
                ]
            )

            history_df.index = range(
                1,
                len(history_df) + 1
            )

            history_df.index.name = (
                "S.No"
            )

            st.dataframe(
                history_df,
                use_container_width=True,
                height=300
            )

        else:
            st.info(
                "No prediction history found."
            )


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
<div style='text-align:center;
padding:15px;
border-radius:10px;
background-color:#F5F5F5;
color:#444;'>

<h4>🎯 AI-Driven Smart Career Guidance System</h4>

<b>Developed by:</b>
Aayush Aggarwal<br>

<b>Course:</b>
MCA (Master of Computer Application)<br>

<b>University:</b><br>
Guru Jambheshwar University of
Science & Technology

</div>
""", unsafe_allow_html=True)