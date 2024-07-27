import re

def solution(s):
    num = re.split(r'\D+', s)
    num_filter = list(filter(None, num))
    num_dic = dict.fromkeys(num_filter, 0)
    for key in num_dic.keys():
        num_dic[key] += num_filter.count(key)
    answer = dict(sorted(num_dic.items(), key=lambda item: item[1], reverse=True)).keys()
    return list(map(int, answer))