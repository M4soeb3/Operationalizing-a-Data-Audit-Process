from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Import data validation functions
from scripts.validate_data import validate_schema, check_completeness, detect_outliers

# Default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG('data_audit_pipeline', default_args=default_args, schedule_interval='@daily') as dag:
    
    # Task for schema validation
    schema_validation = PythonOperator(
        task_id='validate_schema',
        python_callable=validate_schema,
        op_kwargs={'dataframe': data, 'schema': expected_schema}
    )
    
    # Task for completeness check
    completeness_check = PythonOperator(
        task_id='check_completeness',
        python_callable=check_completeness,
        op_kwargs={'dataframe': data, 'required_columns': required_columns}
    )
    
    # Task for outlier detection
    outlier_detection = PythonOperator(
        task_id='detect_outliers',
        python_callable=detect_outliers,
        op_kwargs={'dataframe': data, 'column': 'amount'}
    )

    # Task dependencies
    schema_validation >> completeness_check >> outlier_detection
