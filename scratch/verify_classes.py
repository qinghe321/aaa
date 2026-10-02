import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

with open("js/main.js", "r", encoding="utf-8") as f:
    js = f.read()

class_selectors = re.findall(r'\$\$?\(["\']\.([a-zA-Z0-9_-]+)["\']\)', js)
class_selectors = sorted(list(set(class_selectors)))

print(f"Total class selectors in JS: {len(class_selectors)}")
for c in class_selectors:
    in_html = f'class="' in html and c in html
    in_css = f'.{c}' in css
    print(f"  .{c}: HTML={'YES' if in_html else 'NO'}, CSS={'YES' if in_css else 'NO'}")
