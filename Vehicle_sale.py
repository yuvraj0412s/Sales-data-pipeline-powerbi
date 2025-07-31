import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

print("Original Data Shape:", df.shape)
print("Columns:", df.columns.tolist())

df.dropna(subset=['SALES', 'ORDERDATE', 'CUSTOMERNAME'], inplace=True)

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')
df.dropna(subset=['ORDERDATE'], inplace=True)  

df['SALES'] = pd.to_numeric(df['SALES'], errors='coerce')
df.dropna(subset=['SALES'], inplace=True)

df['Year'] = df['ORDERDATE'].dt.year
df['Month'] = df['ORDERDATE'].dt.month_name()
df.rename(columns={
    'CUSTOMERNAME': 'Customer Name',
    'PRODUCTLINE': 'Product Line',
    'ORDERNUMBER': 'Order Number',
    'DEALSIZE': 'Deal Size'
}, inplace=True)

columns_to_drop = ['POSTALCODE', 'TERRITORY', 'PHONE']
df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

print("Cleaned Data Shape:", df.shape)
print("Cleaned Columns:", df.columns.tolist())

df.to_csv("sales_data_cleaned.csv", index=False)
print("Cleaned dataset saved as 'sales_data_cleaned.csv'")
