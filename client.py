import datetime
import dateutil.relativedelta as rd
import pandas as pd
import requests
import re
from typing import List, Optional, Union


class KweClient:
    def __init__(self, api_key: str):

        self.api_key = api_key
        self.api_headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.api_key
        }

    def get_credit_ballance(self) -> str:
        response = requests.get('https://api.keywordseverywhere.com/v1/account/credits', headers=self.api_headers)
        return response.content.decode('utf-8')

    def get_countries(self) -> str:
        response = requests.get('https://api.keywordseverywhere.com/v1/countries', headers=self.api_headers)
        return response.content.decode('utf-8')

    def get_currencies(self) -> str:
        response = requests.get('https://api.keywordseverywhere.com/v1/currencies', headers=self.api_headers)
        return response.content.decode('utf-8')

    def get_keyword_data(self):
        pass
