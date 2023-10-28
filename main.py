import pandas as pd
import psycopg2
import yaml

def read_csv(file_name):
    return pd.read_csv(file_name)

def upload_to_postgres(df, config):
    connection = psycopg2.connect(
        host='localhost',
        port=config['port'],
        user=config['username'],
        password=config['password'],
        dbname=config['database']
    )
    cursor = connection.cursor()

    # Create table if not exists
    cols = ",".join([f"{col} TEXT" for col in df.columns])
    create_table_query = f"CREATE TABLE IF NOT EXISTS data ({cols});"
    cursor.execute(create_table_query)
    connection.commit()

    # Insert data
    for _, row in df.iterrows():
        columns = ','.join(row.keys())
        values = ','.join([f"'{val}'" for val in row])
        insert_query = f"INSERT INTO data ({columns}) VALUES ({values})"
        cursor.execute(insert_query)
        connection.commit()

    cursor.close()
    connection.close()

if __name__ == "__main__":
    with open("config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)
        
    df = read_csv("data.csv")
    upload_to_postgres(df, config['postgresql'])
