from flask import Flask, render_template, jsonify, request
from api_folder.api import get_trending_titles, get_sources

app = Flask(__name__)

@app.route('/')
def index():
    #################################GENRE##############################################3
    #genre = request.args.get('genre')
    #movies = get_trending_titles(page=1, genre_filter=genre)
    #print out ever genre checked and returned movies
    #print(f"Genre: {genre} | Movies Returned: {movies}") 
    #return render_template('index.html', movies=movies, genre=genre)
########################################################################################
    sources = get_sources()
    #movies = get_trending_titles(page=1, sources_filter=sources)
    #return render_template('index.html', movies-movies, sources=sources)
    return render_template('index.html', sources=sources)


@app.route('/load_more')
def load_more():
    page = int(request.args.get('page', 1))
    genre = request.args.get('genre')
    movies = get_trending_titles(page=page, genre_filter=genre)
    return jsonify(movies)

#@app.route('/')


#fixed app run
if __name__ == '__main__':
    app.run(debug=True)