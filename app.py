from flask import Flask, render_template
from dotenv import load_dotenv
import os
from api_folder.api import get_trending_titles  

load_dotenv()  
app = Flask(__name__, template_folder='frontend')


#@app.route('/')
#def index():
#    movies = get_trending_titles()
#    return render_template('index.html', movies=movies)

@app.route('/')
def index():
    movies = get_trending_titles()
    for m in movies:
        print(m['poster'])
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
