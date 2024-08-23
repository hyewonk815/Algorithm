def solution(n, arr1, arr2):
    arr_1 = []
    arr_2 = []
    answer = []
    for i in range(n):
        answer_1 = ""
        arr_1.append(bin(arr1[i])[2:].zfill(n))
        arr_2.append(bin(arr2[i])[2:].zfill(n))
        for j in range(n):
            if (int(arr_1[i][j]) == 1) | (int(arr_2[i][j]) == 1):
                answer_1 += "1"
            else:
                answer_1 += "0"
        answer.append(answer_1)
        answer[i] = answer[i].replace("1","#").replace("0"," ")
    return answer