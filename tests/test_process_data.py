import pandas as pd
from scripts import process_data

def test_clean_column_names():
    df = pd.DataFrame(columns=["Country Name", " Total Power"])
    cleaned_df = process_data.clean_column_names(df)
    assert cleaned_df.columns.tolist() == ["country_name", "total_power"]
