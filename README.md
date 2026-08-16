# Telecom Customer Churn Prediction System

## Overview
The Telecom Customer Churn Prediction System is a machine learning and NLP-based web application designed to identify customers who are likely to leave a telecom service.

The system combines:

* Random Forest for customer churn prediction
* Hugging Face DistilBERT for customer complaint sentiment analysis
* Rule-based retention recommendations
* SQLite for storing prediction results
* Flask for backend development
* HTML and CSS for the frontend
* Chart.js for dashboard visualizations

The goal is to help telecom companies identify high-risk customers early and take appropriate retention actions.

---

## Project Objective

The main objective of this project is to answer:

> Which customers are likely to churn, and what retention action should be taken?

The system predicts churn probability from customer information and analyzes the customer's complaint to understand their sentiment.

---

## Main Features

### 1. Customer Churn Prediction

The system uses a Random Forest Classifier to predict whether a customer is likely to churn.

The prediction includes:

* Churn status
* Churn probability

Example:

```text
Customer is likely to Churn
Churn Probability: 70.02%
```

### 2. Customer Complaint Sentiment Analysis

Customer complaints are analyzed using the Hugging Face model:

The complaint is classified as:

* Positive
* Negative

Example:

```text
Complaint:
The network is very slow and customer support is poor.

Sentiment:
Negative
```

### 3. Retention Recommendation

The system uses churn probability and sentiment to recommend an appropriate retention action.

Examples include:

* Discount offers
* Priority customer support
* Service issue resolution
* Loyalty rewards
* Personalized retention offers
* Follow-up support



## Machine Learning Model

### Algorithm

Random Forest Classifier

The model was trained on the Telco Customer Churn dataset.

### Model Performance

Current model performance:

```text
Accuracy : 77.5%
ROC-AUC  : 0.8493
```

The model uses customer attributes such as:

* Contract
* Tenure
* Internet Service
* Monthly Charges
* Total Charges
* and other preprocessed customer features

The trained model is stored at:

```text
models/churn_model.pkl
```

---

## Dataset

The project uses the Telco Customer Churn dataset.

Dataset files included in the project:

```text
dataset/
├── Telco_customer_churn.xlsx
└── cleaned_telco.csv
```
## Future Enhancements

* Real-time customer data integration
* Login and role-based access
* Email/SMS alerts for high-risk customers
* Advanced retention models
---


This project is developed for educational and academic purposes.
