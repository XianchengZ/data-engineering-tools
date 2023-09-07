from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
  'owner': 'andrew',
  'etries': 5,
  'retry_delay': timedelta(minutes=2)
}

def greet(ti):
  firstname = ti.xcom_pull(task_ids='get_name', key='first_name')
  lastname = ti.xcom_pull(task_ids='get_name', key='last_name')
  age = ti.xcom_pull(task_ids='get_age', key='age')
  print("Hello world from python callable")
  print("My first name is:", firstname)
  print("My last name is:", lastname)
  print("My age is:", age)

def get_name(ti):
  ti.xcom_push(key='first_name', value='andrew')
  ti.xcom_push(key='last_name', value='soft')

def get_age(ti):
  ti.xcom_push(key='age', value='21')

with DAG(
  dag_id='python_operator',
  default_args=default_args,
  description="DAG with python operator",
  start_date=datetime(2023, 9, 6, 2),
  schedule_interval='@daily'
  ) as dag:

  task1 = PythonOperator(
    task_id='python_greet',
    python_callable=greet,
  )
  
  
  task2 = PythonOperator(
    task_id='get_name',
    python_callable=get_name
  )
  
  get_age_task = PythonOperator(
    task_id='get_age',
    python_callable=get_age
  )
  
  
  [task2, get_age_task] >> task1