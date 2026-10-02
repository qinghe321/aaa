import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("js/main.js", "r", encoding="utf-8") as f:
    js = f.read()

# Extract IDs in JS: $("#...")
id_selectors = re.findall(r'\$\(["\']#([a-zA-Z0-9_-]+)["\']\)', js)
# Extract getElementById
id_selectors += re.findall(r'getElementById\(["\']([a-zA-Z0-9_-]+)["\']\)', js)

id_selectors = sorted(list(set(id_selectors)))

missing_ids = []
found_ids = []
for i in id_selectors:
    pattern = f'id="{i}"'
    if pattern in html:
        found_ids.append(i)
    else:
        missing_ids.append(i)

print(f"Total IDs checked: {len(id_selectors)}")
print(f"Found IDs: {len(found_ids)}")
print(f"Missing IDs: {missing_ids}")

# Check key new IDs
key_ids = [
    "bambooCardEra", "bambooCardSource", "bambooCardTitle", "bambooCardReason",
    "printClassics", "printViewBlock", "printViewType", "woodblockGrid", "blockTryNewBtn", "blockWarning",
    "typeTrayGrid", "pressGrid", "pressBookTitle", "pressStatus",
    "metricReuse", "metricTime", "metricOutput",
    "aiPlayBtn", "playIcon", "playText", "stepGlyph", "stepToken", "stepEncode", "stepData",
    "bridgeStream", "blockEncoder", "blockDecoder", "head1", "head2", "head3", "decoderStatus"
]
print("\nChecking key new IDs:")
for k in key_ids:
    print(f"  {k}: {'EXISTS' if f'id=\"{k}\"' in html else 'MISSING'}")
