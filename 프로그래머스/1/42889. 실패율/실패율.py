def solution(N, stages):
    game = dict()
    people = len(stages)
    for i in range(1, N+1):
        k = stages.count(i)
        if k == 0:
            game[i] = 0
            people -= k
        else:
            game[i] = k / people
            people -= k
    answer = sorted(game.items(), key= lambda item:item[1], reverse=True)
    answer_k = [item[0] for item in answer]
    return answer_k