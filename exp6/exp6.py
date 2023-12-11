# Read the CSV file
input_file_path = 'input_data.csv'

# Initialize variables to store the 5-number summary
data = []

# Read the data from the CSV file, skipping the header
with open(input_file_path, 'r') as file:
    next(file)  # Skip the header
    # Extract numerical values from each line and store in the data list
    for line in file:
        value = float(line.strip().split(',')[0])
        data.append(value)

# Sort the data in ascending order
sorted_data = sorted(data)

# Calculate the 5-number summary
min_value = sorted_data[0]
q1 = sorted_data[int(len(sorted_data) * 0.25)]
median = sorted_data[int(len(sorted_data) * 0.5)]
q3 = sorted_data[int(len(sorted_data) * 0.75)]
max_value = sorted_data[-1]

# Print the 5-number summary
print("5-Number Summary:")
print(f"min: {min_value}")
print(f"Q1: {q1}")
print(f"median: {median}")
print(f"Q3: {q3}")
print(f"max: {max_value}")

# Save the 5-number summary to a new CSV file
output_file_path_summary = 'output_5_number_summary.csv'
with open(output_file_path_summary, 'w') as output_file:
    output_file.write("Statistic,Value\n")
    output_file.write("min,{:.2f}\n".format(min_value))
    output_file.write("Q1,{:.2f}\n".format(q1))
    output_file.write("median,{:.2f}\n".format(median))
    output_file.write("Q3,{:.2f}\n".format(q3))
    output_file.write("max,{:.2f}\n".format(max_value))

print(f"\n5-Number summary saved to {output_file_path_summary}")
