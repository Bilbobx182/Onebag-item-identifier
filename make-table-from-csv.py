with open("test2.csv", encoding="utf8") as f:
    content = f.readlines()
content = ["|" + x.strip()  +"|" for x in content]

for line in content:
    print(line)