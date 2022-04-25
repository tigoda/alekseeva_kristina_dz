import re


def email_parse(email_address):
    email_address_dict = dict()
    pattern = re.compile(r'(\w+)@([a-zA-Z]+\.[a-zA-Z]+)')
    result = pattern.search(email_address)
    try:
        email_address_dict['username'] = result.group(1)
        email_address_dict['domain'] = result.group(2)
        return email_address_dict
    except:
        raise ValueError(f'ValueError: wrong email: {email_address}')


print(email_parse('someone@geekbr ns.ru'))
