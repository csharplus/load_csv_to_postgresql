#!/bin/bash

# Setup python virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Install psql
brew install postgresql

# Generate sample data for data.csv
echo "column1,column2,column3" > data.csv
echo "value1,value2,value3" >> data.csv
echo "value4,value5,value6" >> data.csv

# Start a PostgreSQL docker instance
docker run --name postgres-docker -e POSTGRES_USER=test_username -e POSTGRES_PASSWORD=test_password -e POSTGRES_DB=test_database -p 5432:5432 -d postgres
