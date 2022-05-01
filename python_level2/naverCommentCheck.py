import time

from selenium import webdriver
import requests


# 웹드라이버 생성
driver = webdriver.Chrome('/Users/nekot/Desktop/chromedriver')
driver.implicitly_wait(3)

#driver.find_element_by_xpath("//div[@class='tableType value']")[1]

# naver 로그인 접속
time.sleep(1)
driver.get('https://nid.naver.com/nidlogin.login')

# ID 입력
time.sleep(1.5)
driver.find_element_by_id('id').send_keys('nekote4')

# 비밀번호 입력
time.sleep(1.5)
driver.find_element_by_id('pw').send_keys('M@k3y0urb3dN')
# 로그인
time.sleep(1.5)
# driver.find_element_by_id('log.login').click()
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
# //<검색할 tag, * wildecard 사용가능>
# @id, @name 등등 사용가능
# 이후 /를 이용하여 하위 태그로 넘어갈 수있다.
'''



# 웹 페이지 가장 밑으로 스크롤
# scrollHeight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight 까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # scrollHeight 비교
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


# 이미지 다운로드
for elt in driver.find_elements_by_class_name('post-list__post.post'):
    # 'style'이라는 속성에서 이미지 url (이미지 주소) 추출
    style_string = elt.get_attribute('style')
    img_url = 'https://workey.codeit.kr' + \
        style_string.split(' url("')[1].split('")')[0]
    # 이미지 저장할 경로 정의
    img_path = '/Users/nekot/Desktop/my_images/' + img_url.split('/')[-1]
    # requests 패키지 써서 이미지 다운로드
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(img_path, 'wb+') as f:
            f.write(response.content)

'''
