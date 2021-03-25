from hashlib import sha256
import uuid
from pytezos import pytezos

from econet.config import config


def getUserPointsAndRank(username):
    try:
        pyt = pytezos.using(
            key=config["TEZOS_PRIVATE_KEY"],
            shell="https://edonet-tezos.giganode.io"
        )
        contract = pyt.contract(config["CONTRACT"])

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
        return points, rank
    except:
        print("Tezos error")
    return 0, 100

def updateUserPoints(username, points):
    try:
        pyt = pytezos.using(
            key=config["TEZOS_PRIVATE_KEY"],
            shell="https://edonet-tezos.giganode.io"
        )
        contract = pyt.contract(config["CONTRACT"])

        contract.updatePoints(
            username=username,
            points=points
        ).operation_group.sign().inject()
    except:
        print("Tezos error")

def createUser(username):
    try:
        pyt = pytezos.using(
            key=config["TEZOS_PRIVATE_KEY"],
            shell="https://edonet-tezos.giganode.io"
        )
        contract = pyt.contract(config["CONTRACT"])
        contract.createUser(username).operation_group.sign().inject()
    except:
        print("error in creating user in blockchain. probably it already exists.")

def hash(password):
    return sha256(password.encode()).hexdigest()

def generateUUID():
    return uuid.uuid4()

