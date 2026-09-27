import sqlite3
import pandas as pd

df = pd.read_csv("data/books_cleaned.csv")

connection = sqlite3.connect("database/jobs.db")

df.to_sql("jobs", connection, if_exists="replace", index=False)

print("Data successfully stored in SQLite!")

connection.close()