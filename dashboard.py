from flask import Blueprint, render_template
import sqlite3

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard")
def dashboard_page():

    conn = sqlite3.connect("telecom.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Fetch all prediction records
    
    cursor.execute("""
        SELECT * FROM customer_predictions
        ORDER BY id DESC
    """)
    records = cursor.fetchall()

    # Total predictions
    
    cursor.execute("SELECT COUNT(*) FROM customer_predictions")
    total_predictions = cursor.fetchone()[0]

    # Churn count
    
    cursor.execute("""
        SELECT COUNT(*)
        FROM customer_predictions
        WHERE churn_prediction='Customer is likely to Churn'
    """)
    churn_count = cursor.fetchone()[0]

    # Non-churn count
    
    cursor.execute("""
        SELECT COUNT(*)
        FROM customer_predictions
        WHERE churn_prediction='Customer is NOT likely to Churn'
    """)
    non_churn_count = cursor.fetchone()[0]

    # Average churn probability
    
    cursor.execute("""
        SELECT AVG(churn_probability)
        FROM customer_predictions
    """)
    avg_probability = cursor.fetchone()[0]

    if avg_probability is None:
        avg_probability = 0

    # Positive sentiment count
    
    cursor.execute("""
        SELECT COUNT(*)
        FROM customer_predictions
        WHERE sentiment='Positive'
    """)
    positive_count = cursor.fetchone()[0]

    # Negative sentiment count
    
    cursor.execute("""
        SELECT COUNT(*)
        FROM customer_predictions
        WHERE sentiment='Negative'
    """)
    negative_count = cursor.fetchone()[0]

    # Neutral sentiment count
    
    cursor.execute("""
        SELECT COUNT(*)
        FROM customer_predictions
        WHERE sentiment='Neutral'
    """)
    neutral_count = cursor.fetchone()[0]
    
    

    conn.close()

    return render_template(
    "dashboard.html",
    records=records,
    total_predictions=total_predictions,
    churn_count=churn_count,
    non_churn_count=non_churn_count,
    avg_probability=round(avg_probability,2),
    positive_count=positive_count,
    negative_count=negative_count,
    neutral_count=neutral_count
)