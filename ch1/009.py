import math
import random


def sort_string(sentence):
    result_l = []
    sentence_l = sentence.split()
    for s in sentence_l:
        if len(s) <= 4:
            result_l.append(s)
            continue
        # print(f'{s=}')
        sort_s = list(s[1:-1])
        # print(f'{sort_s=}')
        for i in range(1, len(sort_s)):
            r = math.floor(random.random() * len(sort_s))
            sort_s[i], sort_s[r] = sort_s[r], sort_s[i]
        sort_s.insert(0, s[0])
        sort_s.append(s[-1])
        # print(sort_s)

        result_l.append(''.join(sort_s))

    return ' '.join(result_l)


print(sort_string('I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'))
