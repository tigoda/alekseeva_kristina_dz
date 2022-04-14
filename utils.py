from requests import get, utils


def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    for el in content.split('<CharCode>')[1:]:
        a = (el.split('</Value>')[0])
        b = a.partition('<Value>')
        if currency in a:
            answer = f'{currency} :{b[-1]}'
            return answer
    return None
