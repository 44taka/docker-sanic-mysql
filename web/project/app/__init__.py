from sanic import Sanic
import sanic.exceptions as se

from tortoise import Tortoise
import tortoise.exceptions as te

from .routes import setting_routes
from .configs import local

from .handlers.sanic_error_handler import not_found, server_error
from .handlers.tortoise_error_handler import db_connection, configuration_error

app = Sanic()

# 環境別の設定ファイルを読み込み
app.config.from_object(local)

# エラーハンドリング設定
app.error_handler.add(se.NotFound, not_found)
app.error_handler.add(se.ServerError, server_error)
app.error_handler.add(te.DBConnectionError, db_connection)
app.error_handler.add(te.ConfigurationError, configuration_error)

# ルーティング設定
for route in setting_routes:
    app.add_route(**route)


# 起動タイミングでDBコネクションを開始
@app.listener('before_server_start')
async def setup_db(app, loop):
    await Tortoise.init(
        db_url="mysql://root:sanicpass@db:3306/sanic",
        modules={"models": ["app.models"]}
    )


# 落とすタイミングでDBコネクションを切断
@app.listener('after_server_stop')
async def close_db(app, loop):
    await Tortoise.close_connections()
