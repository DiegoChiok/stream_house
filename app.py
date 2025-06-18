from flask import Flask, render_template, jsonify, request
from api_folder.api import get_trending_titles, get_sources, get_source_titles_new

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
    selected_sources = request.args.getlist('sources')  
    #movies = get_source_titles(page=1, source_filter=selected_sources)  
    movies = get_source_titles_new(source_ids=selected_sources, page=1)
    return render_template('index.html', movies=movies, sources=sources, selected_sources=selected_sources)


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




    #<form method="get" action="/">
    #    <label for="source">Filter by Streaming Availability:</label><br>
    #    {% for source in sources %}
    #        <input type="checkbox" name="sources" value="{{ source.name }}"
    #            {% if source.name in selected_sources %}checked{% endif %}>
    #        {{ source.name }}<br>
    #    {% endfor %}
    #    <button type="submit">Apply</button>
    #</form>