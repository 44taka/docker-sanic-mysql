import MySQLdb
from datetime import datetime
from pytz import timezone

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BaseCli:
    def __init__(self):
        # データベースの接続開始
        self.conn = MySQLdb.connect(
            host="db",
            db="sanic",
            user="root",
            passwd="sanicpass",
            charset="utf8"
        )
        # seleniumのドライバー設定
        self.driver = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME
        )
        # 現在日時
        self.date = datetime.now(timezone('Asia/Tokyo')).strftime('%Y-%m-%d %H:%M:%S')

    def __del__(self):
        # データベースの接続終了
        self.conn.close()
        # seleniumの終了
        self.driver.quit()