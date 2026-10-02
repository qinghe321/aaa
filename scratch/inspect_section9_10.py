with open("js/main.js", "r", encoding="utf-8") as f:
    text = f.read()

h10 = text.find("9. 第六幕 · 芯片")
h11 = text.find("10. 第七幕 · AI")
h12 = text.find("11. 尾声")

print(f"H10: {h10}, H11: {h11}, H12: {h12}")
print("--- Section 9 (Chip) snippet ---")
print(text[h10-60:h10+200])
print("...")
print(text[h11-200:h11])
print("--- Section 10 (AI) snippet ---")
print(text[h11-60:h11+200])
print("...")
print(text[h12-200:h12])
