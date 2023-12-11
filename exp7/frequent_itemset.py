def read_transactions_from_csv(file_path):
    transactions = []
    with open(file_path, 'r') as csvfile:
        for line in csvfile:
            transaction = line.strip().split(',')
            transactions.append(set(transaction))
    return transactions

def generate_frequent_itemsets(transactions, min_support_percentage):
    num_transactions = len(transactions)
    min_support = (min_support_percentage / 100) * num_transactions

    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

    frequent_itemsets = []
    for item, count in item_counts.items():
        if count >= min_support:
            support_percentage = (count / num_transactions) * 100
            frequent_itemsets.append(([item], support_percentage))  # Include support in the tuple

    length = 2
    while True:
        candidates = []
        for i in range(len(frequent_itemsets) - 1):
            for j in range(i + 1, len(frequent_itemsets)):
                candidate = list(set(frequent_itemsets[i][0]) | set(frequent_itemsets[j][0]))
                if len(candidate) == length:
                    candidates.append(candidate)

        if not candidates:
            break

        frequent_candidates = []
        for candidate in candidates:
            support = sum(1 for transaction in transactions if set(candidate).issubset(transaction))
            if support >= min_support:
                support_percentage = (support / num_transactions) * 100
                frequent_itemsets.append((candidate, support_percentage))  # Include support in the tuple
                frequent_candidates.append(candidate)

        if not frequent_candidates:
            break

        length += 1

    return frequent_itemsets

if __name__ == "__main__":
    file_path = 'Itemset.csv'

    # Read transactions from CSV file
    transactions = read_transactions_from_csv(file_path)

    # Get minimum support from the user
    min_support_percentage = float(input("Enter the minimum support percentage (e.g., 2.5): "))

    # Generate frequent itemsets
    frequent_itemsets = generate_frequent_itemsets(transactions, min_support_percentage)

    # Display the result
    print("\nFrequent Itemsets:")
    for itemset, support_percentage in frequent_itemsets:
        print(f"{itemset} | Support: {support_percentage:.2f}%")
