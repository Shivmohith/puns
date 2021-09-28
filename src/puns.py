from flask import Flask, request, Response
import db

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Punsters!</p>"


@app.route("/puns", methods=['GET', 'POST'])
def puns():
    try:
        if request.method == 'POST':
            body = request.json

            print(body)
            db.add_pun(pun=body['pun'])
            return Response(status=201)

        else:
            row = db.get_random_pun()
            print(row)

            resp = Response(status=200)
            resp.set_data(row[0])
            return resp
    except Exception as error:
        resp = Response(status=500)
        resp.set_data(str(error))
        return resp


if __name__ == "__main__":
    db.connect()
    app.run('localhost', '3030')
