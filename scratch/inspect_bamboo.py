with open("js/main.js", "r", encoding="utf-8") as f:
    text = f.read()

idx2 = text.find("const slipElements = [];")
header5 = text.find("/* ============================================================\n     4. 第二幕 · 纸")
if header5 == -1:
    header5 = text.find("4. 第二幕 · 纸")
print("Section from slipElements to Header 5 is length:", header5 - idx2)
print("Snippet from slipElements:")
print(text[idx2:idx2+400])
print("Snippet before Header 5:")
print(text[header5-400:header5])
