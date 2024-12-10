def solution(arr, k):
    answer = []
    arr_set = []
    for num in arr:
        if num not in arr_set:
            arr_set.append(num)
    if len(arr_set) < k:
        answer.extend(arr_set[:k])
        answer.extend([-1]*(k-len(arr_set)))
    else:
        answer.extend(arr_set[:k])
    return answer