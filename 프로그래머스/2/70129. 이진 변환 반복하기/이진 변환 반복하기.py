def solution(s):
    count = 0
    count_z = 0
    while s != "1":
        count_z += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        count += 1
    return [count, count_z]