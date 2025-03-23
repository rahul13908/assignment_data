import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
payment_data = pd.read_csv('payment_information.csv')  # Dataset 1
client_data = pd.read_csv('industry_client_details.csv')  # Dataset 2

# Merge datasets on 'client_id'
merged_data = pd.merge(payment_data, client_data, on='client_id', how='inner')

# Convert 'payment_date' to datetime format and extract the year
merged_data['payment_date'] = pd.to_datetime(merged_data['payment_date'], errors='coerce')
merged_data['year'] = merged_data['payment_date'].dt.year

# Group by year and payment method to calculate the median amount paid
median_paid_per_year = merged_data.groupby(['year', 'payment_method'])['amount_paid'].median().reset_index()

# Print the results
print("Median Amount Paid Each Year for All Payment Methods:")
print(median_paid_per_year)

# Visualization: Bar Plot
plt.figure(figsize=(12, 6))
sns.barplot(
    x='year', 
    y='amount_paid', 
    hue='payment_method', 
    data=median_paid_per_year, 
    palette='viridis'
)
plt.title("Median Amount Paid Each Year for All Payment Methods")
plt.xlabel("Year")
plt.ylabel("Median Amount Paid")
plt.legend(title="Payment Method")
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.show()
