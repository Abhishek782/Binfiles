import pandas as pd

# Read the CSV file
input_file_path = 'input_data.csv'
output_file_path_width = 'output_binned_data_width.csv'
output_file_path_quantile = 'output_binned_data_quantile.csv'
output_file_path_boundary = 'output_binned_data_boundary.csv'

# Load the data into a DataFrame
df = pd.read_csv(input_file_path)

# Extract the column to be binned
column_to_bin = 'value'  # Change this to the column you want to bin
data_to_bin = df[[column_to_bin]]

# Get user input for binning parameters
num_bins_width = int(input("Enter the number of bins for equal-width binning: "))
bin_labels_width = [f'Bin{i+1}' for i in range(num_bins_width)]  # You can customize bin labels

num_bins_quantile = int(input("Enter the number of bins for equal-frequency binning (quantiles): "))
bin_labels_quantile = [f'Bin{i+1}' for i in range(num_bins_quantile)]  # You can customize bin labels

# Perform equal-width binning
df_width = df.copy()  # Create a copy of the original DataFrame to store equal-width binning results
df_width['binned_width'] = pd.cut(data_to_bin[column_to_bin], bins=num_bins_width, labels=bin_labels_width, include_lowest=True)

# Display and print equal-width binned data
print("Equal-Width Binned Data:")
for label, group in df_width.groupby('binned_width', observed=False):
    print(f"{label}: {sorted(list(group['value']))}")

df_width.to_csv(output_file_path_width, index=False)
print(f"\nEqual-width binned data saved to {output_file_path_width}\n")

# Perform equal-frequency binning (quantile binning)
df_quantile = df.copy()  # Create a copy of the original DataFrame to store equal-frequency binning results
df_quantile['binned_quantile'] = pd.qcut(data_to_bin[column_to_bin], q=num_bins_quantile, labels=bin_labels_quantile)

# Display and print equal-frequency binned data
print("Equal-Frequency Binned (Quantile) Data:")
for label, group in df_quantile.groupby('binned_quantile', observed=False):
    print(f"{label}: {sorted(list(group['value']))}")

df_quantile.to_csv(output_file_path_quantile, index=False)
print(f"\nEqual-frequency binned (quantile) data saved to {output_file_path_quantile}\n")

# Get user input for boundary binning
num_bins_boundary = int(input("Enter the number of bins for boundary binning: "))
bin_labels_boundary = [f'Bin{i + 1}' for i in range(num_bins_boundary)]

# Perform boundary binning
df_boundary = df.copy()  # Create a copy of the original DataFrame to store boundary binning results
df_boundary['binned_boundary'] = pd.qcut(df_boundary[column_to_bin], q=num_bins_boundary, labels=bin_labels_boundary)

# Replace each element in the bin with its closest boundary value (max or min)
for bin_label, group in df_boundary.groupby('binned_boundary', observed=False):
    max_value = group['value'].max()
    min_value = group['value'].min()
    
    # Replace each element with the closest boundary value
    df_boundary.loc[df_boundary['binned_boundary'] == bin_label, 'value'] = df_boundary.apply(
        lambda row: max_value if abs(row['value'] - max_value) < abs(row['value'] - min_value) else min_value,
        axis=1
    )

# Display and print boundary binned data
print("Boundary Binned Data (Closest Boundary):")
for label, group in df_boundary.groupby('binned_boundary', observed=False):
    print(f"{label}: {sorted(list(group['value']))}")

df_boundary.to_csv(output_file_path_boundary, index=False)
print(f"\nBoundary binned data (closest boundary) saved to {output_file_path_boundary}\n")
