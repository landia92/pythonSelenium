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

# 페이지가 완전히 로딩되도록 10초동안 기다림
time.sleep(5)

# 검색어 창을 찾아 search 변수에 저장 (By.XPATH 방식)
news_box = driver.find_element(By.XPATH, '//*[@id="gartnerinternalpage-141b1ef95b"]/div[2]/div/div/div/div/div/div[2]/section/div[1]/div[2]')
#news = driver.find_element(By.CLASS_NAME, 'newsletter-item')
i=1
for i in range(1, 13):
    #뉴스 요소를 클래스 이름으로 찾기
    # 각 뉴스 요소에서 href 속성을 가져와 출력
    news_items = news_box.find_elements(By.XPATH,
                                        '//*[@id="gartnerinternalpage-141b1ef95b"]/div[2]/div/div/div/div/div/div[2]/section/div[1]/div[2]/div[' + str(i) + ']/a')
    for i in news_items :
        href = i.get_attribute('href')
        print(href)
    # print(href)



#크롬드라이버 종료
driver.quit()
