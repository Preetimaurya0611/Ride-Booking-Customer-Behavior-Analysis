# Ride Booking & Customer Behavior Analysis

## Project Overview

This project analyzes ride booking data to understand ride performance, customer behavior, revenue trends, cancellation patterns, payment preferences, vehicle performance, and peak-hour activity.

The analysis was performed using Python, Pandas, and Matplotlib to clean the dataset, perform exploratory data analysis, generate visualizations, and identify meaningful business insights.

## Objectives

* Analyze overall ride status and completion trends
* Understand customer behavior and customer types
* Analyze revenue by city, vehicle type, payment method, and booking source
* Identify common cancellation reasons
* Analyze distance categories and peak-hour activity
* Understand payment preferences
* Identify important business insights from ride booking data

## Tools & Technologies

* Python
* Pandas
* Matplotlib
* Microsoft Excel
* VS Code

## Python Libraries

* Pandas
* Matplotlib

## Dataset

The project uses ride booking and customer data containing information such as:

* Ride ID
* Customer ID
* Gender
* Age
* City
* Vehicle Type
* Ride Status
* Cancellation Reason
* Payment Method
* Booking Source
* Customer Type
* Distance
* Fare
* Revenue
* Customer Rating
* Promo Code
* Ride Date and Time

Two Excel files are included:

* `Ride_Booking_Raw_Data.xlsx` – Original dataset
* `Ride_Booking_Customer_Analysis_CLEAN.xlsx` – Cleaned dataset used for analysis

## Data Cleaning

The following data-cleaning steps were performed:

* Checked missing values
* Checked duplicate records
* Handled missing cancellation reasons
* Replaced missing promo codes with "No Promo"
* Standardized payment method values
* Created age groups using age ranges
* Verified data types and dataset structure

## Analysis Performed

The project includes analysis of:

* Ride Status
* Revenue by Ride Status
* City-wise Revenue and Ride Performance
* Vehicle Type Performance
* Customer Type
* Booking Source
* Payment Method
* Distance Category
* Gender
* Peak vs Off-Peak Rides
* Promo Code Usage
* Cancellation Reasons
* Age Group Distribution

## Visualizations

The following charts were created using Matplotlib:

1. Ride Status Distribution
2. City-wise Revenue
3. Vehicle Type Distribution
4. Distance Category Distribution
5. Peak vs Off-Peak Rides
6. Revenue by Payment Method
7. Customer Type Distribution
8. Age Group Distribution
9. Cancellation Reasons
10. Revenue by Vehicle Type

## Key Business Insights

1. **Ride Completion:** 64.5% of rides were completed, while 35.5% were either cancelled or resulted in a no-show.

2. **Revenue:** Completed rides generated total revenue of ₹105,248.65, with an average revenue of ₹203.97 per completed ride.

3. **City Performance:** Mumbai generated the highest revenue of ₹15,600.63 from 132 rides.

4. **Vehicle Performance:** Mini vehicles generated the highest revenue of ₹33,530.77 and had the highest ride volume.

5. **Customer Retention:** Repeat customers accounted for 94.75% of total rides and generated ₹99,279.79 in revenue.

6. **Payment Preference:** UPI was the most used payment method with 340 rides and ₹45,933.36 in revenue.

7. **Distance Pattern:** Medium-distance rides were the most common at 43.50%, followed by long-distance rides at 29.75%.

8. **Peak Hours:** Off-peak hours accounted for 64% of rides, generating ₹68,242.17 in revenue.

9. **Cancellation Reasons:** Payment issues and wrong pickup locations together accounted for approximately 37% of cancelled rides.

## Conclusion

This project demonstrates how Python and data analysis techniques can be used to transform raw ride booking data into meaningful business insights. The analysis helps identify revenue-driving factors, customer behavior patterns, payment preferences, operational challenges, and opportunities for improving ride completion and business performance.

## Author

**Preeti Satyanarayan Maurya**

B.Sc. IT Graduate | Aspiring Data Analyst

**Skills:** Python | SQL | Excel | Power BI | Tableau | Pandas | Matplotlib
