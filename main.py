import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Display transaction type against count of fraudulant transactions
query = '''SELECT Transaction_Type, COUNT(*) AS count FROM transactions WHERE Fraud_Label=1 GROUP BY Transaction_Type'''
cursor.execute(query)
output = cursor.fetchall()
labels, y = zip(*output)
plt.pie(y, labels=labels)
plt.show()

conn.commit()
conn.close()