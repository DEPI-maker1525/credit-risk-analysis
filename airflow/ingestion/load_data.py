import duckdb

<<<<<<< HEAD
con = duckdb.connect("warehouse/my_db.duckdb")

with open("ingestion/load_data.sql", "r") as f:
=======
con = duckdb.connect("/usr/local/airflow/warehouse/my_db.duckdb")

with open("/usr/local/airflow/ingestion/load_data.sql", "r") as f:
>>>>>>> 9f7674fcfb3ab1cdc9986f145d85e73397004e05
    con.execute(f.read())

print("Data loaded successfully ✅")