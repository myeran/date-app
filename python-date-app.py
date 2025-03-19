from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_date')
def get_date():
    # קבלת התאריך הנוכחי (לפי שעון ישראל)
    israel_tz = pytz.timezone('Asia/Jerusalem')
    current_date = datetime.now(israel_tz).strftime('%d/%m/%Y %H:%M:%S')
    return {'date': current_date}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
