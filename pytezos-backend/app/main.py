from flask import Flask, request, jsonify
from pytezos import pytezos
from flask_cors import CORS, cross_origin
from .config import config

pyt = pytezos.using(
    key=config["TEZOS_PRIVATE_KEY"],
    shell="https://edonet-tezos.giganode.io"
)
contract = pyt.contract(config["CONTRACT"])


app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route("/get/<string:username>")
def get(username):
    users = contract.storage()
    points = -1
    if username in users:
        points = users[username]
    rank = 1
    for user in users:
        if users[user] > points:
            rank += 1
    if points == -1:
        points = 0
    return {
        'points': points,
        'rank': rank
    }

@app.route("/update/<string:username>/<int:points>")
def update(username, points):
    contract.updatePoints(
        username=username,
        points=points
    ).operation_group.sign().inject()
    return '1'

@app.route("/create/<string:username>")
def create(username):
    contract.createUser(username).operation_group.sign().inject()
    return '1'
