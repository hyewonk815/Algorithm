def solution(n, t, m, p):
    alpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    answer = ''
    game = ''
    time = p - 1
    # 숫자를 n 진수로 변환
    for i in range(m*t):
        tmp = ''
        if i == 0:
            tmp = '0'
        while i:
            remainder = i % n
            if remainder >= 10:
                tmp = alpha[remainder] + tmp
            else:
                tmp = str(i % n) + tmp
            i //= n
        game += tmp
    # 튜브가 말해야 하는 숫자만 추출
    while len(answer) < t:
        answer += game[time]
        time += m
    return answer