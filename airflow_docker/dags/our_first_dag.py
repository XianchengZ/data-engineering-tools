from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
  'owner': 'andrew',
  'etries': 5,
  'retry_delay': timedelta(minutes=2)
}

with DAG(
  dag_id='our_first_dag',
  default_args=default_args,
  description="this is our first dag that we write",
  start_date=datetime(2023, 9, 7, 2),
  schedule_interval='@daily'
  ) as dag:
  task1 = BashOperator(
    task_id='first_task',
    bash_command='echo hello world, first task here'
  )
  
  task2 = BashOperator(
    task_id='second_task',
    bash_command='echo second task'
  )
  
  task3 = BashOperator(
    task_id='third_task',
    bash_command='echo third task runs in parallel'
  )
  
  # one way
  # task1 >> task2
  # task1 >> task3
  
  # alternatively
  task1 >> [task2, task3]
  pass