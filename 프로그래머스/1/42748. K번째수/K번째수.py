def solution(array, commands):
    answer = []
    answer_1 = []
    for i in range(len(commands)):
        answer.append(array[commands[i][0]-1:commands[i][1]])
        answer[i].sort()
    for j in range(len(commands)):
        answer_1.append(answer[j][commands[j][2]-1])
    return answer_1