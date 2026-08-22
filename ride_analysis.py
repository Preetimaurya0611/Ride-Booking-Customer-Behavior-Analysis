import pandas as pd
import matplotlib.pyplot as plt

# Load clean dataset
df = pd.read_excel("Ride_Booking_Customer_Analysis_CLEAN.xlsx")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())


# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nRide Status Count:")
print(df["Ride_Status"].value_counts())

print("\nCancellation Reason by Ride Status:")
print(pd.crosstab(df["Ride_Status"], df["Cancellation_Reason"].isna()))

print("\nPromo Code Usage:")
print(df["Promo_Code"].value_counts(dropna=False))

# Handle missing Cancellation Reason
df.loc[
    (df["Ride_Status"] == "Completed") & (df["Cancellation_Reason"].isna()),
    "Cancellation_Reason"
] = "Not Applicable"

df["Cancellation_Reason"] = df["Cancellation_Reason"].fillna("Unknown")


# Handle missing Promo Code
df["Promo_Code"] = df["Promo_Code"].fillna("No Promo")


# Check missing values again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Categorical Data Analysis

print("\nGender Distribution:")
print(df["Gender"].value_counts())

print("\nCity Distribution:")
print(df["City"].value_counts())

print("\nVehicle Type Distribution:")
print(df["Vehicle_Type"].value_counts())

print("\nPayment Method Distribution:")
print(df["Payment_Method"].value_counts())

print("\nBooking Source Distribution:")
print(df["Booking_Source"].value_counts())

print("\nCustomer Type Distribution:")
print(df["Customer_Type"].value_counts())

print("\nDistance Category Distribution:")
print(df["Distance_Category"].value_counts())

print("\nPeak Hour Distribution:")
print(df["Peak_Hour"].value_counts())

# Standardize Payment Method
df["Payment_Method"] = df["Payment_Method"].str.strip().str.lower()

df["Payment_Method"] = df["Payment_Method"].replace({
    "upi": "UPI",
    "cash": "Cash",
    "credit card": "Credit Card",
    "debit card": "Debit Card",
    "wallet": "Wallet"
})

print("\nPayment Method After Cleaning:")
print(df["Payment_Method"].value_counts())

# Ride Status Percentage

ride_status_percentage = df["Ride_Status"].value_counts(normalize=True) * 100

print("\nRide Status Percentage:")
print(ride_status_percentage.round(2))

# Revenue by Ride Status

revenue_by_status = df.groupby("Ride_Status")["Revenue"].agg(
    ["sum", "mean", "count"]
)

print("\nRevenue by Ride Status:")
print(revenue_by_status.round(2))

# City-wise Ride and Revenue Analysis

city_analysis = df.groupby("City").agg(
    Total_Rides=("Ride_ID", "count"),
    Completed_Rides=("Ride_Status", lambda x: (x == "Completed").sum()),
    Total_Revenue=("Revenue", "sum"),
    Average_Fare=("Fare", "mean")
).sort_values("Total_Revenue", ascending=False)

print("\nCity-wise Ride and Revenue Analysis:")
print(city_analysis.round(2))

# Vehicle Type Analysis

vehicle_analysis = df.groupby("Vehicle_Type").agg(
    Total_Rides=("Ride_ID", "count"),
    Completed_Rides=("Ride_Status", lambda x: (x == "Completed").sum()),
    Total_Revenue=("Revenue", "sum"),
    Average_Fare=("Fare", "mean"),
    Average_Distance=("Distance_KM", "mean")
).sort_values("Total_Revenue", ascending=False)

print("\nVehicle Type Analysis:")
print(vehicle_analysis.round(2))

# Customer Type Analysis

customer_analysis = df.groupby("Customer_Type").agg(
    Total_Rides=("Ride_ID", "count"),
    Completed_Rides=("Ride_Status", lambda x: (x == "Completed").sum()),
    Total_Revenue=("Revenue", "sum"),
    Average_Fare=("Fare", "mean"),
    Average_Rating=("Customer_Rating", "mean")
).sort_values("Total_Revenue", ascending=False)

print("\nCustomer Type Analysis:")
print(customer_analysis.round(2))

# Booking Source Analysis

