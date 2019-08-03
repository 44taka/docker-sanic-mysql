from .base import BaseJinjaView


class GraphView(BaseJinjaView):
    """

    """
    async def get(self, request):

        return self.render({
            "Player": "ロナウド",
            "Category": "サッカー",
        })
