from flask import Flask
import os
from os.path import join, dirname
from dotenv import load_dotenv
from pymongo import MongoClient
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient('mongodb+srv://salamull1005:jabbar1005@cluster0.t8jsdpg.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r', encoding='ISO-8859-1') as file:
        html_content = file.read()
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
