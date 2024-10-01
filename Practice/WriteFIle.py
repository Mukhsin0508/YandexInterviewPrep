import requests
import json

response = requests.get(url = "https://api.thecatapi.com/v1/images/search?limit=10")

response = response.json()

def json_to_txt_columns(input_json, output_file):
    with open(input_json, 'r') as f:
        data = json.load(f)

        if isinstance(data, dict):
            columns = list(data.keys())

    with open(output_file, 'w') as f:

        f.write('\t'.join(columns) + "\n")

        if isinstance(data, list):
            for item in data:
                row = [str(item.get(col , '')) for col in columns]
                f.write('\t'.join(row) + '\n')


input_json='response'
output_file='output_file'
json_to_txt_columns(input_json, output_file)
