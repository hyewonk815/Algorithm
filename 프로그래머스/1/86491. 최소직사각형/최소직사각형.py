# 가로 길이를 더 긴 것으로
def solution(sizes):
    width = list(map(max, sizes))
    height = list(map(min, sizes))
    answer = max(width) * max(height)
    return answer