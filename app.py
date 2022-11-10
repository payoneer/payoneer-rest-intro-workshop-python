from flask import Flask, Response
from flask_cors import CORS
from .data.seed import items

app = Flask("app",
            static_url_path='', 
            static_folder='web')
CORS(app)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route("/items")
def get_items():
    return Response(str(items), content_type="application/json")