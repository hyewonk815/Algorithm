def solution(numbers, target):
    answer = 0
    bfs = [0]
    for num in numbers:
        res = []
        for data in bfs:
            res.append(data + num)
            res.append(data - num)
        bfs = res
    for i in range(len(bfs)):
        if target == bfs[i]:
            answer += 1
    return answer