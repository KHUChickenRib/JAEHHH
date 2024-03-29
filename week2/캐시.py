def solution(cacheSize, cities):
    # 걸린시간
    answer = 0
    # 캐시사이즈 0일때
    if cacheSize == 0:
        return len(cities) * 5

    # 대소문자 구분없이
    for i in range(0, len(cities)):
        cities[i] = cities[i].lower()
    
    # 캐시 리스트
    temp = [' '] * cacheSize
    # 들어온 순서 리스트 -> 0 1 2 / 3 1 2 / 3 4 2 ...
    countArr = [0] * cacheSize
    # 들어온 순서 cnt
    cnt = cacheSize

    # 시작 값 구하기
    num = 0

    for i in cities:
        if i in temp:
            answer += 1
            countArr[temp.index(i)] = cnt
        else:
            answer += 5
            temp[countArr.index(min(countArr))] = i
            countArr[countArr.index(min(countArr))] = cnt
        cnt += 1
        
    return answer

# 실행 예
cacheSize = 11
cities = ["Jeju", "Soeul",  "Jeju", "Jeju"]
print(solution(cacheSize, cities))

""" 다른 답
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
"""