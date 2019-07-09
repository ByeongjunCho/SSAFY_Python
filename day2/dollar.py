import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'

response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")

dollar = soup.select_one('#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_bx > div.rate_spot._rate_spot > div.rate_tlt > h3 > a > span.spt_con.dw > strong').text

# url 입력
url = 'https://finance.naver.com/marketindex//exchangeList.nhn'  # url 요청
# 2. 파이썬이 찾기 편한 형식으로 문서를 변경한다.
response = requests.get(url).text

# 3. HTML 문서로 바꾸기
soup = BeautifulSoup(response, 'html.parser')

# 4. 원하는 내용을 선택 메서드로 찾기
# table = soup.select_one('body > div > table > tbody').text
table = soup.select('body > div > table > tbody > tr')
dollar = soup.select_one('body > div > table > tbody > tr:nth-child(1) > td.sale').text
eur = soup.select_one('body > div > table > tbody > tr:nth-child(2) > td.sale').text
body = soup.select('body > div > table > tbody > tr')

# for tr in table:
#     print(tr.select_one('td.sale').text)


# print(table)
# print(len(table))