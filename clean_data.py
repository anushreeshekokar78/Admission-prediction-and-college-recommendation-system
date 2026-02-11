import pandas as pd

data = pd.read_csv("final_dataset.csv")

print("Original Columns:")
print(data.columns)

print("Before Cleaning:", data.shape)

# Remove duplicates
data = data.drop_duplicates()

# Remove missing values
data = data.dropna()

# Drop first column if it's just index/Serial No
data = data.iloc[:,1:]

# Rename columns
data.columns = [
"GRE","TOEFL","UniRating","SOP","LOR","CGPA","Research","Chance"
]

data.to_csv("clean_dataset.csv", index=False)

print("After Cleaning:", data.shape)
print("Cleaning completed. clean_dataset.csv created.")
