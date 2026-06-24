from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime

default_args = {
    'owner': 'data_engineer',
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='init_sakila_db',
    default_args=default_args,
    schedule_interval=None, 
    catchup=False,
    template_searchpath=['/opt/source_scripts']
) as dag:

    create_schema = SQLExecuteQueryOperator(
        task_id='create_schema',
        conn_id='mysql_sakila_conn',
        sql='sakila-schema.sql'
    )

    insert_data = SQLExecuteQueryOperator(
        task_id='insert_data',
        conn_id='mysql_sakila_conn',
        sql='sakila-data.sql'
    )

    create_schema >> insert_data