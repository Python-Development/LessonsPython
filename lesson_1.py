import re
import collections
from functools import reduce
import itertools

print('"Hello, World!"')


def is_stressful(subj):
    if subj.isupper() or subj[-3:] == '!!!':
        return True
    subj = subj.lower()
    reg = re.compile('[^a-zA-Z ]')
    subj = (reg.sub('', subj))

    subj = list(subj)
    should_restart = True
    while should_restart:
        should_restart = False
        for i in range(len(subj) - 1):
            if subj[i] == subj[i + 1]:
                subj.remove(subj[i])
                should_restart = True
                break
    subj = ''.join(subj)

    if 'help' in subj or 'asap' in subj or 'urgent' in subj:
        return True
    else:
        return False


def time_converter(time):
    if time[:2] == '00':
        return '12' + time[2:] + ' a.m.'
    if int(time[:2]) > 13:
        new_format = int(time[:2]) - 12
        time = str(new_format) + time[2:]
        return time + ' p.m.'
    elif int(time[:2]) < 12:
        return str(int(time[:2])) + time[2:] + ' a.m.'
    else:
        return time + ' p.m.'


def bigger_price(limit: int, data: list) -> list:
    data = (sorted(data, key=lambda x: x['price'], reverse=True))
    return data[:limit]


def popular_words(text: str, words: list) -> dict:
    text = text.lower().split()
    dic = {}
    for i in range(len(words)):
        dic[words[i]] = text.count(words[i])
    return dic


def between_markers(text: str, begin: str, end: str) -> str:
    if begin not in text and end not in text:
        return text
    elif begin not in text:
        return text[:text.index(end)]
    elif end not in text:
        return text[text.index(begin) + len(begin):]
    elif text.index(begin) > text.index(end):
        return ''
    else:
        return text[text.index(begin) + len(begin):text.index(end)]


def checkio(data: list) -> list:
    data = [x for x in data if data.count(x) > 1]
    return data


def frequency_sort(items):
    dic = {}
    sort_array = []
    for i in items:
        dic[i] = items.count(i)
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for i in dic:
        for element, frequency in zip(*[iter(i)] * 2):
            for i in range(frequency):
                sort_array.append(element)
    return sort_array


def flat_list(array):
    # result = []
    # for el in array:
    #     if hasattr(el, "__iter__") and not isinstance(el, str):
    #         result.extend(flat_list(el))
    #     else:
    #         result.append(el)
    # return result
    return [int(i) for i in str(array).replace("[", "").replace("]", "").split(", ") if i != ""]


def long_repeat(line):
    # return max(len(max(re.findall(s + '+', line), key=len)) for s in set(line)) if len(line) else 0
    # -------------------------------------------------------------------------------------------------
    # if not line:
    #     return 0
    # consecutive_groups = [list(group) for key, group in itertools.groupby(line)]
    # print(consecutive_groups)
    # max_length = max(len(group) for group in consecutive_groups)
    # return max_length
    # -------------------------------------------------------------------------------------------------
    return max(len(list(j)) for i, j in itertools.groupby(line)) if line else 0
    # -------------------------------------------------------------------------------------------------
    # if not line:
    #     return 0
    # count = 1
    # result = 0
    # for i in range(len(line) - 1):
    #     if line[i] == line[i + 1]:
    #         count += 1
    #         continue
    #     if count > result:
    #         result = count
    #     count = 1
    # return max(count, result)


def sun_angle(time):
    degrees = sum((int(a) - 6) * 60 + int(b) for a, b in zip(*[iter(time.split(':'))] * 2)) * 0.25
    return degrees if 0 <= degrees <= 180 else "I don't see the sun!"


VOWELS = "aeiouy"


def translate(phrase):
    # skip = 0
    # new_phrase = ''
    # for i in range(len(phrase)):
    #     if skip > 0:
    #         skip -= 1
    #         continue
    #     if phrase[i] == ' ':
    #         new_phrase += phrase[i]
    #     elif phrase[i] not in VOWELS:
    #         new_phrase += phrase[i]
    #         skip = 1
    #     else:
    #         new_phrase += phrase[i]
    #         skip = 2
    # return new_phrase
    phrase = re.sub(r'([bcdfghjklmnpqrstvwxz])[aeiouy]', r'\1', phrase)
    phrase = re.sub(r'([aeiouy]){3}', r'\1', phrase)

    result = re.sub(r'India', 'the World', 'AV is largest Analytics community of India')
    print(result)
    return phrase


print(translate("hieeelalaooo"))
