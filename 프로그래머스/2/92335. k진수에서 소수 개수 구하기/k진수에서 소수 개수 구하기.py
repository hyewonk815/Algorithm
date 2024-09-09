def solution(n, k):
    answer = -1
    tmp = ''
    while n:
        tmp = str(n % k) + tmp
        n //= k
    tmp_z = tmp.split("0")
    count = 0
    for i in tmp_z:
        if (i == '1')| (i == ''):
            continue
        num = int(i)
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                break
        else:
            count += 1
    return count