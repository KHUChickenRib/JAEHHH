def solution(food_times, k):
    answer = 0
    # 배열 길이
    lens = len(food_times)
    # 정렬 [1, 2, 3]
    temp = sorted(food_times)
    # minus
    minus = 0
    # 회전수
    cycle = 0
    # 나머지 가야하는 수
    na = 0

    i = 0
    kexe = 0
    inx = 0
    k += 1
    if sum(food_times) < k:
        return -1
    while 1:
        for i in range(lens):
            if food_times[i] != 0:
                food_times[i] -= 1
                k -= 1
            if k == 0:
                kexe = 1
                inx = i
                break
        if kexe:
            break
    return inx + 1

food_times = [4,2,3,6,7,1,5,8]
k = 16
print(solution(food_times, k))