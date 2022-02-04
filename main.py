import argparse
# import requests
import time
import json
from xml.sax.xmlreader import Locator


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from collections import defaultdict
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


parser = argparse.ArgumentParser()
parser.add_argument("--city", help='this is citycode', type=str)
args = parser.parse_args()
# print(f"第 1 個引數：{args.arg1:^10}，type={type(args.arg1)}")

# 暫存 city
cityData = {}

# 輸出 dict
exportData = {}

# opts = Options()
opts = webdriver.ChromeOptions()
# opts.add_argument('--headless')  # 無頭chrome
opts.add_argument('--disable-gpu')
browser = webdriver.Chrome(
    executable_path=ChromeDriverManager().install(), chrome_options=opts)

# browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())


# 抓取縣市
url = "https://www.cwb.gov.tw/V8/C/"

browser.get(url)
# 檢查條件
locator = (By.XPATH, '//*[@id="megacity"]/section[1]/label/select')
try:
    WebDriverWait(browser, 10, 0.5).until(
        EC.presence_of_element_located(locator))  # 最長等待10秒，每0.5秒檢查一次條件是否成立
finally:
    # print(browser.title)

    # 獲得頁面資訊
    pageSource = browser.page_source
    # print(pageSource)

    # title = browser.title
    # 關閉瀏覽器視窗
    # browser.close()

soup = BeautifulSoup(pageSource, 'lxml')
cidSelects = soup.find("select", {'name':'CID'}).select("option")

# print(cidSelect)

for select in cidSelects:
    if select['value'] == 'overall' or select['value'] == '':
        continue
    cid = select['value']
    cname = select.text
    cityData.update({cid:cname})

# print(cityData)
# browser.close()
# exit()


# ---------------------------------------------------
# 處理命令行輸入的城市參數
cityCode = "63"
city = "臺北市"

def cityToCode(city):
    code = ""
    # print(cityData)
    for key in cityData:
        if city == cityData[str(key)]:
            city = cityData[str(key)]
            code = key
            break
    return [city, code]

if args.city:
    cc = cityToCode(args.city)
    city, cityCode = cc

if cityCode == "":
    print('對應不到城市')
    browser.close()
    exit()

time.sleep(1)

# ---------------------------------------------------
# 抓取今日
# 定位到需要懸停的元素,然後執行滑鼠懸停操作（例：對設定標籤進行懸停）
# move_to_element_location = browser.find_element_by_css_selector("#menu-list-li > li.dropdown.mega-menu-fullwidth.open")
# move_to_element_location = browser.find_element("#menu-list-li > li.dropdown.mega-menu-fullwidth.open")
move_to_element_location = browser.find_element_by_xpath('//*[@id="menu-list-li"]/li[3]/a')
ActionChains(browser).move_to_element(move_to_element_location).perform()
time.sleep(1)  # 睡兩秒，看一下效果

# 使用Select類操作下拉框
citySelect = Select(browser.find_element_by_xpath(
    '//*[@id="megacity"]/section[1]/label/select'))
citySelect.select_by_value(cityCode)
# time.sleep(1)

# 滑鼠懸浮後點擊高階搜尋
browser.find_element_by_css_selector(
    "#megacity > section:nth-child(2) > button").click()


locator = (By.XPATH, '/html/body/div[2]/main/div/div[1]/div[3]/div[2]/ul')
try:
    WebDriverWait(browser, 10, 0.5).until(
        EC.presence_of_element_located(locator))  # 最長等待10秒，每0.5秒檢查一次條件是否成立
finally:
    # print(browser.title)

    # 獲得頁面資訊
    pageSource = browser.page_source
    # print(pageSource)

    # title = browser.title
    # 關閉瀏覽器視窗
    # browser.close()

# 建立爬取對象
soup = BeautifulSoup(pageSource, 'lxml')
soup.select("body > div.wrapper > main > div > div:nth-child(1) > div.d-xl-none.d-block > div.banner_wrap > ul > li:nth-child(1)")
todayData = {}
todayData['img'] = "https://www.cwb.gov.tw/"+soup.find("img").get("src", "")
todayData['tem'] = soup.find("span", class_="tem-C").text
exportData.update({"today": todayData})


# ---------------------------------------------------

# 抓取一週預報
url = "https://www.cwb.gov.tw/V8/C/W/week.html"
browser.get(url)
# 檢查條件
locator = (By.XPATH, '//*[@id="table1"]/tbody[2]')

try:
    WebDriverWait(browser, 10, 0.5).until(
        EC.presence_of_element_located(locator))  # 最長等待10秒，每0.5秒檢查一次條件是否成立
finally:
    # print(browser.title)

    # 獲得頁面資訊
    pageSource = browser.page_source
    # print(pageSource)

    # title = browser.title
    # 關閉瀏覽器視窗
    browser.close()


# 建立爬取對象
soup = BeautifulSoup(pageSource, 'lxml')

# 輸出排版後的 HTML 程式碼
# print(soup.prettify())

# 根據 city code 抓取 tbody
cityBody = soup.find(id="C"+cityCode).parent.parent
# print(cityBody)

# 分別抓取白天晚上區塊
daytime = cityBody.find(class_='day')
nighttime = cityBody.find(class_='day')
# print(daytime)
# print(nighttime)

weekData = []
for i in range(1, 7):
    data = {}
    data["date"] = soup.find("th", id="day" + str(i)).find("span").text
    data["img"] = "https://www.cwb.gov.tw/"+daytime.find("td", headers='day' + str(i)).find("img").get("src", "")
    data["tem"] = daytime.find(
        "td", headers='day' + str(i)).find("span", class_="tem-C").text
    weekData.append(data)
# print(wData)

exportData.update({"week": weekData})
exportData.update({"city": cityData[cityCode]})
exportData.update({"city_code": cityCode})
print(json.dumps(exportData))


