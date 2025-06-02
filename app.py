from flask import Flask, render_template
from dotenv import load_dotenv
import os
from api_folder.api import get_trending_titles  # from your API logic

load_dotenv()  # Load environment variables from .env

#app = Flask(__name__)
app = Flask(__name__, template_folder='frontend')


@app.route('/')
def index():
    movies = get_trending_titles()
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
