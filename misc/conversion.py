import pandas as pd
import numpy as np

# Load the dataset, assuming the first row contains column names
file_path = "data.csv"  # Update with your actual file path
df = pd.read_csv(file_path)

# Remove the 'name' column
df = df.drop(columns=["name"], errors="ignore")

# Convert the DataFrame to a NumPy array
data_array = df.to_numpy()

# Save as a .npy file
np.save("parkinsons.npy", data_array)

print("Conversion complete: 'parkinsons.npy' has been saved.")
