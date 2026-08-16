import sqlite3

DATABASE_NAME = "telecom.db"

def create_database():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customer_predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contract TEXT NOT NULL,
    tenure_months INTEGER NOT NULL,
    internet_service TEXT NOT NULL,
    monthly_charges REAL NOT NULL,
    total_charges REAL NOT NULL,
    complaint TEXT,
    sentiment TEXT,
    churn_prediction TEXT,
    churn_probability REAL,
    prediction_time DATETIME DEFAULT CURRENT_TIMESTAMP

   );
   """)

    conn.commit()
    conn.close()


def save_prediction(data):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO customer_predictions (
    contract,
    tenure_months,
    internet_service,
    monthly_charges,
    total_charges,
    complaint,
    sentiment,
    churn_prediction,
    churn_probability
   )
   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, data)

    conn.commit()
    conn.close()