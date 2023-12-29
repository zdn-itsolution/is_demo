import pandas as pd


def format_excel_data(excel_file, sheet_name):
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    return df.to_dict('records')
