def solution(n):
    answer = ''
    word = "수박"
    if n % 2 == 0:
        answer += word * (n // 2)
    else:
        answer += (word * ((n+1) // 2))[:-1]
    return answer