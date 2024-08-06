def solution(k, m, score):
    score.sort(reverse=True)
    total_price = 0
    for i in range(0, len(score), m):
        box = []
        box.extend(score[i:i+m])
        if len(box) < m:
            break
        total_price += min(box) * m
    return total_price