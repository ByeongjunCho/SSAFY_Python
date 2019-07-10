from flask import Flask, render_template
import random
app = Flask(__name__)  # 객체 생성

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/hi")
def hi():
    # return "<h1>용흠아 안녕</h1>"   # 주소/hi : "용흠아 안녕 출력"
    return render_template('hi.html')
# variable routing! 경로를 변수로 활용한다.
@app.route("/hi/<string:name>")
def hiyo(name):
    # return f"<h1>{name}야 안녕?</h1>"
    return render_template('hi2.html', namee=name)  # 들어오는 이름을 html에 넘겨줌    
# /lunch/사람이름
# menu = []

@app.route('/lunch/<string:name>')
def lunch(name):
    menu = ['코파컵 우승 못해', '월드컵 우승 못해', '넌 못지나간다']
    # return f'{name}야, {random.choice(menu)}!!!'
    return render_template('lunch.html', lunchmenu = random.choice(menu), namee = name)
    

# /cube/<숫자>
# 세제곱 결과를 보여주는 페이지!
@app.route('/cube/<int:number>')
def mutipl3(number):
    return f'<h1>{number}의 세제곱은 {number**3}입니다.</h1>'


# 로또!  /lotto
# 로또번호 6개를 추천해주는 페이지
@app.route('/lotto')
def lotto():
    numbers = random.sample(range(1,46), 6)
    return f"<h1>이번주 당첨번호는{str(sorted(numbers))}입니다</h1>"

if __name__ == '__main__':
    # python app.py 를 하면 아래의 코드 블록을 실행시킨다.
    app.run(debug=True)