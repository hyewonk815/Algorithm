def solution(n, m, section):
    answer = 0    
    while section:
        if m == 1:
            answer += len(section)
            break
        else:
            roller = section[0] + m -1
            section = [s for s in section if s > roller]
            answer += 1
    return answer