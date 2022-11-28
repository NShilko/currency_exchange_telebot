import exeptions
import requests
import config
import texts
from fuzzywuzzy import fuzz


class GetExchange:
    @staticmethod
    def print_support_currency():
        text = '🚩 Список поддерживаемых валют: \n\n'
        for key, name in config.dic_currency_support.items():
            text += f'🔸 [ {key} ] {name} \n'
        return text

    @staticmethod
    def detect_currency(str_currency):
        detect_score = 60
        dic_key = False
        for key, name in config.dic_currency_names.items():
            for i in name:
                if fuzz.token_set_ratio(str_currency, i) >= detect_score:
                    dic_key = key
                    detect_score = fuzz.token_set_ratio(str_currency, i)

        return dic_key

    @staticmethod
    def get_currency_names(txt):
        wrong_currency = ''
        currency_amount = None
        data = txt.replace(' в ', ' ').split(' ')
        try:
            if len(data) != 3 and len(data) != 2:
                raise exeptions.ErrUserWrongInput('Wrong len of user input data')

            currency_from = GetExchange.detect_currency(data[0])
            if not currency_from:
                wrong_currency = data[0]
                raise exeptions.ErrWrongCurrency(f'Wrong currency_from : [ {wrong_currency} ]')

            currency_to = GetExchange.detect_currency(data[1])
            if not currency_to:
                wrong_currency = data[1]
                raise exeptions.ErrWrongCurrency(f'Wrong currency_to [ {wrong_currency} ]')

            if len(data) == 2:
                currency_amount = '1'
            else:
                currency_amount = data[2].replace(',', '.')
            if not currency_amount.replace('.', '').isdigit():
                raise exeptions.ErrWrongValue(f'User try to put [ {currency_amount} ] in to currency_amount')

            url = f'https://api.exchangerate.host/convert?from={currency_from}&to={currency_to}&amount={currency_amount}'
            response = requests.get(url)
            if response.json()['success']:
                value = response.json()['result']
                text = f'''💹 Успешная конвертация

🔸 из [ {currency_from} ] {config.dic_currency_support[currency_from]} 
🔹 в   [ {currency_to} ] {config.dic_currency_support[currency_to]}
♦ сумма: [ {currency_amount} ] 

✅ Результат: [ {value} ]'''

                return text
            else:
                raise exeptions.ErrNoResponse()

        except exeptions.ErrUserWrongInput:
            return texts.err_wrong_len
        except exeptions.ErrNoResponse:
            return texts.err_no_response
        except exeptions.ErrWrongCurrency:
            return texts.err_wrong_currency + f'[ {wrong_currency} ]'
        except exeptions.ErrWrongValue:
            return texts.err_wrong_value + f'[ {currency_amount} ]'