booking_analysis = df.groupby("Booking_Source").agg(
    Total_Rides=("Ride_ID", "count"),
    Completed_Rides=("Ride_Status", lambda x: (x == "Completed").sum()),
    Total_Revenue=("Revenue", "sum"),
    Average_Fare=("Fare", "mean")
).sort_values("Total_Revenue", ascending=False)

print("\nBooking Source Analysis:")
print(booking_analysis.round(2))

# Payment Method Analysis

payment_analysis = df.groupby("Payment_Method").agg(
    Total_Rides=("Ride_ID", "count"),
    Completed_Rides=("Ride_Status", lambda x: (x == "Completed").sum()),
    Total_Revenue=("Revenue", "sum"),
    Average_Fare=("Fare", "mean")
).sort_values("Total_Revenue", ascending=False)

print("\nPayment Method Analysis:")
print(payment_analysis.round(2))

# Distance Category Analysis

print("Distance Category Distribution:")
print(df['Distance_Category'].value_counts())

print("\nDistance Category Percentage:")
print(df['Distance_Category'].value_counts(normalize=True) * 100)

# Gender-wise Analysis

gender_analysis = df.groupby("Gender").agg(
    Total_Rides=("Ride_ID", "count"),
    Completed_Rides=("Ride_Status", lambda x: (x == "Completed").sum()),
    Total_Revenue=("Revenue", "sum"),
    Average_Fare=("Fare", "mean"),
    Average_Rating=("Customer_Rating", "mean")
).sort_values("Total_Revenue", ascending=False)

print("\nGender-wise Analysis:")
print(gender_analysis.round(2))

# Peak Hour Analysis

peak_hour_analysis = df.groupby("Peak_Hour").agg(
    Total_Rides=("Ride_ID", "count"),
    Completed_Rides=("Ride_Status", lambda x: (x == "Completed").sum()),
    Total_Revenue=("Revenue", "sum"),
    Average_Fare=("Fare", "mean")
).sort_values("Total_Revenue", ascending=False)

print("\nPeak Hour Analysis:")
print(peak_hour_analysis.round(2))

# Promo Code Analysis

promo_analysis = df.groupby("Promo_Code").agg(
    Total_Rides=("Ride_ID", "count"),
    Completed_Rides=("Ride_Status", lambda x: (x == "Completed").sum()),
    Total_Revenue=("Revenue", "sum"),
    Average_Fare=("Fare", "mean")
).sort_values("Total_Revenue", ascending=False)

print("\nPromo Code Analysis:")
print(promo_analysis.round(2))

# Cancellation Reason Analysis

cancellation_analysis = df[df["Ride_Status"] == "Cancelled"].groupby(
    "Cancellation_Reason"
).agg(
    Cancelled_Rides=("Ride_ID", "count")
).sort_values("Cancelled_Rides", ascending=False)

print("\nCancellation Reason Analysis:")
print(cancellation_analysis)

print("\nCancellation Reason Percentage:")

cancellation_percentage = (
    df[df["Ride_Status"] == "Cancelled"]["Cancellation_Reason"]
    .value_counts(normalize=True) * 100
)

print(cancellation_percentage.round(2))

# Age Group Analysis

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 18, 25, 35, 45, 55, 65, 100],
    labels=[
        "Under 18",
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "56-65",
        "65+"
    ]
)

age_group_analysis = df.groupby("Age_Group", observed=True).agg(
    Total_Rides=("Ride_ID", "count"),
    Completed_Rides=("Ride_Status", lambda x: (x == "Completed").sum()),
    Total_Revenue=("Revenue", "sum"),
    Average_Fare=("Fare", "mean"),
    Average_Rating=("Customer_Rating", "mean")
)

print("\nAge Group Analysis:")
print(age_group_analysis.round(2))

# ==========================================
# VISUALIZATION 1: RIDE STATUS DISTRIBUTION
# ==========================================

import matplotlib.pyplot as plt

ride_status_counts = df["Ride_Status"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    ride_status_counts.index,
    ride_status_counts.values
)

plt.title("Ride Status Distribution")
plt.xlabel("Ride Status")
plt.ylabel("Number of Rides")

plt.tight_layout()

# Save graph as image
plt.savefig("Ride_Status_Distribution.png")

# Display graph
plt.show()

# ==========================================
# VISUALIZATION 2: CITY-WISE REVENUE
# ==========================================

