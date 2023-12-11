import pandas as pd
import numpy as np
import csv

def min_max_normalization(value, old_min, new_min, old_range, new_range):
    normalized_value = ((value - old_min) / old_range) * new_range + new_min
    return normalized_value

def standard_deviation(values):
    mean = np.mean(values)
    standard_deviation = 0
    for value in values:
        standard_deviation += (value - mean) ** 2
    std_dev = np.sqrt(standard_deviation / len(values))

    return std_dev

input_file = 'input_data.csv'

data = pd.read_csv(input_file)

values = data.values.flatten()
print("Original Values:")
print(values)

new_min = float(input("Enter the new minimum: "))
new_max = float(input("Enter the new maximum: "))

old_range = values.max(axis=0) - values.min(axis=0)
new_range = new_max - new_min

# Min-Max Normalization
normalized_values = [min_max_normalization(value, values.min(), new_min, old_range, new_range) for value in values]

# Z-score Normalization
std_deviation_data = standard_deviation(values)
standard_normalized_values = [(value - np.mean(values)) / std_deviation_data for value in values]

print("\nMin-Max Normalized Values:")
print(normalized_values)
print("\nZ-score Normalized Values:")
print(standard_normalized_values)

# Save the normalized values to CSV
output_file_minmax = 'output_data_minmax.csv'
output_file_zscore = 'output_data_zscore.csv'

with open(output_file_minmax, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Original", "Min-Max Normalized"])
    for original, normalized in zip(values, normalized_values):
        writer.writerow([original, normalized])

with open(output_file_zscore, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Original", "Z-score Normalized"])
    for original, normalized in zip(values, standard_normalized_values):
        writer.writerow([original, normalized])

print(f"\nMin-Max Normalized values saved to {output_file_minmax}")
print(f"Z-score Normalized values saved to {output_file_zscore}")


# Save all values to CSV
output_file_all = 'output_data_all.csv'

with open(output_file_all, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Original", "Min-Max Normalized", "Z-score Normalized"])
    for original, minmax, zscore in zip(values, normalized_values, standard_normalized_values):
        writer.writerow([original, minmax, zscore])

