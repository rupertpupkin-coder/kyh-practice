import pathlib

p = pathlib.Path("system.log")

content = p.read_text()


def case():

    dokument = "system.log"
    important = []
    keep_phrases = ["BEAR", "X-RAY"]

    with open(dokument) as f:
        f = f.readlines()

    for line in f:
        line = line.strip()
        for phrase in keep_phrases:
            if phrase in line:
                important.append(line)
                break

    print(*important, sep="\n")


if __name__ == '__main__':
    case()
