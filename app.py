from flask import Flask, render_template
import random
#文字エンコード
import urllib.parse

app = Flask(__name__)

results = [
    {"result": "大吉", "advice": "今日は何事もうまくいく！", "item": "黒のボールペン"},
    {"result": "吉", "advice": "外出するといいことあるかも！", "item": "ベージュの帽子"},
    {"result": "中吉", "advice": "部屋を掃除するといいことあるかも！！", "item": "青い靴"},
    {"result": "小吉", "advice": "小さな幸せを見逃さないで！", "item": "コーヒー"},
    {"result": "凶", "advice": "持ち物を無くすかも！", "item": "キーホルダー"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/omikuji')
def omikuji():
    choice = random.choice(results)
    share_text = f"今日の運勢は {choice['result']}!アドバイス: {choice['advice']}(ラッキーアイテム: {choice['item']}) #おみくじ"
    #エンコードを追加
    encoded_text = urllib.parse.quote(share_text)
    
    x_url = f"https://x.com/intent/post?text={share_text}"
    return render_template('result.html', choice=choice, x_url=x_url)

if __name__ == '__main__':
    app.run(debug=True)