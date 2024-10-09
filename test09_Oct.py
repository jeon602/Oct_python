import requests  # 웹 페이지에 접속하기 위한 모듈
from bs4 import BeautifulSoup  # HTML 데이터를 분석하기 위한 모듈

# 크롤링할 웹사이트 URL
url = "http://example.com"  # 예시 웹사이트

# 웹 페이지에 접속해서 HTML 코드 가져오기
response = requests.get(url)  # 웹사이트에 접속하고 데이터를 가져옴

# HTML 코드를 BeautifulSoup을 이용해 분석하기 쉽게 변환
soup = BeautifulSoup(response.text, 'html.parser')  # HTML 파싱

# 예시: <h1> 태그의 텍스트를 추출하기 (웹사이트의 제목 등을 추출할 수 있음)
title = soup.find('h1').get_text()  # <h1> 태그를 찾아서 그 안의 텍스트를 가져옴
print(title)  # 출력해서 확인



#chrome:version//
