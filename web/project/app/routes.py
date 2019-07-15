from .views.todo import TodoListView, TodoDetailView


setting_routes = [
    {"handler": TodoListView.as_view(), "uri": "/todo"},
    {"handler": TodoDetailView.as_view(), "uri": "/todo/<id:int>"},
]