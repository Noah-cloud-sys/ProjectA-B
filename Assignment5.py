
# Program Name: Assignment5.py
# Course:    IT3833/Section 01/W02
# Student Name: David Touchstone
# Assignment Number:  Lab5
# Due Date:  04/28/2025
# Purpose:   Pull the temperature readings from an input file,then average out the temperatures for Sunday and Thursday.
#            
# Resources: Python “sqlite3” module docs: https://docs.python.org/3/library/sqlite3.html

import sqlite3 #Pulling SQlite database
import re

DB_NAME    = 'temperatures.db'
TABLE_NAME = 'temperature_readings'
FILE_NAME  = r"C:\Users\noaht\Downloads\Assignment5input.txt"  #file path

def create_database():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            ID                 INTEGER PRIMARY KEY AUTOINCREMENT,
            Day_Of_Week        TEXT    NOT NULL,
            Temperature_Value  REAL    NOT NULL
        );
    ''')
    conn.commit()
    return conn

def insert_data(conn):
    c = conn.cursor()
    with open(FILE_NAME, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # split on commas / whitespace
            parts = re.split(r'[\s,]+', line)
            if len(parts) != 2:
                print(f"Skipping malformed line: {line}")
                continue

            day, temp_str = parts
            try:
                temp = float(temp_str)
            except ValueError:
                print(f"Skipping invalid temperature '{temp_str}' on line: {line}")
                continue

            c.execute(
                f'INSERT INTO {TABLE_NAME} (Day_Of_Week, Temperature_Value) VALUES (?, ?);',
                (day, temp)
            )

    # commit 
    conn.commit()

def compute_averages(conn, days):
    c = conn.cursor()
    results = {}
    for day in days:
        c.execute(
            f'SELECT AVG(Temperature_Value) FROM {TABLE_NAME} WHERE Day_Of_Week = ?;',
            (day,)
        )
        results[day] = c.fetchone()[0]
    return results

def main():
    conn = create_database()
    insert_data(conn)

    averages = compute_averages(conn, ['Sunday', 'Thursday'])
    for day, avg in averages.items():
        if avg is not None:
            print(f"Average temperature for {day}: {avg:.2f}")
        else:
            print(f"No data found for {day}.")

    conn.close()

if __name__ == '__main__':
    main()
