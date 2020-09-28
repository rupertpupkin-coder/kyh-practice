import webbrowser

from pathlib import Path

p = Path('uppgift29_template.html')
#webbrowser.open(str(p))

s = "Hejsan Banarne!"

s2 = s.replace("H", "D")

print(s2)