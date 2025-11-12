import pandas as pd
import numpy as np

# Path to your Excel file
excel_file = 'SRI_LAB_VM0042_Project.xlsx'

# Name of the sheet you want to read
sheet_name = 'VM042_OC_SRI_Combine'  # Change this to your actual sheet name

# Read the specific sheet into a DataFrame
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Get unique values in the "FAO LEGEND" column
unique_fao = df["FAO LEGEND"].unique()

print("Unique FAO LEGEND values:")
print(unique_fao)

# If you also want counts of each unique value:
fao_counts = df["FAO LEGEND"].value_counts()

print("\nCounts of FAO LEGEND values:")
print(fao_counts)
print()

avg_bd = df["Bulk Density (g/cm3)"].mean(skipna=True)

for value in unique_fao:
	# Filter rows
	subset = df[df["FAO LEGEND"] == value]
	values = subset["Soil Organic Carbon (%)"].dropna()
	for val in values:
		val = val*avg_bd*30
	
	# Sample size
	n = len(values)

	# Calculate the average Soil Organic Carbon (%)
	avg_soc = subset["Soil Organic Carbon (%)"].mean(skipna=True)
	variance_of_mean = values.var(ddof=1)
	sem = values.std(ddof=1) / np.sqrt(n)
	print("Average SOC", value, " (t/ha): ", avg_soc*avg_bd*30)
	print("Variance of the mean:", variance_of_mean)
	print("Standard Error of the mean:", sem*avg_bd*30)
	print()
