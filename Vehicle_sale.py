import pandas as pd

# Load the CSV file (use correct encoding for special characters)
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# Display original info
print("Original Data Shape:", df.shape)
print("Columns:", df.columns.tolist())

# Step 1: Drop rows with critical missing values
df.dropna(subset=['SALES', 'ORDERDATE', 'CUSTOMERNAME'], inplace=True)

# Step 2: Convert ORDERDATE to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')
df.dropna(subset=['ORDERDATE'], inplace=True)  # Drop rows with invalid dates

# Step 3: Convert numeric columns
df['SALES'] = pd.to_numeric(df['SALES'], errors='coerce')
df.dropna(subset=['SALES'], inplace=True)

# Step 4: Create new date columns
df['Year'] = df['ORDERDATE'].dt.year
df['Month'] = df['ORDERDATE'].dt.month_name()

# Step 5: Rename columns for readability (optional)
df.rename(columns={
    'CUSTOMERNAME': 'Customer Name',
    'PRODUCTLINE': 'Product Line',
    'ORDERNUMBER': 'Order Number',
    'DEALSIZE': 'Deal Size'
}, inplace=True)

# Step 6: Drop unnecessary columns (optional)
columns_to_drop = ['POSTALCODE', 'TERRITORY', 'PHONE']
df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

# Final info
print("Cleaned Data Shape:", df.shape)
print("Cleaned Columns:", df.columns.tolist())

# Step 7: Save cleaned dataset
df.to_csv("sales_data_cleaned.csv", index=False)
print("Cleaned dataset saved as 'sales_data_cleaned.csv'")
