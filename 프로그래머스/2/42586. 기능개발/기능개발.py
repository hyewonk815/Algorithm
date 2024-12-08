import math
def solution(progresses, speeds):
    answer = []
    time = []
    for i in range(len(progresses)):
        time.append(math.ceil((100-progresses[i]) / speeds[i]))
    current = time[0]
    count = 0
    for t in time:
        if t <= current:
            count += 1
        else:
            answer.append(count)
            current = t
            count = 1
    answer.append(count)
    return answer