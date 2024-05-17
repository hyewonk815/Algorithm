def solution(strings, n):
    answer = []
    for i in strings:
        answer.append(i[n]+i)
    answer.sort()
    answer_i = []
    for j in answer:
        answer_i.append(j[1:])
    return answer_i