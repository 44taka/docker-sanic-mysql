from .views.todo import TodoListView, TodoDetailView
from .views.aiseki_bar import AisekiBarAggregateView
from .views.graph import GraphView

setting_routes = [
    {"handler": TodoListView.as_view(), "uri": "/todo", "version": 1},
    {"handler": TodoDetailView.as_view(), "uri": "/todo/<id:int>", "version": 1},
    {"handler": AisekiBarAggregateView.as_view(), "uri": "/aiseki/aggregate", "version": 1},
    {"handler": GraphView.as_view(), "uri": "/jinja"},
]