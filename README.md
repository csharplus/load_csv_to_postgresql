# A data pipeline example

This data pipeline uploads a csv file to a PostgreSQL database. More detail is explained in the following Medium post: [Create a data pipeline using chatGPT to import a CSV file into a PostgreSQL database](https://medium.com/p/75835c95d34b)

## How to run this pipeline:
1. Grant execute permissions to bash scripts:
    ```bash
    chmod +x init.sh run.sh
    ```
2. Setup the environment and generate sample data:
    ```bash
    ./init.sh
    ```
3. Run the Python main program:
    ```bash
    ./run.sh
    ```
