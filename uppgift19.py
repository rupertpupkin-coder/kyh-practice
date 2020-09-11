from pathlib import Path
import json

p = Path("data.json")
s = p.read_text(encoding="utf8")
o = json.loads(s)

print(o)


