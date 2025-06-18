import os
import requests
from dotenv import load_dotenv

#find .env file
load_dotenv()

#use api key in .env
API_KEY = os.getenv("WATCHMODE_API_KEY")


def get_sources():
    url = f'https://api.watchmode.com/v1/sources/?apiKey={API_KEY}'
    response = requests.get(url)
    #fail case: api call fails to get anything so return nothing
    if response.status_code != 200:
        return []
    
    data = response.json()
    #array of dict source with name and id
    return [{"id": str(source["id"]), "name": source["name"]} for source in data]

    


#def get_trending_titles(page=1, genre_filter=None):
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

#def get_source_titles(page=1, source_filter=None):
    url = f"https://api.watchmode.com/v1/list-titles/?apiKey={API_KEY}&types=movie&sort_by=popularity_desc&limit=40&page={page}"
    response = requests.get(url)

    if response.status_code != 200:
        return []
    
    
    #response from request in json
    data = response.json()
    #get title list
    titles = data.get("titles", [])
    movies = []

###############################################################################################
    #loop through each movie title in list
    for t in titles:
        #get id, use id in url to collect info about movie
        title_id = t.get("id")



        sources_url = f"https://api.watchmode.com/v1/title/{title_id}/sources/?apiKey={API_KEY}"
        sources_response = requests.get(sources_url)

        #error code if title url gets nothing in return
        if sources_response.status_code != 200:
            continue

        sources = sources_response.json()
        #source_names = sources.get("name", [])
        source_names = [s.get("name") for s in sources]

        if source_filter:
            lower_source_names = [s.lower() for s in source_names if s]
            if not any(sel.lower() in lower_source_names for sel in source_filter):
                continue

        details_url = f"https://api.watchmode.com/v1/title/{title_id}/details/?apiKey={API_KEY}"
        details_response = requests.get(details_url)
        if details_response.status_code != 200:
            continue

        details = details_response.json()
        poster = details.get("poster")

        movies.append({
            "title": t.get("title"),
            "year": t.get("year"),
            "poster": poster
        })

    return movies

def get_source_titles_new(source_ids, page=1):
    url = f"https://api.watchmode.com/v1/list-titles/"
    #url = f'https://api.watchmode.com/v1/list-titles/?apiKey={API_KEY}&source_ids={source_ids}'
    params = {
        "apiKey": API_KEY,
        "types": "movie",  # or "tv_series" etc.
        "source_ids": ",".join(source_ids),  # IDs as string
        "sort_by": "popularity_desc",
        "page": page,
        "limit": 40  # or up to 250
    }

    #response = requests.get(url)
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return []

    data = response.json()
    titles = data.get("titles", [])
    movies = []

    #loop through each movie title in list
    for t in titles:
        #get id, use id in url to collect info about movie
        title_id = t.get("id")

        details_url = f"https://api.watchmode.com/v1/title/{title_id}/details/?apiKey={API_KEY}"
        details_response = requests.get(details_url)
        if details_response.status_code != 200:
            continue

        details = details_response.json()
        poster = details.get("poster")

        movies.append({
            "title": t.get("title"),
            "year": t.get("year"),
            "poster": poster
        })

    return movies


    #return data.get("titles", [])
