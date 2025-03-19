from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>ברוכים הבאים!</h1>
    <form action="/get_date" method="get">
        <button type="submit">לחץ לקבלת התאריך של היום</button>
    </form>
    '''

@app.route('/get_date')
def get_date():
    today = datetime.now().strftime("%Y-%m-%d")
    return f'<h1>התאריך של היום הוא: {today}</h1><br><a href="/">חזור</a>'

#if __name__ == '__main__':
#    app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)