import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_excel("dataset/Telco_customer_churn.xlsx")

print("Original Shape:", df.shape)

# Drop unnecessary columns
columns_to_drop = [
    "CustomerID",
    "Count",
    "Country",
    "State",
    "City",
    "Zip Code",
    "Lat Long",
    "Latitude",
    "Longitude",
    "Churn Label",
    "Churn Reason",
    "Churn Score",
    "CLTV"
]

df.drop(columns=columns_to_drop, inplace=True)

print("Shape after dropping columns:", df.shape)


# Convert Total Charges
df["Total Charges"] = pd.to_numeric(
    df["Total Charges"],
    errors="coerce"
)

# Fill missing values
df["Total Charges"] = df["Total Charges"].fillna(
    df["Total Charges"].median()
)


encoder = LabelEncoder()

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = encoder.fit_transform(df[col])


df.to_csv("dataset/cleaned_telco.csv", index=False)

print("\nCleaning Completed Successfully!")

print("Cleaned Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())