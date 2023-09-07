# Run Airflow Locally

We first need to clone the whole repo, then we need to get into this directory.

```shell
cd airflow_local
```

The next thing to do is to create the local python environment, for mac do

```shell
python3 -m venv py_env
```

Then we need to activate it.

```shell
source py_env/bin/activate
```

Then we will install all the required files.

```shell
pip install -r requirements.txt
```

## Airflow Part

### Install airflow

```shell
pip install 'apache-airflow==2.7.0' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.0/constraints-3.11.txt"
```

Set the airflow home directory.

```shell
export AIRFLOW_HOME=~/
```

Then we initialize the database

```shell
airflow db init
```

### Starting webserver

First we need to create a user, I already created a bash script so

```shell
./createUser.sh
```

Then we can run the web server. By default, the port is 8080

```shell
airflow webserver -p 8080
```

### Running DAG

We need to start the scheduler to run DAG. So we should open another terminal, get into the environment, and re-export airflow home directory. Then we are able to run the scheduler.

```shell
source py_env/bin/activate
export AIRFLOW_HOME=~/
airflow scheduler
```
