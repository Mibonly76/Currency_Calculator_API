from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_currency_rate(currency_in="USD", currency_out="BGN"):
    request_url_check = f'https://v6.exchangerate-api.com/v6/{os.getenv("API_KEY")}/latest/all'
    currency_rates_check = requests.get(request_url_check).json()
    if (currency_in in currency_rates_check["conversion_rates"]
            and currency_out in currency_rates_check["conversion_rates"]):

        request_url = f'https://v6.exchangerate-api.com/v6/{os.getenv("API_KEY")}/latest/{currency_in}'
        currency_rates = requests.get(request_url).json()
        currency_rate = currency_rates["conversion_rates"][f"{currency_out}"]

        return currency_rate
    else:
        return 404


def convertor(current_rate, amount):
    result = amount * current_rate
    result = "{:.2f}".format(result)
    return result


if __name__ == "__main__":
    print('\n*** Enter the Currency Exchange Details ***\n')

    req_currency_in = input("\nPlease enter a currency from: ")
    req_currency_out = input("\nPlease enter a currency to: ")

    requested_currency_rate = get_currency_rate(req_currency_in, req_currency_out)

    print("\n")
    pprint(requested_currency_rate)
