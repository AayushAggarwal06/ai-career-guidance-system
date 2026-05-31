import joblib
import pandas as pd


# ==========================================
# LOAD SAVED FILES
# ==========================================

MODEL_PATH = "models/career_model.pkl"
SCALER_PATH = "models/scaler.pkl"
LABEL_ENCODER_PATH = "models/label_encoder.pkl"
FEATURE_COLUMNS_PATH = "models/feature_columns.pkl"

WORK_TYPE_ENCODER_PATH = (
    "models/work_type_encoder.pkl"
)

WORK_STYLE_ENCODER_PATH = (
    "models/work_style_encoder.pkl"
)


model = joblib.load(MODEL_PATH)

scaler = joblib.load(SCALER_PATH)

label_encoder = joblib.load(
    LABEL_ENCODER_PATH
)

feature_columns = joblib.load(
    FEATURE_COLUMNS_PATH
)

work_type_encoder = joblib.load(
    WORK_TYPE_ENCODER_PATH
)

work_style_encoder = joblib.load(
    WORK_STYLE_ENCODER_PATH
)


# ==========================================
# PREDICTION FUNCTION
# ==========================================

def predict_career(student_data):
    """
    Predict career role
    from student profile
    """

    student_data[
        "Preferred_Work_Type"
    ] = work_type_encoder.transform([
        student_data[
            "Preferred_Work_Type"
        ]
    ])[0]

    student_data[
        "Work_Style"
    ] = work_style_encoder.transform([
        student_data[
            "Work_Style"
        ]
    ])[0]

    # Convert to dataframe
    input_df = pd.DataFrame(
        [student_data]
    )

    # Match training columns
    input_df = input_df[
        feature_columns
    ]

    # Scale for SVM compatibility
    input_scaled = scaler.transform(
        input_df
    )

    # Random Forest prediction
    prediction_encoded = model.predict(
        input_df
    )[0]

    predicted_career = (
        label_encoder.inverse_transform(
            [prediction_encoded]
        )[0]
    )

    return predicted_career