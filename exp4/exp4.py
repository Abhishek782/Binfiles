import pandas as pd
import math

def calculate_entropy(data, class_column):
    class_counts = data[class_column].value_counts()
    entropy = 0

    for count in class_counts:
        probability = count / len(data)
        entropy -= probability * math.log2(probability)

    return entropy

def calculate_information_gain(data, attribute, class_column):
    total_entropy = calculate_entropy(data, class_column)

    attribute_entropy = 0
    attribute_values = data[attribute].unique()

    for value in attribute_values:
        subset = data[data[attribute] == value]
        subset_entropy = calculate_entropy(subset, class_column)
        weight = len(subset) / len(data)
        attribute_entropy += weight * subset_entropy

    information_gain = total_entropy - attribute_entropy
    return information_gain

# Load data from CSV
file_path = 'input_data.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Get the list of attributes (excluding the class column)
attributes = list(data.columns)
attributes.remove('PlayTennis')  # Replace 'PlayTennis' with your actual class column name

# Calculate and print information gain for each attribute
print("Information Gain for Each Attribute:")
for attribute_name in attributes:
    info_gain = calculate_information_gain(data, attribute_name, 'PlayTennis')
    print(f"{attribute_name}: {info_gain}")
