# top-down(재귀함수), bottom-up(재귀 호출 X)

def solution(triangle):
    for i in reversed(range(len(triangle)-1)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]