"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv
import os


def transform_csv(csv_file):
    '''Removes all empty lines from the csv file'''
    with open(csv_file, 'r') as f:
        lines = f.readlines()
        lines = [line for line in lines if line.strip()]
    with open(csv_file, 'w') as f:
        f.writelines(lines)


#load the csv file and insert into a new sqlite3 database
def load(dataset="/workspaces/sqlite-lab-njs35/data/seattle_weather.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""
    # Transform
    transform_csv(dataset)
    
    # Load
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('Weather.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS seattle_weather")
    c.execute('''
        CREATE TABLE seattle_weather (
            date TEXT,
            precipitation REAL, 
            temp_max REAL,
            temp_min REAL,
            wind REAL,
            weather TEXT
        )
    ''')
    c.executemany("INSERT INTO seattle_weather VALUES (?,?,?,?,?,?)", payload)
    conn.commit()
    conn.close()
    return "Weather.db"

