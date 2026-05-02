from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from pendulum import datetime
import duckdb
def load_data():
    con = duckdb.connect("/usr/local/airflow/warehouse/my_db.duckdb")
    with open("/usr/local/airflow/ingestion/load_data.sql", "r") as f:
        con.execute(f.read())

    print("Data loaded successfully ✅")
    con.close()
    
default_args={
    "owner":"airflow",
    "retries":1
}
with DAG(
    dag_id="pipeline_dag",
    default_args=default_args,
    schedule="@daily",
    start_date=datetime(2026, 4, 1),
    catchup=False
) as dag:
    ingestion_task = PythonOperator(
        task_id="ingestion_task",
        python_callable=load_data
    )

    dbt_build_task = BashOperator(
        task_id="dbt_build_task",
        bash_command="cd /usr/local/airflow/dbt_project && dbt build",
    )

ingestion_task >> dbt_build_task