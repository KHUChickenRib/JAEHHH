
# 플로이드
def solution(n, s, a, b, fares):
    # 1. 그래프 초기화
    INF = int(1e9) # 무한 값
    graph = [[INF] * n for _ in range(n)]  # 초기화
    for i in range(n):
        graph[i][i] = 0     # 자기 자신 비용 0

    # 2. 주어진 fares값 -> graph 대입 
    for i in fares:
        graph[i[0]-1][i[1]-1] = i[2]
        graph[i[1]-1][i[0]-1] = i[2]  # 방향 상관없이 거리 같음
 
 
 
    """
    23 = min(23 / 2113)
    """    
    # 3. 플로이드 알고리즘
    for a1 in range(n):
        for a2 in range(n):
            for a3 in range(n):
                graph[a2][a3] = min(graph[a2][a3], graph[a2][a1]+graph[a1][a3])
                graph[a3][a2] = graph[a2][a3]   # 방향 상관없이 거리 같음
    

    answer = INF         # 초기 값
    # 경로 확인
    for i in range(n):
        # s 에서 같이간 곳 = i
        # min(s->i + i->a + i->b)
        temp = graph[s-1][i] + graph[i][a-1] + graph[i][b-1]
        answer = min(answer, temp)

    return answer