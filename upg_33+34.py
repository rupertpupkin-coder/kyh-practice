import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template.html')


class Djur:
    def __init__(self, djur, carnivore, wiki_url):
        self.carnivore = carnivore
        self.djur = djur
        self.wiki_url = wiki_url

    def carnivore_or_vegetarian(self):
        if self.carnivore:
            return "Köttätare"
        else:
            return "Vetegarian"


if __name__ == '__main__':
    djur = []
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
        cell_2 = d.carnivore_or_vegetarian()
        html += f'<tr><td><a href="{d.wiki_url}">{d.djur}</a></td><td>{cell_2}</td></tr>\n'
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))


