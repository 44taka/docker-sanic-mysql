import fire
from base import BaseCli


class JisScrapingCli(BaseCli):

    # def __init__(self):
    #     super().__init__()
    #     self.bar_type = "jis"

    def scraping(self):
        self.driver.implicitly_wait(3)
        self.driver.get("https://jis.bar/index.html")
        self.bar_type = "jis"

        data = []
        for e in self.driver.find_elements_by_css_selector("div.table_counter"):
            branch_name = e.get_attribute("class").split(" ")[1]
            mens = e.find_element_by_css_selector("strong.mens").text
            ladys = e.find_element_by_css_selector("strong.ladys").text
            data.append(
                (0, self.bar_type, branch_name, mens, ladys, self.date, self.date, self.date)
            )
        cursor = self.conn.cursor()
        cursor.executemany("""
            INSERT INTO aiseki_bar_aggregate VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, data)
        self.conn.commit()

    # def  __del__(self):
    #     super().__del__()


if __name__ == "__main__":
    fire.Fire(JisScrapingCli)