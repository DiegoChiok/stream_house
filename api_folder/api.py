import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WATCHMODE_API_KEY")

def get_trending_titles(page=1, genre_filter=None):
    url = f"https://api.watchmode.com/v1/list-titles/?apiKey={API_KEY}&types=movie&sort_by=popularity_desc&limit=20&page={page}"
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

        if details_response.status_code != 200:
            continue

        details = details_response.json()
        genres = details.get("genre_names", [])
        poster = details.get("poster")

        if genre_filter and genre_filter.lower() not in [g.lower() for g in genres]:
            continue

        movies.append({
            "title": t.get("title"),
            "year": t.get("year"),
            "poster": poster
        })

    return movies
