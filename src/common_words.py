import re
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.tokenize import word_tokenize
wnl = WordNetLemmatizer()

def is_word_noun(word):

    word_tags = nltk.pos_tag([word])
    for word_list in word_tags:
        for classification in word_list:
            if 'N' in classification:
                return True
    return False

def is_valid_line(line):

    ## ToDo, Make this nice
    if 'bag' in line  or 'clothes' in line or 'tech' in line or 'toiletries' in line or  'misc' in line or'www' in line or '_________' in line or '###' in line:
        return False
    else :
        return True

wordcount = {}
# data = get_data_from_file("Transformed-output.md")
for line in data:

    if is_valid_line(line):
        for word in word_tokenize(re.sub(r'\W+', ' ', line.lower()).strip()):

            if len(word) > 2:
                word = wnl.lemmatize(word)
                if is_word_noun(word) :
                    if word in wordcount:
                        wordcount[word] += 1
                    else:
                        wordcount[word] = 1

for item in {k: v for k, v in sorted(wordcount.items(),reverse=True, key=lambda x: x[1])}:
    print(item + "," + str(wordcount[item]))
