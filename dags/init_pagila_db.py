from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

default_args = {
    'owner': 'data_engineer',
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='init_pagila_db',
    default_args=default_args,
    schedule_interval=None, 
    catchup=False,
    template_searchpath=['/opt/source_scripts'] 
) as dag:

    create_schema = PostgresOperator(
        task_id='create_schema',
        postgres_conn_id='postgres_pagila_conn',
        sql='pagila-schema.sql'
    )

    insert_data = PostgresOperator(
        task_id='insert_data',
        postgres_conn_id='postgres_pagila_conn',
        sql='pagila-insert-data.sql'  
                                     
    )

    create_schema >> insert_data