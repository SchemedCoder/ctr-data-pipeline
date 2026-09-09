from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_pipeline():
    subprocess.run(["python", "/path/to/etl/ctr_pipeline.py"])

dag = DAG(
    "ctr_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
)

task = PythonOperator(
    task_id="run_ctr_pipeline",
    python_callable=run_pipeline,
    dag=dag
)

