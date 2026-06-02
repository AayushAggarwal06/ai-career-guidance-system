import sqlite3
import json
from datetime import datetime


# ==========================================
# DATABASE PATH
# ==========================================

DB_PATH = "database/career_guidance.db"


# ==========================================
# CREATE TABLE
# ==========================================

def initialize_database():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS
        prediction_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            student_name TEXT,

            gpa REAL,

            predicted_career TEXT,

            skill_gap_summary TEXT,

            recommended_courses TEXT,

            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


# ==========================================
# SAVE PREDICTION
# ==========================================

def save_prediction(
    student_name,
    gpa,
    predicted_career,
    priority_skills,
    courses
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    # Check duplicate entry
    cursor.execute("""
        SELECT *
        FROM prediction_history
        WHERE student_name = ?
        AND gpa = ?
        AND predicted_career = ?
    """, (
        student_name,
        gpa,
        predicted_career
    ))

    existing_entry = cursor.fetchone()

    # Save only if entry does not exist
    if existing_entry is None:

        timestamp = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        skill_gap_summary = json.dumps(
            priority_skills
        )

        recommended_courses = json.dumps(
            courses
        )

        cursor.execute("""
            INSERT INTO prediction_history (

                student_name,
                gpa,
                predicted_career,
                skill_gap_summary,
                recommended_courses,
                timestamp

            )

            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            student_name,
            gpa,
            predicted_career,
            skill_gap_summary,
            recommended_courses,
            timestamp
        ))

        conn.commit()

    conn.close()

# ==========================================
# GET HISTORY
# ==========================================

def get_prediction_history():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            student_name,
            predicted_career,
            gpa,
            timestamp
        FROM prediction_history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================================
# CLEAR HISTORY
# ==========================================

def clear_prediction_history():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    # Delete all rows
    cursor.execute(
        "DELETE FROM prediction_history"
    )

    conn.commit()

    # Reset auto increment
    cursor.execute("""
        DELETE FROM sqlite_sequence
        WHERE name='prediction_history'
    """)

    conn.commit()

    conn.close()