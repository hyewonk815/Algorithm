from collections import deque
def solution(maps):
    # 상하좌우 [-1, 0], [1, 0], [0, -1], [0, 1]
    dx = [-1, 1, 0, 0] # 상(-1), 하(+1), 좌우 이동 없음
    dy = [0, 0, -1, 1] # 좌(-1), 우(+1), 상하 이동 없음
    n, m = len(maps), len(maps[0]) # n: 맵의 세로 길이(행 개수), m: 맵의 가로 길이(열 개수)
    # 우선 출발지를 기준으로 상하좌우 탐색이 가능한 길인지 검증 후 점차 탐색영역을 넓혀서 넓게 탐색해야 함
    def bfs(x,y):
        queue = deque()
        queue.append((x,y)) # 시작점 (x, y)를 큐에 추가
        # queue가 빌 때까지 반복
        while queue:
            x, y = queue.popleft() # 큐에서 가장 앞에 있는 좌표 (x, y)를 꺼냄
            # 상하좌우 칸 확인하기
            for i in range(4):
                nx = x + dx[i] # 새로운 x좌표는 현재 x좌표에 dx[i]를 더한 값
                ny = y + dy[i] # 새로운 y좌표는 현재 y좌표에 dy[i]를 더한 값
                # 맵을 안 벗어나는 경우
                if 0 <= nx < n and 0 <= ny < m: # 새로운 좌표 (nx, ny)가 맵 안에 있는지 확인
                    # 벽이면 무시하기
                    if maps[nx][ny] == 0:
                        continue # 벽이므로 다음 방향으로 이동
                    # 처음 지나가는 길이면 거리 계산 후 다시 상하좌우 확인하기
                    if maps[nx][ny] == 1:
                        maps[nx][ny] = maps[x][y] + 1 # 이전 좌표에서의 값에 1을 더해 거리를 기록
                        queue.append((nx, ny)) # 큐에 새로운 좌표 (nx, ny)를 추가해 다음에 탐색
        # 상대 팀 진영(제일 오른쪽 아리 칸)까지의 거리 반환
        # 이 값이 시작점에서 목표 지점까지의 최단 경로의 길이를 나타냄
        return maps[n-1][m-1]
    answer = bfs(0,0)
    # 만약 목표 지점의 값이 1이라면, 경로가 없다는 뜻이므로 -1을 반환
    return -1 if answer == 1 else answer