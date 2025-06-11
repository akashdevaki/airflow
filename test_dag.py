from airflow import DAG
     from airflow.operators.python import PythonOperator
     from datetime import datetime
 
     def my_task():
         print("Hello from Airflow!")
 
     with DAG(
         dag_id='my_simple_dag',
         start_date=datetime(2023, 1, 1),
         schedule=None,
         catchup=False
     ) as dag:
         task1 = PythonOperator(
             task_id='print_hello',
             python_callable=my_task
         )
