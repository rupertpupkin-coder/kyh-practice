import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template.html')

# definition av ny klass "Djur"

class Djur:

    # init konstruerar en "instans" av klassen "Djur"
    def __init__(self, djur, carnivore, wiki_url):
        self.carnivore = carnivore
        self.djur = djur
        self.wiki_url = wiki_url
    #34.2
    def carnivore_or_vegetarian(self):
        return 'Köttätare' if self.carnivore else 'Vegetarian'
#        if self.carnivore:
#           return "Köttätare"
#       else:
#          return "Vegetarian"

    #34.3
    def get_html_table_row(self):
        self.html = f'<tr><td><a href="{self.wiki_url}">{self.djur}</a></td><td>{self.carnivore_or_vegetarian()}</td></tr>\n'


if __name__ == '__main__':
    djur = []
    # Skapa två instanser av klassen "Djur"
    # instans kallas också "objekt" eller "klassinstans"
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')
    giraff = Djur('Giraff', False, 'https://sv.wikipedia.org/wiki/Giraff')
    lejon = Djur('Lejon', True, 'https://sv.wikipedia.org/wiki/Lejon')
    hyena = Djur('Hyena', True, 'https://sv.wikipedia.org/wiki/Hyenor')
    djur.append(zebra)
    djur.append(tiger)
    djur.append(giraff)
    djur.append(lejon)
    djur.append(hyena)
    html = '<html><table>'
    for d in djur:
        html += d.get_html_table_row()
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))


