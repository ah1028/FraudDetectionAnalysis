import pandas as pd
import sqlite3

df = pd.read_csv("synthetic_fraud_dataset.csv")

df = df.astype({
    "Transaction_Type": str,
    "Timestamp": "datetime64[ns]",  
    "Device_Type": str,
    "Location": str,
    "Merchant_Category": str,
    "Card_Type": str,
    "Authentication_Method": str
})
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["Transaction_ID"] = df["Transaction_ID"].str.extract(r'(\d+)').astype(int)
df["User_ID"] = df["User_ID"].str.extract(r'(\d+)').astype(int)

print(df.dtypes)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

create_table = '''CREATE TABLE IF NOT EXISTS transactions(
                Transaction_ID INTEGER PRIMARY KEY,
                User_ID INTEGER,
                Transaction_Amount REAL,
                Transaction_Type TEXT,
                Timestamp TEXT,
                Account_Balance REAL,
                Device_Type TEXT,
                Location TEXT,
                Merchant_Category TEXT,
                IP_Address_Flag INTEGER,
                Previous_Fraudulent_Activity INTEGER,
                Daily_Transaction_Count INTEGER,
                Avg_Transaction_Amount_7d REAL,
                Failed_Transaction_Count_7d INTEGER,
                Card_Type TEXT,
                Card_Age INTEGER,
                Transaction_Distance REAL,
                Authentication_Method TEXT,
                Risk_Score REAL,
                Is_Weekend INTEGER,
                Fraud_Label INTEGER);'''

cursor.execute(create_table)

df.to_sql("transactions", conn, if_exists="append", index=False)

conn.commit()
conn.close()