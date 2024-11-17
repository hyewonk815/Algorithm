def solution(n, costs):
    answer = 0
    # 중복 제거
    island = set([costs[0][0]])
    # 세 번째 값을 기준으로 오름차순 정렬
    costs.sort(key=lambda x:x[2])
    print(costs)
    while len(island) != n:
        for x,y,z in costs:
            if x in island and y in island:
                continue
            if x in island or y in island:
                # island.extend([x,y]) -> set 지원 X
                island.update([x,y])
                answer += z
                break
    return answer