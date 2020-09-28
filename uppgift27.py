import json
from pathlib import Path

p = Path("data.json")
content = p.read_text(encoding=("utf8"))
data = json.loads(content)


def main():
    print("Innehåll:                          100g")
    for elem in data:
        if elem['rightalign']:
            print(f"{elem['what']:>20} {elem['value']:17}{elem['unit']}")
        elif not elem['rightalign']:
            print(f"{elem['what']:20} {elem['value']:17}{elem['unit']}")


if __name__ == '__main__':
    main()
