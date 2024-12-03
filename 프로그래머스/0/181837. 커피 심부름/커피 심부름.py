def solution(order):
    answer = 0
    for i in range(len(order)):
        if 'americano' in order[i] or "anything" in order[i]:
            answer += 4500
        else:
            answer += 5000
    return answer