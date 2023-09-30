"""Query the database"""

import sqlite3
import pandas as pd
import fire


def get_df_and_print_head(query, conn, head_size=10):
    """Return a dataframe and print the head"""
    df = pd.read_sql_query(query, conn)
    df.reset_index(drop=True, inplace=True)
    print(df.head(head_size))
    return df


def query_db(query="SELECT * FROM seattle_weather LIMIT 6"):
    """Query the database given an input query"""
    conn = sqlite3.connect("Weather.db")
    df = get_df_and_print_head(query, conn, head_size=10)
    conn.close()
    return "Success"


