from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ptt"]
movies = db["movies"]

driver = webdriver.Chrome()
# 設定等待網頁載入的時間，如果提早載入完成，會提早結束等待，如果時間不夠，讀到的網頁內容會有殘缺
driver.implicitly_wait(10)

href_list: list[str] = []
article_list: list[dict] = []

try:
    # 抓取文章連結
    # 最新頁
    driver.get(f"https://www.ptt.cc/bbs/movie/index.html")

    for a in driver.find_elements(By.CSS_SELECTOR, ".title a"):
        href_list.append(a.get_attribute("href"))

    # 往後九頁
    for page in range(9):
        driver.find_element(By.XPATH, "//a[@class='btn wide' and contains(text(), '‹ 上頁')]").click()

        for a in driver.find_elements(By.CSS_SELECTOR, ".title a"):
            href_list.append(a.get_attribute("href"))

    for page_num in range(10072, 10081):
        driver.get(f"https://www.ptt.cc/bbs/movie/index{page_num}.html")

        for a in driver.find_elements(By.CSS_SELECTOR, ".title a"):
            href_list.append(a.get_attribute("href"))

    # 抓取文章標題、內容、回文
    article_id: int = 1

    for href in href_list:
        driver.get(href)
        soup = BeautifulSoup(driver.page_source, "lxml")

        title = soup.select("span.article-meta-value")[2].text.strip()

        main_content = soup.find("div", id="main-content").text
        article = main_content.split("--")[0]
        lines = article.split("\n")
        content = "\n".join(lines[1:])

        # 回文
        push_objs: list[dict] = []
        pushes = soup.select("div.push")

        for push in pushes:
            spans = push.contents

            push_tag = spans[0].text.strip()
            push_userid = spans[1].text.strip()
            push_content = spans[2].text.strip()
            push_time = datetime.strptime(f"2024/{spans[3].text.strip()}", "%Y/%m/%d %H:%M")

            push_objs.append(
                {
                    "push_tag": push_tag,
                    "push_userid": push_userid,
                    "push_content": push_content,
                    "push_time": push_time
                }
            )

        article_list.append(
            {
                "article_id": article_id,
                "title": title,
                "content": content,
                "pushes": push_objs
            }
        )

        article_id += 1

    movies.insert_many(article_list)

finally:
    driver.quit()