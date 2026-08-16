from flask import Flask, render_template, request
import pandas as pd
import joblib

from database import create_database, save_prediction
from sentiment import analyze_sentiment
from recommendation import generate_recommendation
from dashboard import dashboard

app = Flask(__name__)

# Register Dashboard Blueprint
app.register_blueprint(dashboard)

# Create database if it doesn't exist
create_database()

# Load trained model
model = joblib.load("models/churn_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get form value
    
    contract = int(request.form["Contract"])
    tenure = int(request.form["TenureMonths"])
    internet_service = int(request.form["InternetService"])
    monthly_charges = float(request.form["MonthlyCharges"])
    total_charges = float(request.form["TotalCharges"])
    complaint = request.form["Complaint"]

    # Sentiment Analysis
    sentiment = analyze_sentiment(complaint)

    # Model Input
    input_data = [[
        0,                      # gender
        0,                      # senior citizen
        1,                      # partner
        0,                      # dependents
        tenure,
        1,                      # phone service
        1,                      # multiple lines
        internet_service,
        2,                      # online security
        2,                      # online backup
        2,                      # device protection
        2,                      # tech support
        2,                      # streaming tv
        2,                      # streaming movies
        contract,
        1,                      # paperless billing
        2,                      # payment method
        monthly_charges,
        total_charges
    ]]

    df = pd.DataFrame(input_data)

    # Prediction
    
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    if prediction == 1:
        result = "Customer is likely to Churn"
    else:
        result = "Customer is NOT likely to Churn"

    # AI Recommendation
    
    recommendations = generate_recommendation(
    prediction,
    probability,
    sentiment
    )
    # Save to Database
    # Convert encoded values to readable text for the database

    contract_map = {
    0: "Month-to-Month",
    1: "One Year",
    2: "Two Year"
   }

    internet_map = {
    0: "DSL",
    1: "Fiber Optic",
    2: "No Internet"
   }

    save_prediction((
    contract_map.get(contract, "Unknown"),
    tenure,
    internet_map.get(internet_service, "Unknown"),
    monthly_charges,
    total_charges,
    complaint,
    sentiment,
    result,
    round(probability * 100, 2)
   ))
    
    return render_template(
        "index.html",
        prediction=result,
        probability=round(probability * 100, 2),
        complaint=complaint,
        sentiment=sentiment,
        recommendations=recommendations
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)