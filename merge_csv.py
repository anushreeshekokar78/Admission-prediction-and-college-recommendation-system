import pandas as pd

# Load both CSV files
df1 = pd.read_csv("Admission_Predict_Ver1.1.csv")
df2 = pd.read_csv("Admission_Predict.csv")

# Merge (stack rows)
merged = pd.concat([df1, df2], ignore_index=True)

# Save final dataset
merged.to_csv("final_dataset.csv", index=False)

print("Done! final_dataset.csv created.")
