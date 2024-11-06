from collections import defaultdict

def solution(tickets):
    answer = []
    tree = defaultdict(list)
    for start, end in tickets:
        tree[start].append(end)
    for start in tree:
        tree[start].sort(reverse=True)
    def dfs(start):
        while tree[start]:
            end = tree[start].pop()
            dfs(end)
        answer.append(start)
    dfs("ICN")
    return answer[::-1]