city_revenue = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))

plt.bar(
    city_revenue.index,
    city_revenue.values
)

plt.title("City-wise Revenue")
plt.xlabel("City")
plt.ylabel("Total Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

# Save graph as image
plt.savefig("City_Wise_Revenue.png")

# Display graph
plt.show()

# ==========================================
# VISUALIZATION 3: VEHICLE TYPE DISTRIBUTION
# ==========================================

vehicle_counts = df["Vehicle_Type"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    vehicle_counts.index,
    vehicle_counts.values
)

plt.title("Vehicle Type Distribution")
plt.xlabel("Vehicle Type")
plt.ylabel("Number of Rides")

plt.tight_layout()

# Save graph as image
plt.savefig("Vehicle_Type_Distribution.png")

# Display graph
plt.show()

# ==========================================
# VISUALIZATION 4: DISTANCE CATEGORY DISTRIBUTION
# ==========================================

distance_counts = df["Distance_Category"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    distance_counts.index,
    distance_counts.values
)

plt.title("Distance Category Distribution")
plt.xlabel("Distance Category")
plt.ylabel("Number of Rides")

plt.tight_layout()

# Save graph as image
plt.savefig("Distance_Category_Distribution.png")

# Display graph
plt.show()

# ==========================================
# VISUALIZATION 5: PEAK VS OFF-PEAK RIDES
# ==========================================

peak_counts = df["Peak_Hour"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    peak_counts.index,
    peak_counts.values
)

plt.title("Peak vs Off-Peak Rides")
plt.xlabel("Time Category")
plt.ylabel("Number of Rides")

plt.tight_layout()

# Save graph as image
plt.savefig("Peak_vs_OffPeak_Rides.png")

# Display graph
plt.show()

# ==========================================
# VISUALIZATION 6: REVENUE BY PAYMENT METHOD
# ==========================================

payment_revenue = df.groupby("Payment_Method")["Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 5))

plt.bar(
    payment_revenue.index,
    payment_revenue.values
)

plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Revenue")

plt.xticks(rotation=20)

plt.tight_layout()

# Save graph as image
plt.savefig("Revenue_by_Payment_Method.png")

# Display graph
plt.show()

# ==========================================
# VISUALIZATION 7: CUSTOMER TYPE DISTRIBUTION
# ==========================================

customer_type_counts = df["Customer_Type"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    customer_type_counts.index,
    customer_type_counts.values
)

plt.title("Customer Type Distribution")
plt.xlabel("Customer Type")
plt.ylabel("Number of Rides")

plt.tight_layout()

# Save graph as image
plt.savefig("Customer_Type_Distribution.png")

# Display graph
plt.show()

# ==========================================
# VISUALIZATION 8: AGE GROUP DISTRIBUTION
# ==========================================

age_counts = df["Age_Group"].value_counts().sort_index()

plt.figure(figsize=(9, 5))

plt.bar(
    age_counts.index.astype(str),
    age_counts.values
)

plt.title("Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Rides")

plt.xticks(rotation=20)

plt.tight_layout()

# Save graph as image
plt.savefig("Age_Group_Distribution.png")

# Display graph
plt.show()

# ==========================================
# VISUALIZATION 9: CANCELLATION REASONS
# ==========================================

cancellation_counts = (
    df[df["Ride_Status"] == "Cancelled"]["Cancellation_Reason"]
    .value_counts()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))

plt.bar(
    cancellation_counts.index,
    cancellation_counts.values
)

plt.title("Cancellation Reasons")
plt.xlabel("Cancellation Reason")
plt.ylabel("Number of Cancelled Rides")

plt.xticks(rotation=30, ha="right")

plt.tight_layout()

# Save graph as image
plt.savefig("Cancellation_Reasons.png")

# Display graph
plt.show()

# ==========================================
# VISUALIZATION 10: REVENUE BY VEHICLE TYPE
# ==========================================

vehicle_revenue = (
    df.groupby("Vehicle_Type")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

plt.bar(
    vehicle_revenue.index,
    vehicle_revenue.values
)

plt.title("Revenue by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.ylabel("Total Revenue")

plt.tight_layout()

# Save graph as image
plt.savefig("Revenue_by_Vehicle_Type.png")

# Display graph
plt.show()