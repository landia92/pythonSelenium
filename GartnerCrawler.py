# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver
from selenium.webdriver.common.by import By
# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

# 크롬드라이버 실행
driver = webdriver.Chrome()

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://www.gartner.com/en/newsroom/archive')

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(10)

# 검색어 창을 찾아 search 변수에 저장 (By.XPATH 방식)
news_box = driver.find_element(By.XPATH, '//*[@id="gartnerinternalpage-141b1ef95b"]/div[2]/div/div/div/div/div/div[2]/section/div[1]/div[2]')
news = driver.find_element(By.CLASS_NAME, 'newsletter-item')
a = news_box.get_dom_attribute('href')
print(a)
# for elem in news_box:
#     href = elem.get_attribute('href')
#     print(href)