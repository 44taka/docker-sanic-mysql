from sanic.response import json
from ..utils import status_codes, error_codes


async def db_connection(request, exception):
    """
    DB接続エラー時のエラーハンドリング
    :param request: リクエストオブジェクト
    :param exception: 例外オブジェクト
    :return: JSONパラメータ
    """
    return json({
        "status": "NG",
        "code": error_codes.E00_0003,
        "message": error_codes.codes[error_codes.E00_0003],
        "result": exception
    }, status_codes.HTTP_500)


async def configuration_error(request, exception):
    """
    DB設定エラー時のエラーハンドリング
    :param request: リクエストオブジェクト
    :param exception: 例外オブジェクト
    :return: JSONパラメータ
    """
    return json({
        "status": "NG",
        "code": error_codes.E00_0004,
        "message": error_codes.codes[error_codes.E00_0004],
        "result": exception
    }, status_codes.HTTP_500)
