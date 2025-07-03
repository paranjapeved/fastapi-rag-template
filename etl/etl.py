import pandas as pd
from pprint import pprint
import json
import re

def load_data(file_path):
    df = pd.read_excel(file_path)
    return df
    
def remove_special_characters(text):
    return re.sub(b'[\\u00ae]', '', text)

def format_row(df, columns):
    json_data = []
    print(columns)
    for i in range(len(df)):
        description = ""
        for j, col in enumerate(columns):
            description += f"{col}: {df.iloc[i][j]}\n"
        json_data.append({
            "name": df.iloc[i]["Card name"].encode('ascii', 'ignore').decode(),
            "description": description.encode('ascii', 'ignore').decode()
        })
    return json_data

def transform_data_to_json(df):
    return df.to_json(orient="records")

if __name__ == "__main__":
    df = load_data("credit_cards.xlsx")
    columns = df.columns.tolist()
    json_data =format_row(df, columns)
    pprint(json_data)
    with open("credit_cards.json", "w") as f:
        f.write(json.dumps(json_data))