import requests
import json
from datetime import datetime

def save_json_response(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

api_url = "https://www.cineworld.co.uk/uk/data-api-service/v1/quickbook/10108/film-events/in-cinema/103/at-date/2023-10-21?attr=&lang=en_GB"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

try:
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        save_json_response(data, f"{timestamp}_cineworld_data.json")
    else:
        print(f"Request failed with status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
