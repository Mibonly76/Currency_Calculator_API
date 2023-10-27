# from forex_python.converter import CurrencyRates
from api_reuester import get_currency_rate, convertor


def currency_converter_in(from_currency_input, to_currency_input, amount_input):
    from_currency_input = from_currency_input
    to_currency_input = to_currency_input
    currency_rate = get_currency_rate(from_currency_input, to_currency_input)
    if currency_rate != 404 and amount_input.isdigit():
        amount_input = int(amount_input)
        result = convertor(currency_rate, amount_input)

        return result, currency_rate
    else:
        return 404


if __name__ == "__main__":
    from_currency = input("Input currency: ")
    to_currency = input("Output currency: ")
    amount = (input("The Amount of currency: "))
    result_test = currency_converter_in(from_currency, to_currency, amount)
    print(result_test)
