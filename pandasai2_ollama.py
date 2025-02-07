import pandas as pd
import os
from pathlib import Path
import matplotlib.pyplot as plt
from langchain_community.llms import Ollama
from pandasai import SmartDatalake, SmartDataframe
import glob

# Initialize the LLM model
llm = Ollama(model="llama3.1")

dir_path = str(Path(os.path.dirname(__file__)))

# Path to the folder containing your CSV files
template_folder = os.path.join(dir_path, 'csv')

# Use glob to find all CSV files in the folder
csv_files = glob.glob(os.path.join(template_folder, "*.csv"))

dataframes = []  # List to hold pandas DataFrames
smart_dataframes = [] # List to hold SmartDataframes if you need them later

# Iterate through each CSV file
for file in csv_files:
    print(f"Processing file: {file}")

    # Read the current CSV file
    data = pd.read_csv(file, dtype=str)

    smart_data = SmartDataframe(data) # Create the SmartDataframe, but don't use it for the lake
    smart_dataframes.append(smart_data)

    dataframes.append(data) # Append the original pandas DataFrame

# Create a SmartDatalake using the list of pandas DataFrames
lake = SmartDatalake(dataframes, config={"llm": llm, "verbose": True})  # Corrected line
response = lake.chat("calculate average of age column")
print(response)

# Now you can use the smart_dataframes list for any SmartDataframe specific operations if needed.
# Example:
# for sdf in smart_dataframes:
#     print(sdf.describe())
