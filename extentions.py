import json
import requests

from config import currencies


class ConvertionException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно конвертировать одинаковые валюты {base}.')

        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = currencies[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать сумму {amount}.')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/16c81cac9ff597dd55aabc7f/pair/{quote_ticker}/{base_ticker}')
        total_base = (json.loads(r.content)['conversion_rate']) * amount

        return total_base