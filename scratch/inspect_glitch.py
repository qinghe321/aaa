with open("js/main.js", "r", encoding="utf-8") as f:
    text = f.read()

pos_glitch = text.find("];,")
idx2 = text.find("const slipElements = [];", pos_glitch)
print("From glitch to slipElements:")
print(text[pos_glitch:pos_glitch+50])
print("...")
print(text[idx2-50:idx2+60])
