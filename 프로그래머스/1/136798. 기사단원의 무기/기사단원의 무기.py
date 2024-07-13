def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        measure = 0
        for j in range(1, int(i**(1/2)) + 1):
            if (i % j == 0):
                measure += 1 
                if ( (j**2) != i) : 
                    measure += 1
        if measure <= limit:
            answer += measure
        else:
            answer += power
    return answer