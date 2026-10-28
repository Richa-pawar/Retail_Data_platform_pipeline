from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta


default_args = {
    "owner": "richa",
    "retries": 2,
    "retry_delay": timedelta(minutes=5)
}


with DAG(
    dag_id="shopify_ingestion_pipeline",
    default_args=default_args,
    description="Extract Shopify data into Bronze layer",
    start_date=datetime(2026,10,28),
    schedule="@daily",
    catchup=False
) as dag:


    extract_shopify = BashOperator(
        task_id="extract_shopify_data",
        bash_command="""
        python /opt/airflow/project/api/shopify_ingestion.py
        """
    )


    extract_shopify