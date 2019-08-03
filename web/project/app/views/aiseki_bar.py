from sanic.response import json
from tortoise.exceptions import DoesNotExist
from .base import BaseView
from ..models import Aiseki_bar_aggregate
from ..utils import validates, error_codes, status_codes


class AisekiBarAggregateView(BaseView):
    """
    AisekiBarAggregateViewクラス
    """
    def __init__(self):
        super().__init__()

    async def get(self, request):
        """
        Todo一覧を取得
        :param request:リクエストオブジェクト
        :return:処理結果JSON
        """
        aggregate = await Aiseki_bar_aggregate\
            .filter(
                bar_type="jis",
                branch_name__in=["umeda"]
            )\
            .order_by("branch_name", "aggregated_at")

        data = {}
        labels = []
        for agg in aggregate:
            # 集計日時
            labels.append(agg.aggregated_at)
            if agg.branch_name not in data:
                data[agg.branch_name] = {}
            if agg.sex not in data[agg.branch_name]:
                data[agg.branch_name][agg.sex] = {"x": [], "y": []}

            data[agg.branch_name][agg.sex]["x"].append(agg.aggregated_at)
            data[agg.branch_name][agg.sex]["y"].append(agg.visitors)

        print(list(set(labels)))

        """
        resp = {
            labels: ["22:55", "23:00", "23:05"],
            data: [
                {
                    branch_nm: "umeda_mens",
                    visitors: [10, 20, 30],
                },
                {
                    branch_nm: "umeda_ladys",
                    visitors: [20, 40, 10],
                },
            ]
        }
        """
        return json(self.response_ok({
            "labels": ["22:55", "23:00", "23:05"],
            "data": [
                {
                    "branch_nm": "umeda_mens",
                    "visitors": [10, 20, 30],
                },
                {
                    "branch_nm": "umeda_ladys",
                    "visitors": [20, 40, 10],
                },
            ]
        }))

        # return json(self.response_ok(data))