import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
subscription_data = pd.read_csv('subscription_information.csv')  # Dataset 1
company_data = pd.read_csv('industry_client_details.csv')       # Dataset 2

# Merge the datasets on 'client_id'
merged_data = pd.merge(subscription_data, company_data, on='client_id', how='inner')

# Group by Industry to calculate total clients and renewals
industry_grouped = merged_data.groupby('industry').agg(
    Total_Clients=('client_id', 'count'),
    Renewed_Clients=('renewed', 'sum')  # Assuming 'renewed' is 1 for yes and 0 for no
).reset_index()

# Calculate renewal rate for each industry
industry_grouped['Renewal Rate (%)'] = (industry_grouped['Renewed_Clients'] / industry_grouped['Total_Clients']) * 100

# Find the industry with the highest renewal rate
highest_renewal_industry = industry_grouped.loc[industry_grouped['Renewal Rate (%)'].idxmax()]

print("Renewal Rates by Industry:")
print(industry_grouped)
print("\nIndustry with the highest renewal rate:")
print(highest_renewal_industry)

# Visualization: Bar chart of renewal rates
plt.figure(figsize=(12, 6))
sns.barplot(x='industry', y='Renewal Rate (%)', data=industry_grouped,
            hue = 'industry', # Assigning 'industry' to hue
            dodge = False,    # Ensure single bars per industry
            palette='coolwarm')# used color palette
plt.legend([], frameon = False) #Remove legend for clarity
plt.title("Renewal Rates by Industry")
plt.xlabel("Industry")
plt.ylabel("Renewal Rate (%)")
plt.xticks(rotation=45)  # Rotate industry names for clarity
plt.show()
