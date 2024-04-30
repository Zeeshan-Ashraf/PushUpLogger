from http import HTTPStatus

from flask import Flask, Response, jsonify

from controller import controller
from database import mysqlSession
from database.userRepository import UserRepository

app = Flask(__name__)


@app.route("/")
def helloWorld():
    data = controller.helloWorld()
    return jsonify(data)


@app.route("/health")
def health():
    return Response("health check ok", status=HTTPStatus.OK)


@app.route("/user")
def user():
    try:
        mysqlSession.add(UserRepository(name="Zeeshan"))
        mysqlSession.commit()
        return Response("user added ok", status=HTTPStatus.OK)
    except Exception as E:
        return Response(E.__repr__(), status=HTTPStatus.OK)


if __name__ == "__main__":
    app.run()
