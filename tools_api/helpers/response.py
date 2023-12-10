from flask import jsonify, make_response

def response_builder(*args):
    res = make_response(args)
    res.headers.add("Access-Control-Allow-Origin", "*")
    res.headers.add("Access-Control-Allow-Headers", "*")
    res.headers.add("Access-Control-Allow-Methods", "*")
    return res

def ok(data: any, message: str) -> any:
    res = {
        'message': message,
        'data': data,
    }
    return response_builder(jsonify(res), 200)


def success(message: str) -> any:
    res = {
        'message': message
    }
    return response_builder(jsonify(res), 201)


def bad_request(values: any) -> any:
    res = {
        'message': 'Validation errors in your request',
        'errors': values,
    }
    return response_builder(jsonify(res), 400)


def server_error() -> any:
    res = {
        'message': 'Something wrong!',
    }
    return response_builder(jsonify(res), 500)
