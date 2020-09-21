import webbrowser
import requests
from pathlib import Path



r = requests.get("https://api.adviceslip.com/advice")           # Get-metoden för att nå data i advice
advice = r.json()                                               #
dict = advice['slip']                                           # Variabel som tar värdet från 'slip'
value = dict['advice']       # Variabel som låter oss nå dic-keys som finns i 'slip'


content = Path('uppgift29_template.html').read_text()
html = content.replace('QUOTE_TEXT', value)


p = Path('goat_quote.html')
p.write_text(html, encoding='utf8')

webbrowser.open(p)