import requests
import pandas as pd
import os
from datetime import datetime

def collect_data(api_url, params, output_dir='data/raw'):
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"social_media_data_{timestamp}.json")
        
        with open(output_file, 'w') as f:
            json.dump(data, f)
        
        print(f"Data collected and saved to {output_file}")
    else:
        print(f"Failed to collect data: {response.status_code}")

if __name__ == "__main__":
    API_URL = "https://api.example.com/data"  # Replace with actual API URL
    PARAMETERS = {
        'query': 'sentiment',
        'count': 100
    }
    
    collect_data(API_URL, PARAMETERS)