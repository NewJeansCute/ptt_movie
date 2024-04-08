from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
# 設定等待網頁載入的時間，如果提早載入完成，會提早結束等待，如果時間不夠，讀到的網頁內容會有殘缺
driver.implicitly_wait(10)

href_list: list[str] = []
article_list: list[dict] = []

try:
    driver.get(f"https://www.ptt.cc/bbs/movie/M.1712543103.A.1DF.html")

    soup = BeautifulSoup(driver.page_source, "lxml")
    # pushes = soup.select(".push")

    sign = soup.find_all("span", class_="h1 push-tag")
    print(sign)
    # print(sign)
    
    # for push in pushes:
        # print(push.get_text())
        # sign = push.find_all("span", {"class": "h1 push-tag"})
        # print(sign)
        # push_userid = push.select("span.f3.h1.push-userid").get_text()
        # push_content = push.select("span.f3.push-content").get_text()
        # push_time = push.select("span.push-ipdatetime").get_text()

        # print(sign)
        # print(push_userid)
        # print(push_content)
        # print(push_time)
        # break
        

    # print(soup.find_all("span.h1 push-tag"))
    # for push in pushes:
    #     print(push.)
    
    # # 抓取文章連結
    # # 最新頁
    # driver.get(f"https://www.ptt.cc/bbs/movie/index.html")

    # for a in driver.find_elements(By.CSS_SELECTOR, ".title a"):
    #     href_list.append(a.get_attribute("href"))

    # # 往後九頁
    # for page_num in range(10070, 10079):
    #     driver.get(f"https://www.ptt.cc/bbs/movie/index{page_num}.html")

    #     for a in driver.find_elements(By.CSS_SELECTOR, ".title a"):
    #         href_list.append(a.get_attribute("href"))

    # # 抓取文章標題、內容、回文
    # article_id: int = 1

    # for href in href_list:
    #     driver.get(href)

    #     push_objs = {}
    #     pushes = driver.find_element(By.CSS_SELECTOR, ".push").text
    #     for push in pushes:
            
    #     article_list.append(
    #         {
    #             "article_id": article_id,
    #             "title": driver.find_element(By.CSS_SELECTOR, "title").text,
    #             "content": driver.find_element(By.CSS_SELECTOR, "#main-content").text,
    #             "pushes": []
    #         }
    #     )

        
            

    #     article_id += 1

    # # 回文

    # for push in pushes:
        # push_list.append(push.text)

finally:
    driver.quit()