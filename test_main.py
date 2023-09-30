"""
Test ETL-Query functions

"""
from main import main_query, find_avg_temp, find_avg_wind
from mylib.extract import extract
from mylib.transform_load import load


def test_main_query():
    """
    Test that the main query function returns a valid df
    """
    df = main_query(
        query="SELECT * FROM seattle_weather WHERE temp_max > 30 LIMIT 2",
        title="Select the first 5 rows of data",
    )
    temp_max_val = df.iloc[1]["temp_max"]
    assert int(temp_max_val) > 30


def test_find_max_temp():
    """
    Test that the find_max_temp function returns a valid df
    """
    df = find_avg_temp()
    temp_max_val = df.iloc[0]["AVG(temp_max)"]
    assert int(temp_max_val) > 0


def test_find_avg_wind():
    """
    Test that the find_avg_wind function returns a valid df
    """
    df = find_avg_wind()
    wind_val = df.iloc[0]["AVG(wind)"]
    assert int(wind_val) > 0


def test_etl():
    """
    Test that the etl functions return valid file paths
    """
    extract_path = extract()
    assert extract_path.endswith("seattle_weather.csv")
    transform_load_path = load()
    assert transform_load_path == "Weather.db"
