def solution(N, stages):
    answer = []
    # 횟수 출력
    count = [0] * (N+1)
    # 실패율
    fail = {}
    # 전체 
    total = len(stages)

    # 1 2 3 4 5 횟수 입력
    # [1, 3, 2, 1, 0, 1]
    for i in stages:
        count[i-1] += 1
    
    # 실패율 계산
    for i in range(N):
        if total != 0:
            fail[i+1] = count[i]/total
        total -= count[i]
    
    # value값 기준 정렬
    fail = sorted(fail.items(), key=lambda x: x[1], reverse=True)

    # 키값만 추가
    for i,j in fail:
        answer.append(i)

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution((N), stages))