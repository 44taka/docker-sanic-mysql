from sanic.response import json
from ..utils import status_codes, error_codes


async def not_found(request, exception):
    """
    NotFound時のエラーハンドリング
    :param request: リクエストオブジェクト
    :param exception: 例外オブジェクト
    :return: JSONパラメータ
    """
    return json({
        "status": "NG",
        "code": error_codes.E00_0001,
        "message": error_codes.codes[error_codes.E00_0001],
        "result": exception
    }, status_codes.HTTP_404)


async def server_error(request, exception):
    """
    サーバエラー発生時のエラーハンドリング
    :param request: リクエストオブジェクト
    :param exception: 例外オブジェクト
    :return: JSONパラメータ
    """
    return json({
        "status": "NG",
        "code": error_codes.E00_0002,
        "message": error_codes.codes[error_codes.E00_0002],
        "result": exception
    }, status_codes.HTTP_500)



