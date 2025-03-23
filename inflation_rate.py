import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
economic_data = pd.read_csv('finanical_information.csv')  # Dataset 1
subscription_data = pd.read_csv('subscription_information.csv')  # Dataset 2

# Ensure column names are stripped of spaces
economic_data.columns = economic_data.columns.str.strip()
subscription_data.columns = subscription_data.columns.str.strip()

# Filter rows where subscriptions were renewed
renewed_subscriptions = subscription_data[subscription_data['renewed'] == 1]

# Merge the two datasets on the start_date or end_date
merged_data = pd.merge(
    renewed_subscriptions, 
    economic_data, 
    left_on='end_date',  # Match the subscription end_date with the economic data
    right_on='end_date', 
    how='inner'
)

# Calculate the average inflation rate for renewed subscriptions
average_inflation_rate = merged_data['inflation_rate'].mean()

print(f"Average Inflation Rate for Renewed Subscriptions: {average_inflation_rate:.2f}%")

# Optional Visualization (Histogram of Inflation Rates for Renewed Subscriptions)
plt.figure(figsize=(10, 6))
plt.hist(merged_data['inflation_rate'], bins=10, color='skyblue', edgecolor='black')
plt.title("Inflation Rates for Renewed Subscriptions")
plt.xlabel("Inflation Rate (%)")
plt.ylabel("Frequency")
plt.show()
