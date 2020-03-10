
from airflow import DAG
from datetime import datetime, timedelta

default_args = {
'owner': 'demo_afctl',
# 'depends_on_past': ,
# 'start_date': ,
# 'email': ,
# 'email_on_failure': ,
# 'email_on_retry': ,
# 'retries': 0

}

dag = DAG(dag_id='dummy', default_args=default_args, schedule_interval='@once')

    
