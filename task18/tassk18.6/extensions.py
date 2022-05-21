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
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не смог обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не смог обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не смог обработать количество {amount}')

        r = requests.get(f'https://api.coingate.com/v2/rates/merchant/{base_ticker}/{quote_ticker}')

        total_base = float(r.text) * amount


        return total_base