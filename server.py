from flask import Flask, render_template, request
from waitress import serve
from currency_converter import currency_converter_in

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/request')
def currency_converter():
    from_currency = request.args.get('from_currency').upper()
    to_currency = request.args.get('to_currency').upper()
    amount = (request.args.get('amount'))
    result = currency_converter_in(from_currency, to_currency, amount)
    if result != 404:
        result, amount = currency_converter_in(from_currency, to_currency, amount)
        return render_template("convert.html",
                               from_currency=from_currency,
                               to_currency=to_currency,
                               amount=amount,
                               result=result)
    else:
        return render_template("error.html")


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
