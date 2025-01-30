def solution(citations):
    citations_sorted = sorted(citations, reverse=True)
    for i, citation in enumerate(citations_sorted):
        if citation < i + 1:
            return i
    return len(citations)
    # 실패코드 1 (효율성 통과 X)
    # for i in range(1, len(citations)+1):
    #     count = 0
    #     for j in citations:
    #         if i <= j:
    #             count += 1
    #     if i < count:
    #         return count-1
    
    # 실패코드 2 ('NoneType' object is not iterable)
    # citations_sorted = citations.sort(reverse=True) -> none 반환
    # for i in range(1, len(citations)+1):
    #     count = 0
    #     for j in citations_sorted:
    #         if i <= j:
    #             count += 1
    #         else:
    #             if count > i:
    #                 return i