# from pathlib import Path
# import json
#
#
# p = Path("massadata.json")
# s = p.read_text(encoding="utf8")
# o = json.loads(s)
# total = o
#
# sumValue1 = sum(d["item"] for d in total.values() if d)
# sumValue2 = sum(d['spec'] for d in total.values() if d)
# sumValue3 = sum(d['total'] for d in total.values() if d)
#
# print(sumValue1)
# print(sumValue2)
# print(sumValue3)
import json
from pathlib import Path
from pprint import pprint


def compute_total(json_object):
    entries_list = json_object["entries"]
    totals = []
    for entry in entries_list:
        totals.append(entry["total"])
    return sum(totals)

def main():
    p = Path("massadata.json")
    content = p.read_text(encoding="utf8")
    json_object = json.loads(content)
    total = compute_total(json_object)
    print(f"Total = {total}")



if __name__ == "__main__":
    main()