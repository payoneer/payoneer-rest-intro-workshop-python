from flask import Flask, Response, request

from .utils.json_decorator import as_json

from .data.seed import items
from .models.item import Item

app = Flask("app",
            static_url_path='', 
            static_folder='web')


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route("/items")
@as_json
def get_items():
    return items


@app.route('/items', methods=["POST"])
@as_json
def add_item():
    body = request.get_json()
    name = body["name"]
    item = Item(name);
    items.append(item)
    return item

@app.route('/items/<id>', methods=['PATCH'])
def update_item(id):
    item =  next(filter(lambda x: x.id == id, items), None)
    if(item is not None):
        body = request.get_json()
        name = body["name"]
        item.name = name;
        return "", 200
    return "", 400


@app.route('/items/<id>', methods=["DELETE"])
def delete_item(id):
    if(id in items):
        items.remove(id)
    else:
        return "", 400
    return "", 200  
