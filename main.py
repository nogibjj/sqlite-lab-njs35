"""
ETL-Query script
"""

import fire
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query_db


def main_query(query="SELECT * FROM seattle_weather LIMIT 6", title="Select the first 5 rows of data"):
    '''
    Wrapper for the query_db function from mylib/query.py
    Used to create a command line tool with Fire.

    CLI Example:
    python main.py --query="SELECT * FROM seattle_weather LIMIT 6" --title="Select the first 5 rows of data"
    '''
    print("\n"+title)
    query_db(query=query)


# Some pre-written, common queries for convienence

def find_max_temp():
    '''
    Pre-written query to find the maximum temperature recorded in the data.
    '''
    query = "SELECT MAX(temp_max) FROM seattle_weather"
    title = "Find the maximum temperature recorded in the data"
    print("\n"+title)
    query_db(query=query)

def find_avg_wind():
    '''
    Pre-written query to find the average wind speed recorded in the data.
    '''
    query = "SELECT AVG(wind) FROM seattle_weather"
    title = "Find the average wind speed recorded in the data"
    print("\n"+title)
    query_db(query=query)


if __name__ == "__main__":
    # ETL
    extract()
    load()
    # Query
    fire.Fire(main_query)

    #find_max_temp()
    #find_avg_wind()
    