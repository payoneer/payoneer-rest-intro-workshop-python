from flask import Flask, Response
from .data.seed import items

app = Flask("app",
            static_url_path='', 
            static_folder='web')


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route("/items")
def get_items():
    return Response(str(items), content_type="application/json")