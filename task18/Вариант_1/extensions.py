import json
import requests
from config import *


class ConvertionException(Exception):
    pass


class CryptoConverter :
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(
                f'Нельзя перевести одинаковые валюты {base}.')

        try:
            froms = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не смог обработать валюту {quote}')

        try:
            to = keys[base]
        except KeyError:
            raise ConvertionException(f'Не смог обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не смог обработать количество {amount}')

        url = f"https://api.apilayer.com/currency_data/convert?to={to}&from={froms}&amount={amount}"

        headers = {
            "apikey": "TdEV3LF2HSDBO7kuZ97ypdZd1B2YwSLO"
        }

        r = requests.get(url=url, headers=headers)

        total_base = json.loads(r.content)["result"]

        return total_base