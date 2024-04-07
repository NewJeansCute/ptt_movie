from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
title_list = []
content_list = []

def add_items(source: list[any], target_list: list[any]) -> None:
    for s in source:
        target_list.append(s.text)

try:
    # 文章標題
    # 最新頁
    driver.get(f"https://www.ptt.cc/bbs/movie/index.html")

    titles = driver.find_elements(By.CSS_SELECTOR, ".title a")
    add_items(titles, title_list)

    # 往後九頁
    for page_num in range(10069, 10078):
        driver.get(f"https://www.ptt.cc/bbs/movie/index{page_num}.html")

        titles = driver.find_elements(By.CSS_SELECTOR, ".title a")
        add_items(titles, title_list)

    # 文章內容
    driver.get("https://www.ptt.cc/bbs/movie/M.1712460428.A.8DA.html")
    main_content = driver.find_element(By.CSS_SELECTOR, "#main-container #main-content")
    content_list.append(main_content.text)

finally:
    driver.quit()