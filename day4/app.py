# 0. flask 패키지 가져오기
from flask import Flask, render_template, request
import random
# 1. app 설정
app = Flask(__name__)

# 2. 요청 경로(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hello.html',namee=name)

@app.route('/lunch')
def lunch():
    menus = ['레드코코넛누들', '소불고기', '삼계탕', '치킨', '싸이버거', '치킨']
    pick = random.choice(menus)
    return render_template('lunch.html', menus = menus, pick = pick)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    # 사용자가 보낸 데이터를 받아와서
    text = request.args.get('say')
    nn = request.args.get('nn')
    tt = '일반 python데이터는 보내질까 궁금하다'
    print(request.args)
    # 템플릿에 넘겨준다.
    return render_template('pong.html', text=text, nn=nn, tt=tt)

@app.route('/random')
def random_():
    colors = ["red", "blue"]
    img = "2.png"
    return render_template('random.html', colors=colors, img=img)
    

@app.route('/random/result')
def random_result():
    tp1 = request.args.get('tp1')
    tp2 = request.args.get('tp2')
    tp3 = request.args.get('tp3')
    result = random.choice([tp1, tp2, tp3])
    
    
    return render_template('random_result.html', tp1=tp1, tp2=tp2, tp3=tp3, result=result)

@app.route('/result')
def result():
    mood = request.args.get('mood')
    weather = request.args.get('weather')
    playlist = {
        '외로움' : "https://www.youtube.com/watch?v=WfnEhxEcu-M"
    }
    music = random.choice(playlist)
    return render_template('result.html', mood=mood, weather=weather, music = music)

@app.route('/lotto')
def lotto():
    
    return render_template('lotto.html')

@app.route('/lotto_result')
def lotto_result():
    name = request.args.get('name')
    num = request.args.get('num')
    random.seed(num)
    numbers = random.sample(range(1,46), 6)

    return render_template('lotto_result.html', namee=name, numberss=numbers)
if __name__ == "__main__":
    app.run(debug=True)
