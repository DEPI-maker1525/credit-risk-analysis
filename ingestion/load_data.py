import duckdb

con = duckdb.connect("warehouse/my_db.duckdb")

with open("ingestion/load_data.sql", "r") as f:
    con.execute(f.read())

print("Data loaded successfully ✅")