
import sqlite3
import pandas as pd
import pathlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import logging

# Your code here....
# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")

# Define the database file in the current root project directory
db_file = pathlib.Path("project.db")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_file", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        dry_bean_path = pathlib.Path("dry_bean_dataset.csv")
       
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            dry_bean_dataset_df.to_sql("dry_bean_dataset", conn, if_exists="replace", index=False)
      
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)



db_filepath = pathlib.Path("C:\\Users\\blehman\\Projects\\datafun-05-sql\\project.db")

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

    logging.info("All SQL operations completed successfully")

if __name__ == "__main__":
    main()


    logging.info("All SQL operations completed successfully")


