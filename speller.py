import sys
from os import path
import re


def speller():
    if path.exists(sys.argv[1]) and path.exists(sys.argv[2]):
        with open(sys.argv[1], 'r') as dictionary_file:
            dictionary = set(dictionary_file.read().split())
        with open(sys.argv[2], 'r') as text_file:
            text1 = text_file.read()
            text2 = re.sub(r"[^A-Za-z']+", " ", text1)
            text = text2.split()
            # прибираю ' тільки на початку слів
            for i in range(len(text)):
                if text[i][0] == "'":
                    text[i] = text[i][1:]
        for word in text:
            if word.lower() not in dictionary:
                with open("text_key.txt", "w") as file:
                    file.write('MISSPELLED WORDS:\n\n')
                    counter = []
                    for i in text:
                        if i.lower() not in dictionary and i.lower() != '':
                            file.write(i + '\n')
                        if i.lower() not in dictionary and i.lower() != '':
                            counter.append(i)
                    file.write(f'\nWORDS MISSPELLED:     {len(counter)}\n')
                    file.write(f'WORDS IN DICTIONARY:  {len(dictionary)}\n')
                    file.write(f"WORDS IN TEXT:        {len(text1.split())}")
                    break


print(speller())

