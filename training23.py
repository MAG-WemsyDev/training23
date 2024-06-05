from flask import Flask, request, render_template
from werkzeug.urls import url_quote_plus as url_quote

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        returned_amount = float(request.form['returned_amount'])
        invested_amount = float(request.form['invested_amount'])
        gain = returned_amount - invested_amount
        roi = ((returned_amount - invested_amount) / invested_amount) * 100
        return render_template('result.html', gain=gain, roi=roi)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
