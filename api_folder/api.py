import os
import requests
from dotenv import load_dotenv

#find .env file
load_dotenv()

#use api key in .env
API_KEY = os.getenv("WATCHMODE_API_KEY")

def get_trending_titles(page=1, genre_filter=None):
    #url for api to form get request
    url = f"https://api.watchmode.com/v1/list-titles/?apiKey={API_KEY}&types=movie&sort_by=popularity_desc&limit=20&page={page}"
    response = requests.get(url)

    #fail case: api call fails to get anything so return nothing
    if response.status_code != 200:
        return []

    #response from request in json
    data = response.json()
    #get title list
    titles = data.get("titles", [])
    movies = []


    #loop through each movie title in list
    for t in titles:
        #get id, use id in url to collect info about movie
        title_id = t.get("id")
        #use url to send request for more specific information on that title
        details_url = f"https://api.watchmode.com/v1/title/{title_id}/details/?apiKey={API_KEY}"
        details_response = requests.get(details_url)

        #error code if title url gets nothing in return
        if details_response.status_code != 200:
            continue

        #for each movie store response og poster and genre
        details = details_response.json()
        genres = details.get("genre_names", [])
        poster = details.get("poster")

        #checks genre filter to the genre of movie
        if genre_filter and genre_filter.lower() not in [g.lower() for g in genres]:
            continue

        #movies list with title, year, and poster returned
        movies.append({
            "title": t.get("title"),
            "year": t.get("year"),
            "poster": poster
        })

    return movies

def get_service_titles(page=1, genre_filter=None):
    url = f"https://api.watchmode.com/v1/list-titles/?apiKey={API_KEY}&types=movie&sort_by=popularity_desc&limit=40&page={page}"
    response = requests.get(url)

    if response.status_code != 200:
        return []
    
    
    #response from request in json
    data = response.json()
    #get title list
    titles = data.get("titles", [])
    movies = []


    #loop through each movie title in list
    for t in titles:
        #get id, use id in url to collect info about movie
        title_id = t.get("id")
        #use url to send request for more specific information on that title
        details_url = f"https://api.watchmode.com/v1/title/{title_id}/details/?apiKey={API_KEY}"
        details_response = requests.get(details_url)

        sources_url = f"https://api.watchmode.com/v1/title/{title_id}/sources/?apiKey={API_KEY}"

        #error code if title url gets nothing in return
        if details_response.status_code != 200:
            continue

        #for each movie store response og poster and genre
        details = details_response.json()
        genres = details.get("genre_names", [])
        poster = details.get("poster")

        #checks genre filter to the genre of movie
        if genre_filter and genre_filter.lower() not in [g.lower() for g in genres]:
            continue

        #movies list with title, year, and poster returned
        movies.append({
            "title": t.get("title"),
            "year": t.get("year"),
            "poster": poster
        })

    return movies