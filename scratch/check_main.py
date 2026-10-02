import re

with open("js/main.js", "r", encoding="utf-8") as f:
    content = f.read()

print("File size:", len(content))
# Check bamboo slips
pos = content.find("商代甲骨·初文")
print("Found bamboo slips at:", pos)

# Check syntax glitch
pos_glitch = content.find("];,")
print("Found glitch at:", pos_glitch)
