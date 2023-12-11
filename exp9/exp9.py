import pandas as pd

# Read the CSV file
input_file_path = 'input_data.csv'

# Load the data into a DataFrame
df = pd.read_csv(input_file_path)

# Choose the two columns for which you want to find the correlation coefficient
column1 = 'column1'  # Replace with your actual column name
column2 = 'column2'  # Replace with your actual column name

# Extract the data for the selected columns
data1 = df[column1]
data2 = df[column2]

# Calculate the mean of each column
mean1 = data1.mean()
mean2 = data2.mean()

# Calculate the numerator and denominator for the correlation coefficient formula
numerator = ((data1 - mean1) * (data2 - mean2)).sum()
denominator = ((data1 - mean1)**2).sum() * ((data2 - mean2)**2).sum()

# Calculate the correlation coefficient
correlation_coefficient = numerator / (denominator**0.5)

# Print the correlation coefficient
print(f"The correlation coefficient between {column1} and {column2} is: {correlation_coefficient}")
