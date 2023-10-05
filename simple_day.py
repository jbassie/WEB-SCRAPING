from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.python import PythonOperator
from airflow.operators.python import PythonVirtualenvOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from airflow.operators.email import EmailOperator


from datetime import datetime, timedelta


default_args = {
    "owner":"airflow",
    "email_on_failure": True,
    "email_on_retry": True,
    "email":"jsbazman@gmail.com",
    "retries": 3,
    "retry_delay": timedelta(minutes = 5)
}


def download_csv():
    """
    This function get data from a URL and saves it locally as CSV file in the specified path
    """

    import requests

    url = 'https://raw.githubusercontent.com/jbassie/WEB-SCRAPING/main/REAL_ESTATE/data/aruba_reality.csv'
    file_path = '/mnt/c/Users/ALIENWARE/Documents/LEARNING/data-engineering1/data/real_estate.csv'
    try:
        response = requests.get(url)
        if response.status_code ==200:
            with open(file_path, 'wb')  as file:
                file.write(response.content)
            print(f"File downloaded and Saved to {file_path}")
        else:
            print(f"Failed to download file {response.status_code}")
    except Exception as e:
        print(f"An Exception Occured: {str(e)}")


def convert_to_parquet():
    """
    Using Pandas Library,we will convert a csv file to a parquet file
    """
    import pandas as pd
    import fastparquet

    columns= ['name','location','property_status','property_type','price','bedrooms','bathrooms','Pool','Latitude','Longitude','link']
    import_data = pd.read_csv('/mnt/c/Users/ALIENWARE/Documents/LEARNING/data-engineering1/data/real_estate.csv')
    import_data = list(import_data)
    data = pd.DataFrame([import_data], columns=columns)
    data.to_parquet('/mnt/c/Users/ALIENWARE/Documents/LEARNING/data-engineering1/data/real_estate.parquet', engine= 'fastparquet')
    print("Sucessfully created a Parquet File")



with DAG('simple_dag', start_date = datetime(2023,9,29),
                schedule_interval = '@daily', default_args = default_args, catchup = False) as dag:

    #check if the URL is available 
    is_data_available =  HttpSensor(
        task_id = 'is_data_available',
        http_conn_id = 'real_estate_api',
        endpoint = 'jbassie/WEB-SCRAPING/main/REAL_ESTATE/data/aruba_reality.csv',
        response_check = lambda response: "name" in response.text,
        poke_interval = 5,
        timeout = 20
    )

    download_csv = PythonVirtualenvOperator(
            task_id  = 'download_csv',
            python_callable = download_csv,
            dag = dag,
            email_on_failure = True,
            system_site_packages = True
    )

    #check if a real_estate.csv file is available locally
    is_real_estate_file_available = FileSensor(
            task_id = 'is_real_estate_file_available',
            fs_conn_id = 'data_path',
            filepath = 'real_estate.csv',
            poke_interval = 5,
            timeout = 20
    )

    convert_to_parquet = PythonVirtualenvOperator(
        task_id = 'convert_to_parquet',
        python_callable = convert_to_parquet,
        dag = dag,
        system_site_packages = True,
        email_on_failure = True
    )

    send_email_notification = EmailOperator(
        task_id = "send_email_notification",
        to = "jsbazman@gmail.com",
        subject = 'Simple Dag',
        html_content = "<h3> Congratulations, your pipeline was successful !!</h3>"
    )

is_data_available >> download_csv >> is_real_estate_file_available >> convert_to_parquet >> send_email_notification
