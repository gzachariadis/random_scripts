from googletrans import Translator
import re

greek_alphabet = 'ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσςΤτΥυΦφΧχΨψΩω'
latin_alphabet = 'AaBbGgDdEeZzHhJjIiKkLlMmNnXxOoPpRrSssTtUuFfQqYyWw'
greek2latin = str.maketrans(greek_alphabet, latin_alphabet)
letters_list = []
names_list = []

# Reads File
file1 = open('my_file.txt', 'r', encoding="utf8")
Lines = file1.readlines()

# Goes line by line and extracts names
for line in Lines:
    line = re.sub(r'[^\w\s]', '', str(line).strip())
    name = str(line.strip())
    translator = Translator(service_urls=['translate.googleapis.com'])
    english_name = translator.translate(name, src='el', dest='en').text
    direct_trans = line.strip().translate(greek2latin)
    if english_name not in names_list:
        names_list.append(english_name)
    if direct_trans not in names_list:
        names_list.append(direct_trans)

print(names_list)

# Goes letter by letter in each name
for i in names_list:
    i = "[" + i.capitalize() + i.lower() + "]{1,}"
    letters_list += [i]

# print(letters_list)

# test_list += ["(author.name) match r\"^.*"]

# test_list += [".*$\""]

# print(''.join(test_list))

