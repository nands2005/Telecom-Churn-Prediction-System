import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)

# Load Cleaned Dataset

df = pd.read_csv("dataset/cleaned_telco.csv")

print("="*60)
print("Dataset Loaded Successfully")
print("="*60)

print("Dataset Shape:", df.shape)

# Features and Target

X = df.drop("Churn Value", axis=1)

y = df["Churn Value"]

print("\nFeatures Shape :", X.shape)
print("Target Shape   :", y.shape)

# Check Class Distribution

print("\nClass Distribution")
print(df["Churn Value"].value_counts())

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Samples :", X_train.shape[0])
print("Testing Samples  :", X_test.shape[0])

# Random Forest Model

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    class_weight="balanced",
    random_state=42
)

print("\nTraining Model...")

model.fit(X_train, y_train)
print("Model Training Completed Successfully!")

# Prediction

y_pred = model.predict(X_test)

# Probability prediction

y_prob = model.predict_proba(X_test)[:, 1]

# Evaluation

accuracy = accuracy_score(y_test, y_pred)

roc_auc = roc_auc_score(y_test, y_prob)

print("\n" + "="*60)
print("MODEL PERFORMANCE")
print("="*60)
print("Accuracy :", round(accuracy,4))
print("ROC AUC  :", round(roc_auc,4))
print("\nClassification Report\n")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, y_pred))

# Feature Importance
importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance": model.feature_importances_

})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop Important Features\n")
print(importance)

# Save feature importance

importance.to_csv(
    "dataset/feature_importance.csv",
    index=False
)

# Save Model

joblib.dump(
    model,
    "models/churn_model.pkl"
)

print("\nModel Saved Successfully!")
print("Location : models/churn_model.pkl")
print("\nFeature Importance Saved!")
print("Location : dataset/feature_importance.csv")
print("\nTraining Completed Successfully.")