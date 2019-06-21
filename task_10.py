from termcolor import colored


def load_words():
    with open('words_alpha.txt') as word_file:
        return set(word_file.read().split())


def speller(text):
    text = list(filter(lambda s: s.isalpha(), text.lower().split(' ')))
    if not [i for i in text if i not in load_words()]:
        return colored('Орфографічні помилки відсутні!', 'green')
    else:
        return colored([i for i in text if i not in load_words()], 'red')


print(speller('''Do you want to know the histori of jeans?
 In 1850 a young man, Levi Strauss, camee to California fromn Germany. 
 California was famous for its gold. Many people were working there.'''))
