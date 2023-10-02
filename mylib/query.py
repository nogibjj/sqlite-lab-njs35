"""Query the database"""

import sqlite3
import pandas as pd


def get_df_and_print_head(query, conn, head_size=10):
    """Return a dataframe and print the head"""
    df = pd.read_sql_query(query, conn)
    # drop frist row
    df.reset_index(drop=True, inplace=True)
    print(df.head(head_size))
    return df


def query_db(query="SELECT * FROM seattle_weather LIMIT 6"):
    """Query the database given an input query"""
    conn = sqlite3.connect("Weather.db")
    if query.lower().startswith("select"):
        df = get_df_and_print_head(query, conn, head_size=10)
        conn.close()
        return df
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    print("Query executed successfully.")
    query_results = cursor.fetchall()
    conn.close()
    return query_results



