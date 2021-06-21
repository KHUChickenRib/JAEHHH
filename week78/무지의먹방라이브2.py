import heapq
def solution(food_times, k):
    answer = 0
    time = 0
    q = []
    answer_rs = []
    # 1. 우선쉰위 큐에 (food_times, 음식번호 순으로 담음)
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    # [3,5,1,5,4,3] 가
    # [1,3,3,5,5,6] 로

    # pop 하기 이전 pop한 값 (0, 1, 3, 3, 5, 5, 6) 순으로 될 것임
    pre_food = 0
    flag = True
    while flag:
        # 예외처리
        if not q:
            return -1
        # q의 길이
        length = len(q)
        # (현재 가장 작은시간 - 이전음식) * 길이
        # 첫번째 : 1 * 6 만큼 빠짐
        # 두번째 : 2 * 5 만큼 빠짐
        time += (q[0][0] - pre_food) * length
        if time > k:
            time -= (q[0][0] - pre_food) * length
            while q:
                # 위치 추가
                answer_rs.append(heapq.heappop(q)[1])
            answer_rs.sort()
            answer = answer_rs[(k-time) % length]
            flag = False
        else:
            pre_food = heapq.heappop(q)[0]
    return answer

food_times = [3,5,1,6,4,3]
k = 20
print(solution(food_times, k))