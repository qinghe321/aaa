import re

with open("js/main.js", "r", encoding="utf-8") as f:
    text = f.read()

stages = re.findall(r'stage:\s*"([^"]+)"', text[:53000])
for i, s in enumerate(stages):
    print(i + 1, s)
