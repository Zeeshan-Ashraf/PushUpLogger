import json
import logging
from http import HTTPStatus

from flask import Flask, Response, jsonify, request

from database import initDb
from model.user import User
from service.health import Health
from service.pushUpLogService import PushUpLogService
from service.userService import UserService

app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@app.route("/")
def helloWorld():
    data = Health().helloWorld()
    return jsonify(data)


@app.route("/health")
def health():
    return Response(str(Health().healthCheck()), status=HTTPStatus.OK)


@app.route("/user/<int:id>", methods=['GET'])
def getUser(id: int):
    try:
        data: User = UserService().getUser(id)
        return Response(response=json.dumps(data.__dict__), status=200, mimetype='application/json')
        # we can also use: return jsonify(data)  p.s: jsonify returns Response object & directly converts obj to json
    except ValueError:
        return Response(response="User not found", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return Response(e.__repr__(), status=HTTPStatus.EXPECTATION_FAILED)


@app.route("/user", methods=['POST'])
def setUser():
    try:
        name, email = request.get_json()['name'], request.get_json()['email']
        logger.info(name + " " + email)
        UserService().save(User(name=name, email=email))
        return Response("Insert Ok", status=HTTPStatus.OK)
    except Exception as E:
        return Response(E.__repr__(), status=HTTPStatus.EXPECTATION_FAILED)


@app.route("/user", methods=['GET'])
def getAllUsers():
    try:
        pageNo: int = int(request.args.get('pageNo')) if request.args.get('pageNo') else None
        pageSize: int = int(request.args.get('pageSize')) if request.args.get('pageSize') else None
        users: User
        if pageNo:
            users: User = UserService().allUserPaginated(pageNo, pageSize)
        else:
            users: User = UserService().getAllUsers()
        return jsonify(users)
    except Exception as E:
        return Response(E.__repr__(), status=HTTPStatus.EXPECTATION_FAILED)


@app.route("/user/<int:id>", methods=['DELETE'])
def deleteUser(id: int):
    try:
        UserService().deleteUser(id)
        return Response(response='Deleted Success', status=HTTPStatus.OK)
    except Exception as E:
        return Response(E.__repr__(), status=HTTPStatus.EXPECTATION_FAILED)


@app.route("/user/search", methods=['GET'])
def searchUser():
    like: str = request.args.get('like')
    minId: str = request.args.get('minId')
    try:
        users = UserService().searchUser(int(minId), like)
        return jsonify(users)
    except ValueError:
        return Response("No Users found", status=HTTPStatus.NOT_FOUND)
    except Exception as E:
        return Response(E.__repr__(), status=HTTPStatus.EXPECTATION_FAILED)


@app.route("/user/raw-query", methods=['GET'])
def rawUserQuery():
    queryString: str = request.get_json()['query']
    try:
        results = UserService().rawUserQuery(queryString)
        return jsonify(results)
    except ValueError:
        return Response("No Results found", status=HTTPStatus.NOT_FOUND)
    except Exception as E:
        return Response(E.__repr__(), status=HTTPStatus.EXPECTATION_FAILED)


@app.route("/pushup", methods=['GET'])
def getAllPushUp():
    try:
        data = PushUpLogService().getAll()
        return jsonify(data)
        # we can also use: return jsonify(data)  p.s: jsonify returns Response object & directly converts obj to json
    except ValueError:
        return Response(response="User not found", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return Response(e.__repr__(), status=HTTPStatus.EXPECTATION_FAILED)


@app.route("/user/<int:id>/pushup", methods=['POST'])
def setUserPushUp(id: int):
    try:
        count, comment = int(request.get_json()['pushUpCount']), request.get_json()['comment']
        logger.info("request recieved at /user/<int:id>/pushup count=" + str(count) + " comment=" + comment)
        PushUpLogService().save(id, count, comment)
        return Response("Insert Ok", status=HTTPStatus.OK)
    except Exception as E:
        return Response(E.__repr__(), status=HTTPStatus.EXPECTATION_FAILED)


if __name__ == "__main__":
    initDb.createDb()
    app.run(debug=True)
