# telegram_bot  6228091502:AAGX9fMa3Np4bPCpub1QPLjqSd-GSZfe5W4
# ID  71046013
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '6228091502:AAGX9fMa3Np4bPCpub1QPLjqSd-GSZfe5W4'
TELEGRAM_CHAT_ID = '71046013'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    reporter = request.form['reporter']
    location = request.form['location']
    complaint = request.form['complaint']

    message = f'신고자: {reporter}\n위치: {location}\n불편내용: {complaint}'

    send_telegram_message(message)

    return '신고가 접수되었습니다. 감사합니다!'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print('텔레그램 메시지 전송 실패')

if __name__ == '__main__':
    app.run(port=5001)  # Use a different port, such as 5001
