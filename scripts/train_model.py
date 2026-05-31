import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC


# ==========================================
# PATH CONFIGURATION
# ==========================================

DATA_PATH = "data/synthetic_dataset.csv"
MODEL_DIR = "models"

os.makedirs(MODEL_DIR, exist_ok=True)


# ==========================================
# LOAD DATASET
# ==========================================

print("\nLoading dataset...")

df = pd.read_csv(DATA_PATH)

print(f"Dataset Shape: {df.shape}")


# ==========================================
# ENCODE CATEGORICAL FEATURES
# ==========================================

print("\nEncoding categorical features...")

work_type_encoder = LabelEncoder()
work_style_encoder = LabelEncoder()

df["Preferred_Work_Type"] = (
    work_type_encoder.fit_transform(
        df["Preferred_Work_Type"]
    )
)

df["Work_Style"] = (
    work_style_encoder.fit_transform(
        df["Work_Style"]
    )
)


# ==========================================
# FEATURE / TARGET SPLIT
# ==========================================

X = df.drop("Career_Role", axis=1)
y = df["Career_Role"]

feature_columns = X.columns.tolist()

print("\nFeature Columns:")
print(feature_columns)


# ==========================================
# TARGET LABEL ENCODING
# ==========================================

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

print("\nCareer Classes:")
print(label_encoder.classes_)


# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)

print("\nTrain Shape:", X_train.shape)
print("Test Shape:", X_test.shape)


# ==========================================
# FEATURE SCALING
# ==========================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ==========================================
# MODEL DEFINITIONS
# ==========================================

models = {
    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ),

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "SVM": SVC(
        kernel="rbf",
        probability=True
    )
}


# ==========================================
# TRAINING + EVALUATION
# ==========================================

results = {}

best_model = None
best_accuracy = 0
best_model_name = ""

print("\nTraining Models...\n")

for model_name, model in models.items():

    print("=" * 60)
    print(f"\nTraining {model_name}...")

    # SVM requires scaling
    if model_name == "SVM":
        model.fit(X_train_scaled, y_train)
        predictions = model.predict(X_test_scaled)

    else:
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(
        y_test,
        predictions,
        average="weighted"
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted"
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    results[model_name] = accuracy

    print(f"\nAccuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=label_encoder.classes_
        )
    )

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_model_name = model_name


# ==========================================
# SAVE MODEL FILES
# ==========================================

print("\n" + "=" * 60)
print(f"\nBest Model: {best_model_name}")
print(f"Best Accuracy: {best_accuracy:.4f}")

joblib.dump(
    best_model,
    f"{MODEL_DIR}/career_model.pkl"
)

joblib.dump(
    scaler,
    f"{MODEL_DIR}/scaler.pkl"
)

joblib.dump(
    label_encoder,
    f"{MODEL_DIR}/label_encoder.pkl"
)

joblib.dump(
    feature_columns,
    f"{MODEL_DIR}/feature_columns.pkl"
)

joblib.dump(
    work_type_encoder,
    f"{MODEL_DIR}/work_type_encoder.pkl"
)

joblib.dump(
    work_style_encoder,
    f"{MODEL_DIR}/work_style_encoder.pkl"
)

print("\nModel files saved successfully!")

print("\nSaved Files:")
print("career_model.pkl")
print("scaler.pkl")
print("label_encoder.pkl")
print("feature_columns.pkl")
print("work_type_encoder.pkl")
print("work_style_encoder.pkl")


# ==========================================
# FINAL MODEL SUMMARY
# ==========================================

print("\nMODEL PERFORMANCE SUMMARY")

for model_name, score in results.items():
    print(f"{model_name}: {score:.4f}")