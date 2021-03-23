from hashlib import sha256
import uuid

def hash(password):
    return sha256(password.encode()).hexdigest()

def generateUUID():
    return uuid.uuid4()