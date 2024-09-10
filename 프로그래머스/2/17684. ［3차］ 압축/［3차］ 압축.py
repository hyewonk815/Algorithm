def solution(msg):
    answer = []
    # 사전 만들기
    dic = {}
    for i in range(26):
        dic[chr(65 + i)] = i + 1
    # LZW 압축
    while True:
        # 마지막 추가
        if msg in dic:
            answer.append(dic[msg])
            break
        # 사전 추가
        for i in range(1, len(msg)+1):
            if msg[0:i] not in dic:
                answer.append(dic[msg[0:i-1]])
                dic[msg[0:i]] = len(dic) + 1
                msg = msg[i-1:]
                break
    return answer