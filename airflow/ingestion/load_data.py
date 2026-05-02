import duckdb

con = duckdb.connect("/usr/local/airflow/warehouse/my_db.duckdb")

with open("/usr/local/airflow/ingestion/load_data.sql", "r") as f:
    con.execute(f.read())

print("Data loaded successfully ✅")