import requests

try:
    requests.get("http://www.pudim.com.br/")
except:
    print('\033[91mNão consegui acessar o Site Pudim :(\033[m')
else:
    print('\033[92mO site Pudim está ACESSIVEL\033[m')
