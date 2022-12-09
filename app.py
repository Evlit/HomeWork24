# Домашка 24
from flask import Flask, request, jsonify, Response
from utils import check_param, build_query

app = Flask(__name__)


@app.route("/perform_query", methods=['POST'])
def perform_query() -> str | Response:
    if request.json:
        param: dict = request.json
    else:
        return Response("Нет входящего запроса", status=400)

    if not check_param(param):
        return Response("Ошибка в параметрах запроса или нет файла", status=400)

# Переменные ниже определил так для обхода ошибок типизации.
# Их валидность проверяется функцией выше и значение 'none' получено быть не может
    cmd1: str = param.get('cmd1', 'none')
    value1: str = param.get('value1', 'none')
    cmd2: str = param.get('cmd2', 'none')
    value2: str = param.get('value2', 'none')
    file_name: str = param.get('file_name', 'none')

    result = None
    result = build_query(cmd1, value1, file_name, result)
    result = build_query(cmd2, value2, file_name, result)

    return jsonify(result)


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
