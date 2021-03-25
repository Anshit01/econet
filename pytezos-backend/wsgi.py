from app.main import app
from app.config import config

if __name__ == "__main__":
    debug = False
    if 'DEBUG' in config and config['DEBUG']:
        debug = True
    app.run(debug=debug)
