def solution(absolutes, signs):
    answer = []
    num = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer.append(absolutes[i])
        else:
            answer.append(-absolutes[i])
    for i in range(len(answer)):
        num += answer[i]
    return num