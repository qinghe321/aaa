with open("js/main.js", "r", encoding="utf-8") as f:
    text = f.read()

import re
headers = [m.start() for m in re.finditer(r'/\* ============================================================', text)]
for idx, pos in enumerate(headers):
    snippet = text[pos:pos+150].replace('\n', ' ')
    print(f"Header {idx} at {pos}: {snippet[:80]}")
