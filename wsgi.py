from app.puns import flask_app
from app import db

if __name__ == '__main__':
    flask_app.run(host="0.0.0.0", port="8080", debug=True)
