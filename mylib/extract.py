"""
Extract a dataset from a github raw csv URL. 

Seattle Weather Data
"""
import requests


def extract(url="https://raw.githubusercontent.com/vega/vega/main/docs/data/seattle-weather.csv", 
            file_path="data/seattle_weather.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



