import random

urls = {}
symbols = 'qwertyuiopasdfghjklzxcvbnm'
list_of_symbols = list(symbols)

def upper_or_lower(input_char):
    choice = random.randint(0, 1)
    a = input_char.lower()
    b = input_char.upper()
    return a if choice == 0 else b

def generate_code():
    number_of_symbols = 7
    code = []
    for i in range(number_of_symbols):
        code.append(upper_or_lower(list_of_symbols[random.randint(0, len(list_of_symbols) - 1)]))
    return ''.join(code)


def add_to_urls(in_url, in_code = generate_code()):
    if in_code not in urls:
        urls.update({in_code: in_url})
    else:
        add_to_urls(in_url, generate_code())

def get_by_code(in_code):
    if urls.get(in_code) is not None:
        print(urls.get(in_code))
    else:
        print(f'element with key {in_code} doesn\'t exist in dictionary')

add_to_urls('wikipedia.com', 'AAAAAAA')
add_to_urls('stackoverflow.com', 'AAAAAAA')
add_to_urls('google.com')
add_to_urls('facebook.com')

print(urls)
get_by_code('AAAAAAA')
get_by_code('BBBBBBB')








