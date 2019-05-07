import re
wordcount = {}

with open("Transformed-output.md", encoding="utf8") as f:
    content = f.readlines()
content = [x.strip() for x in content]

ignore = ['bag','clothes','tech','toiletries','misc']

for line in content:
    if not ('www' in line):
        for word in line.split(" "):
            word = str(re.sub(r'\W+', ' ', word.lower()).strip())
            if not word == '':
                if word in ignore:
                    continue
                if not word in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1

print(wordcount)

for item in wordcount:
    print(item + "," + str(wordcount[item]))