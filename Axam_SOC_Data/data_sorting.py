import pandas as pd

# Path to your Excel file
excel_file = 'SRI_LAB_VM0042_Project.xlsx'

# Name of the sheet you want to read
sheet_name = 'VM042_OC_SRI_Combine'  # Change this to your actual sheet name

# Read the specific sheet into a DataFrame
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Display the first few rows
#print(df)
#print(df.columns)

# Sorting our data by depth
# DataFrame where Depth (cm) == "0-15"
df_0_15 = df[df["Depth (cm)"] == "0-15"]

# DataFrame where Depth (cm) == "15-30"
df_15_30 = df[df["Depth (cm)"] == "15-30"]

# Set display options
pd.set_option('display.max_rows', None)    # Show all rows
pd.set_option('display.max_columns', None) # Show all columns
pd.set_option('display.width', None)       # No line width limit
pd.set_option('display.max_colwidth', None) # Show full content in columns

# Optionally, display them
#print("0-15cm:")
#print(df_0_15)
#print("\n15-30cm:")
#print(df_15_30)

# Column names
soc_col = "Soil Organic Carbon                      (%)"
bd_col = 'Bulk Density (g/cm3)'

# SOC per area for 0-15cm layer of soil
soc_mean_0_15 = df_0_15[soc_col].mean(skipna=True)
bd_mean_0_15 = df_0_15[bd_col].mean(skipna=True)
soc_0_15 = soc_mean_0_15/100 * bd_mean_0_15 * 15

print()
print("SOC % (0-15 cm) average: ", soc_mean_0_15)
print("BD (0-15 cm) average: ", bd_mean_0_15)
print("SOC (0-15 cm) (g/cm^3): ", soc_mean_0_15 * bd_mean_0_15)
print("SOC (0-15 cm) (g/cm^2): ", soc_0_15)
print("SOC (0-15 cm) (t C/ha): ", soc_0_15*100)

# SOC per area for 15-30cm layer of soil
soc_mean_15_30 = df_15_30[soc_col].mean(skipna=True)
bd_mean_15_30 = df_15_30[bd_col].mean(skipna=True)
soc_15_30 = soc_mean_15_30/100 * bd_mean_15_30 * 15

print()
print("SOC % (15-30 cm) average: ", soc_mean_15_30)
print("BD (15-30 cm) average: ", bd_mean_15_30)
print("SOC (15-30 cm) (g/cm^3): ", soc_mean_15_30 * bd_mean_15_30)
print("SOC (15-30 cm) (g/cm^2): ", soc_15_30)
print("SOC (15-30 cm) (t C/ha): ", soc_15_30*100)

# Net SOC per area (t C/ha)
net_soc = (soc_0_15 + soc_15_30)*100
print()
print("Net SOC (0-30 cm) (t C/ha): ", net_soc)
