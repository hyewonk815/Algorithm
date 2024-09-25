def solution(n, computers):
    answer = 0
    visited = [0] * n
    def bfs(i):
        visited[i] = 1
        for j in range(n):
            if (computers[i][j] == 1) and not visited[j]:
                bfs(j)
    for k in range(n):
        if not visited[k]:
            bfs(k)
            answer += 1
    return answer