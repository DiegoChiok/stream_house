import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WATCHMODE_API_KEY")

def get_trending_titles():
    url = f"https://api.watchmode.com/v1/list-titles/?apiKey={API_KEY}&types=movie&sort_by=popularity_desc&limit=10"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        titles = data.get("titles", [])
        return [{
            "title": t.get("title"),
            "poster": t.get("poster"),
            "year": t.get("year")
        } for t in titles]
    else:
        return []
