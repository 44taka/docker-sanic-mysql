from sanic.views import HTTPMethodView
from ..utils import error_codes


class BaseView(HTTPMethodView):
    """
    BaseViesクラス（基幹クラス）
    """
    def __init__(self):
        pass

    def response_ok(self, data=[]):
        """
        処理成功時のJSONを取得
        :param data: データ配列
        :return: JSONパラメータ
        """
        return {
            "status": "OK",
            "result": data
        }

    def response_ng(self, error_cd, result):
        """
        エラー発生時のJSONを取得
        :param error_cd: エラーコード
        :param result: 結果配列
        :return: JSONパラメータ
        """
        return {
            "status": "NG",
            "code": error_cd,
            "message": error_codes.codes[error_cd],
            "result": result
        }
