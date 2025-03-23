# assignment_data
This repository contains Python scripts for performing data analysis and visualization on diverse datasets. Tasks include identifying client patterns, calculating key metrics, and exploring relationships between economic and subscription data.
## Table of Contents
•	Project Overview
•	Features
•	Technologies Used
•	Setup and Installation
•	Tasks and Descriptions 
o	1. Median Amount Paid by Year
o	2. Inflation Rate for Renewed Subscriptions
o	3. Finance Lending and Blockchain Client Count
o	4.The organization has the highest renewal rate
•	Visualization Examples
•	How to Contribute
•	Contact

## Project Overview
The purpose of this project is to process and analyze CSV-based datasets to answer key business questions. Examples include calculating payment trends, evaluating renewal performance, and understanding client segmentation. The provided Python code performs data cleaning, aggregation, and visualization to extract meaningful insights.
## Features
•	Data Merging: Combines datasets based on common keys for deeper analysis.
•	Aggregation: Calculates key metrics like median, average, and counts.
•	Visualization: Bar charts and histograms for exploring trends.
•	Error Handling: Ensures robust data processing with proper error management.
## Technologies Used
•	Python 3.x
•	Libraries: 
o	pandas for data manipulation.
o	matplotlib and seaborn for visualization.

## Tasks and Descriptions
 1. Median Amount Paid by Year
Goal: Calculate the median amount paid each year for all payment methods.
Input:
•	date_set1.csv: Contains client_id, payment_date, amount_paid, and payment_method.
•	date_set2.csv: Contains client_id, company_size, industry, and location.
Output:
•	A grouped table showing the median amount paid each year for each payment method.
•	A bar chart for visualization.
Key Functions:
•	pandas.merge(): Combines payment and client data.
•	.groupby(): Groups by year and payment method.
•	.median(): Calculates the median payment.

## 2. Inflation Rate for Renewed Subscriptions
Goal: Analyze the average inflation rate during renewed subscriptions.
Input:
•	date_set1.csv: Contains start_date, end_date, inflation_rate, and gdp_growth_rate.
•	date_set2.csv: Contains client_id, start_date, end_date, and renewed.

Output:
•	Prints the average inflation rate for renewed subscriptions.
•	A histogram showing the distribution of inflation rates.
Key Functions:
•	pd.to_datetime(): Converts date columns to datetime format.
•	.merge(): Joins subscription and economic data on end_date.
 ## 3. Finance Lending and Blockchain Client Count
Goal: Count the number of clients in Finance Lending and Blockchain industries.
Input:
•	A CSV file containing client details with columns: Client ID and Industry.
Output:
•	Prints the counts for Finance Lending and Blockchain clients.
•	A bar chart showing the results.
Key Functions:
•	.value_counts(): Counts occurrences of each industry.
•	.loc[]: Filters specific industries.
## Visualization Examples
1.	Bar Chart: Median payments by year and payment method.
2.	Histogram: Distribution of inflation rates during renewed subscriptions.
3.	Industry Comparison: Client count for Finance Lending and Blockchain industries.
## Contact
For any questions or feedback, please contact:
•	Name: Rahul kumar
•	Email: Rahul.jan93@gmail.com

