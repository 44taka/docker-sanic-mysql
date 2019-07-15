from sanic.response import json
from tortoise.exceptions import DoesNotExist
from .base import BaseView
from ..models import Todo
from ..utils import validates, error_codes, status_codes


class TodoListView(BaseView):
    """
    TodoListViewクラス
    """
    def __init__(self):
        super().__init__()

    async def get(self, request):
        """
        Todo一覧を取得
        :param request:リクエストオブジェクト
        :return:処理結果JSON
        """
        todos = await Todo.filter(is_finished=False)
        return json(self.response_ok({
            "todos": [{"id": todo.id, "body": todo.body} for todo in todos]
        }))

    async def post(self, request):
        """
        Todoを新規作成
        :param request:リクエストオブジェクト
        :return:処理結果JSON
        """
        # バリデーションチェック
        valid = validates.todo_valid(request.json)
        if len(valid) > 0:
            return json(
                self.response_ng(error_codes.E01_4001, valid),
                status_codes.HTTP_400
            )
        todo = await Todo.create(body=request.json["body"], is_finished=False)
        return json(self.response_ok(todo))


class TodoDetailView(BaseView):
    """
    TodoDetailクラス
    """
    def __init__(self):
        super().__init__()

    async def get(self, request, id):
        """
        Todo詳細を取得
        :param request: リクエストオブジェクト
        :param id: Todoを識別するユニークID
        :return: 処理結果JSON
        """
        try:
            todo = await Todo.get(id=id).filter(is_finished=False)
            return json(self.response_ok({
                "todo": [{"id": todo.id, "body": todo.body}]
            }))
        except DoesNotExist as e:
            return json(
                self.response_ng(error_codes.E01_0001, e),
                status_codes.HTTP_404
            )

    async def patch(self, request, id):
        """
        Todoを更新
        :param request: リクエストオブジェクト
        :param id: Todoを識別するユニークID
        :return: 処理結果JSON
        """
        try:
            # バリデーションチェック
            valid = validates.todo_valid(request.json)
            if len(valid) > 0:
                return json(
                    self.response_ng(error_codes.E01_4001, valid),
                    status_codes.HTTP_400
                )
            todo = await Todo.filter(id=id).update(body=request.json["body"])
            return json(self.response_ok(todo))
        except DoesNotExist as e:
            return json(
                self.response_ng(error_codes.E01_0001, e),
                status_codes.HTTP_404
            )

    async def delete(self, request, id):
        """
        Todoの削除（論理削除）
        :param request: リクエストオブジェクト
        :param id: Todoを識別するユニークID
        :return: 処理結果JSON
        """
        try:
            todo = await Todo.filter(id=id).update(is_finished=True)
            return json(self.response_ok(todo))
        except DoesNotExist as e:
            return json(
                self.response_ng(error_codes.E01_0001, e),
                status_codes.HTTP_404
            )
