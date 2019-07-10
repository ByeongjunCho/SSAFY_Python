from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
iu = Flask(__name__)
url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=iu"
iupage = requests.get(url).text
soup = BeautifulSoup(iupage, 'html.parser')

iu_age = soup.select('#people_info_z > div.cont_noline > div > dl > dt:nth-child(2)').text

# print(iu_age)
# @iu.route('/')
# def hi():
#     url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=iu"
#     iupage = requests.get(url).text
#     soup = BeautifulSoup(iupage, 'html_parser')
#     iu_age = soup.select_one('#people_info_z > div.cont_noline > div > dl > dd:nth-child(3) > span').text
#     return render_template('iu.html', )
# @iu.route('/hello/<string:name>')
# def hello(name):
#     return render_template('hi2.html', namee = name)



# if __name__ == "__main__":
#     iu.run(debug=True)