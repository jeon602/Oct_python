import requests  # 웹 페이지에 HTTP 요청을 보내기 위한 라이브러리
from bs4 import BeautifulSoup  # HTML과 XML 문서를 파싱하기 위한 라이브러리

# URL 설정
url = "https://lecoingolf.fr/"

# 요청할 때 User-Agent를 추가하여 브라우저처럼 보이게 설정 (사이트에서 크롤링을 차단할 수 있는 경우 대비)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

# URL에 GET 요청을 보냄 (웹 서버로부터 페이지를 가져옴)
response = requests.get(url, headers=headers)

# 응답 상태 코드가 200(성공)일 경우에만 다음 작업 진행
if response.status_code == 200:
    # HTML 텍스트 데이터를 BeautifulSoup 객체로 파싱하여 분석 준비
    soup = BeautifulSoup(response.text, 'html.parser')

    # <h2> 태그를 모두 찾음 (웹 페이지에서 제목이나 헤더일 가능성이 큼)
    titles = soup.find_all('h2')  # find_all은 지정한 태그를 모두 가져옴

    # 찾은 모든 <h2> 태그들에서 텍스트만 추출하여 출력
    for title in titles:
        print(title.get_text())  # get_text()는 태그 안의 순수 텍스트만 반환
else:
    # 상태 코드가 200이 아닐 경우 에러 메시지 출력
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

# import


