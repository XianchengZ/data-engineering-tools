# Airflow using Docker

## Setup

In my opinion, it is so much better to run everything inside of docker.

### Fetch the `docker-compose.yaml`

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.0/docker-compose.yaml'
```

To run docker locally, we need to change several things

- Change `AIRFLOW__CORE__EXECUTOR: CeleryExecutor` to `AIRFLOW**CORE**EXECUTOR: LocalExecutor
- Delete

```yaml
AIRFLOW__CELERY__RESULT_BACKEND: db+postgresql://airflow:airflow@postgres/airflow
AIRFLOW__CELERY__BROKER_URL: redis://:@redis:6379/0
```

- Delete Redis dependencies and redies server
- Delete celery worker and flower

### Create folders for dags, logs, plugins, and configs

```bash
mkdir -p ./dags ./logs ./plugins ./config
```

Add `AIRFLOW_UID=50000` to .env file

Then start it

```bash
docker compose up airflow-init
```

then we can run the airflow in the background by

```bash
docker compose up -d
```

The username and password are both airflow

### Clean up

• Run `docker compose down --volumes --remove-orphans` command in the directory you downloaded the `docker-compose.yaml` file
