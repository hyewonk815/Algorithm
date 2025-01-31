def solution(clothes):
    # answer = {key: value for value, key in clothes}
    answer = 0
    dic = {}
    for x, y in clothes:
        if y not in dic:
            dic[y] = 1
        else:
            dic[y] += 1
    if len(dic.keys()) == 1:
        for v in dic.values():
            answer += v
        return answer
    else:
        for v in dic.values():
            if answer == 0:
                answer += v+1
            else:
                answer *= v+1
        return answer - 1

# 실패코드 1
# def solution(clothes):
#     answer = len(clothes)
#     for i in range(len(clothes)-1):
#         for j in range(i+1, len(clothes)):
#             if clothes[i][1] != clothes[j][1]:
#                 answer += 1
#     return answer

# 실패코드 2
# def solution(clothes):
#     # answer = {key: value for value, key in clothes}
#     answer = 0
#     dic = {}
#     for x, y in clothes:
#         if y not in dic:
#             dic[y] = 1
#         else:
#             dic[y] += 1
#     if len(dic.keys()) == 1:
#         for v in dic.values():
#             answer += v
#         return answer
#     else:
#         for v in dic.values():
#             answer += v + 1
#         return answer