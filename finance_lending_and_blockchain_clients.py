
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
data = pd.read_csv('industry_client_details.csv')

# Ensure column names are stripped of spaces
data.columns = data.columns.str.strip()

# Check if 'industry' column exists
if 'industry' not in data.columns:
    print("Error: The 'industry' column is missing from the dataset.")
else:
    # Count clients by category
    category_counts = data['industry'].value_counts()

    # Filter for Finance Lending and Block Chain categories
    selected_categories = category_counts.loc[['Finance Lending', 'Block Chain']].fillna(0)

    # Create a bar plot
    plt.figure(figsize=(8, 5))
    sns.barplot(
        x=selected_categories.index,
        y=selected_categories.values,
        hue=selected_categories.index,  # Use 'hue' for categories
        dodge=False,  # Disable hue dodging for single bars per category
        palette="viridis"
    )
    plt.legend([], frameon=False)  # Remove the legend (not needed for this use case)
    plt.title("Number of Finance Lending and Blockchain Clients")
    plt.xlabel("industry")
    plt.ylabel("Number of Clients")
    plt.show()

    # Output the counts
    for category, count in selected_categories.items():
        print(f"{category}: {count}")
