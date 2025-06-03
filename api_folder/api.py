import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WATCHMODE_API_KEY")

BASE_POSTER_URL = "https://cdn.watchmode.com"  

def get_trending_titles():
    url = f"https://api.watchmode.com/v1/list-titles/?apiKey={API_KEY}&types=movie&sort_by=popularity_desc&limit=10"
    response = requests.get(url)
    if response.status_code != 200:
        return []

    data = response.json()
    titles = data.get("titles", [])
    movies = []

    for t in titles:
        title_id = t.get("id")
        details_url = f"https://api.watchmode.com/v1/title/{title_id}/details/?apiKey={API_KEY}"
        details_response = requests.get(details_url)

        if details_response.status_code == 200:
            details = details_response.json()
            poster = details.get("poster", None)  
            movies.append({
                "title": t.get("title"),
                "year": t.get("year"),
                "poster": poster
            })
        else:
            movies.append({
                "title": t.get("title"),
                "year": t.get("year"),
                "poster": None
            })

    return movies