import pandas as pd

# Load the dataset
data = pd.read_csv("../dataset/StudentPerformanceFactors.csv")

# Display the first 5 rows
print(data.head())

# Display number of rows and columns
print("\nDataset Shape:")
print(data.shape)

# Display column names
print("\nColumn Names:")
print(data.columns)

# Display information about the dataset
print("\nDataset Information:")
print(data.info())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(data.duplicated().sum())
