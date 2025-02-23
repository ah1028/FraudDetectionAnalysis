import pandas as pd
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


query = '''SELECT * FROM transactions'''
cursor.execute(query)

output = cursor.fetchall()

# Print results
for row in output:
    print(row)

conn.commit()
conn.close()