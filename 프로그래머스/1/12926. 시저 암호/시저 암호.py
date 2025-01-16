def solution(s, n):
    answer = ''
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in s:
        if i.isupper(): # 대문자
            upF = up.find(i)+n # find : 인덱스 반환
            answer += up[upF%26] # 알파벳 26으로 나눈 나머지
        elif i.islower():
            lowF = low.find(i)+n
            answer += low[lowF%26]
        else:
            answer += ' '
    return answer