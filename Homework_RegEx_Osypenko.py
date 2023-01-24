import re

# 1. Create RegEx to find specified pattern
text = 'HelloRbbbrrrqqq'
res_1 = re.findall(r'Rb+r{1}', text)
print('Pattern is found' if res_1 else 'No such pattern')


# 2. Credit card validation
def card_validation(card_num: str):
    return re.match(r"^(\d{4}[\s-]?){3}\d{4}$", card_num)


card = '7777-7777-7777 7777'
if card_validation(card):
    print('Card Valid')
else:
    print('Card Not Valid')


# 3. E-mail validation
def email_validator(email: str):
    return re.match(r"^[^_.-]([a-zA-Z0-9_\.\-]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email)


mail = "osypenko.k@gmail.com"
res_2 = email_validator(mail)
print('Email valid' if res_2 else 'Email not valid')


# 4. Login validation
def login_validation(login: str):
    return re.match(r"^([a-zA-Z0-9]{2,10})$", login)


login = "ThisLog007"
if login_validation(login):
    print('Login is Valid')
else:
    print('Login is not valid')
