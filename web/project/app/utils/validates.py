from cerberus import Validator


def todo_valid(values):
    """
    TodoAPIのバリデーション
    :param values:バリデーションする値
    :return:
    """
    v = Validator({
        "body": {
            "type": "string",
            "required": True,
            "maxlength": 255
        }
    })

    return {} if v.validate(values) else v.errors
