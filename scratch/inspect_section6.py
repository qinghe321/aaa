with open("js/main.js", "r", encoding="utf-8") as f:
    text = f.read()

import re
h7 = text.find("6. 第三幕 · 印刷")
h8 = text.find("7. 第四幕 · 电与通信")
print("H7:", h7, "H8:", h8)
print(text[h7-60:h8])
