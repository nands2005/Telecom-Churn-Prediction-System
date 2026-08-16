import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Create plots folder
os.makedirs("plots", exist_ok=True)

# Load Dataset
df = pd.read_csv("dataset/cleaned_telco.csv")

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print(df.head())

print("\nShape :", df.shape)

print("\nColumns")
print(df.columns)

print("\nMissing Values")
print(df.isnull().sum())

# 1. Churn Distribution

plt.figure(figsize=(6,5))

sns.countplot(x="Churn Value", data=df)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Count")

plt.savefig("plots/1_churn_distribution.png")

plt.show()

# 2. Gender vs Churn

plt.figure(figsize=(6,5))

sns.countplot(
    x="Gender",
    hue="Churn Value",
    data=df
)

plt.title("Gender vs Churn")

plt.savefig("plots/2_gender_churn.png")

plt.show()

# 3. Contract vs Churn

plt.figure(figsize=(8,5))

sns.countplot(
    x="Contract",
    hue="Churn Value",
    data=df
)

plt.title("Contract Type vs Churn")

plt.savefig("plots/3_contract_churn.png")

plt.show()

# 4. Internet Service vs Churn

plt.figure(figsize=(8,5))

sns.countplot(
    x="Internet Service",
    hue="Churn Value",
    data=df
)

plt.title("Internet Service vs Churn")

plt.savefig("plots/4_internet_service.png")

plt.show()

# 5. Payment Method vs Churn

plt.figure(figsize=(10,5))

sns.countplot(
    x="Payment Method",
    hue="Churn Value",
    data=df
)

plt.title("Payment Method vs Churn")

plt.xticks(rotation=20)

plt.savefig("plots/5_payment_method.png")

plt.show()

# 6. Monthly Charges Distribution

plt.figure(figsize=(8,5))

sns.histplot(
    df["Monthly Charges"],
    bins=30,
    kde=True
)

plt.title("Monthly Charges Distribution")

plt.savefig("plots/6_monthly_charges.png")

plt.show()

# 7. Total Charges Distribution

plt.figure(figsize=(8,5))

sns.histplot(
    df["Total Charges"],
    bins=30,
    kde=True
)

plt.title("Total Charges Distribution")

plt.savefig("plots/7_total_charges.png")

plt.show()

# 8. Tenure Distribution

plt.figure(figsize=(8,5))

sns.histplot(
    df["Tenure Months"],
    bins=30,
    kde=True
)

plt.title("Tenure Months Distribution")

plt.savefig("plots/8_tenure.png")

plt.show()

# 9. Monthly Charges vs Churn

plt.figure(figsize=(8,5))

sns.boxplot(
    x="Churn Value",
    y="Monthly Charges",
    data=df
)

plt.title("Monthly Charges vs Churn")

plt.savefig("plots/9_boxplot_monthly.png")

plt.show()

# 10. Total Charges vs Churn

plt.figure(figsize=(8,5))

sns.boxplot(
    x="Churn Value",
    y="Total Charges",
    data=df
)

plt.title("Total Charges vs Churn")

plt.savefig("plots/10_boxplot_total.png")

plt.show()

# 11. Correlation Heatmap

plt.figure(figsize=(15,10))

corr = df.corr()

sns.heatmap(
    corr,
    cmap="coolwarm",
    annot=False
)

plt.title("Correlation Heatmap")

plt.savefig("plots/11_heatmap.png")

plt.show()

# 12. Correlation with Churn

correlation = corr["Churn Value"].sort_values(ascending=False)

print("\nCorrelation with Churn\n")

print(correlation)

# 13. Feature Correlation Bar Graph

plt.figure(figsize=(10,8))

correlation.drop("Churn Value").plot(kind="bar")

plt.title("Feature Correlation with Churn")

plt.ylabel("Correlation")

plt.tight_layout()

plt.savefig("plots/12_feature_correlation.png")

plt.show()

# Summary

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated Plots:")

plots = sorted(os.listdir("plots"))

for plot in plots:
    print(plot)