import requests
from bs4 import BeautifulSoup
address = 'https://context.reverso.net/translation/english-french/cheese'
lang = input('Type "en" if you want to translate from French into English, or "fr" if you want to'
             'translate from English into French\n')

word = input('Type the word you want to translate:\n')
print('You chose "{}" as the language to translate "{}" to.'.format(lang, word))
if lang == 'fr':
    add = address + 'english-french' + word
    r = requests.get(add)
    if r.status_code == 200:
        print('200 OK')
    soup = BeautifulSoup(r.content, 'html.parser')
