import csv
from collections import defaultdict
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Read the CSV file containing transaction data
input_file_path = 'transaction_data.csv'

# Dictionary to store transactions
transactions = defaultdict(list)

# Read and process the CSV file
with open(input_file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Filter out empty values
        items = [item.strip() for item in row if item.strip()]
        # Skip empty rows
        if items:
            transactions[len(transactions) + 1] = items

# Convert transactions to a list for MLxtend
transaction_list = list(transactions.values())

# Use TransactionEncoder to transform the data into a format suitable for Apriori
te = TransactionEncoder()
te_ary = te.fit(transaction_list).transform(transaction_list)
transformed_df = pd.DataFrame(te_ary, columns=te.columns_)

# Get user input for the minimum support threshold
min_support = float(input("Enter the minimum support threshold (a value between 0 and 1): "))

# Find frequent itemsets using the Apriori algorithm
frequent_itemsets = apriori(transformed_df, min_support=min_support, use_colnames=True)

# Print the frequent itemsets
print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Find association rules
min_confidence = float(input("Enter the minimum confidence threshold (a value between 0 and 1): "))
association_rules_df = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

# Exclude multiple columns from the association_rules_df
columns_to_exclude = ['leverage', 'conviction', 'zhangs_metric', 'lift']
association_rules_df = association_rules_df.drop(columns=columns_to_exclude, errors='ignore')

# Convert frozensets to sets for a more readable output
association_rules_df['antecedents'] = association_rules_df['antecedents'].apply(lambda x: set(x))
association_rules_df['consequents'] = association_rules_df['consequents'].apply(lambda x: set(x))

# Print the association rules
print("\nAssociation Rules:")
print(association_rules_df)

# Save the association rules to a new CSV file
output_rules_file_path = 'output_association_rules.csv'
association_rules_df.to_csv(output_rules_file_path, index=False)

print(f"\nAssociation rules saved to {output_rules_file_path}")
