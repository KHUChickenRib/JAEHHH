"""
다익스트라 목적
:: 특정위치(s)에서 모든 노드에 갈수있는 최단거리 [1차원 배열] 출력 : distance ::

다익스트라 사용법
[ 3가지 ]

 조건 : graph : graph[src] = [dst, value]

 1. distance : 1차원 배열
 2. heapq
  2-1. 초기경로 -> heappush(value, dst)   # 이진트리. value기준
  2-2. while q -> p dc g 거꾸로 비교
    - heappop
    - distance[now] < value
    - graph[now]
        -> next_value -> if -> heappush
"""

import heapq

INF = int(1e9) # 무한 값

# 다익스트라 구현, 특정위치 포함
def dijkstra(start, graph, n, s, a, b, fares):
    # 1. distance(목표) 초기화 
    distance = [INF] * (n+1)
    distance[start] = 0

    # 2-1 heap 초기화
    q = []
    heapq.heappush(q, (0, start))  # (value, dst)

    # 2-2 while
    while q:
        # heappop
        value, dst = heapq.heappop(q)
        
        # distance 비교
        if distance[dst] < value:
            continue
        
        # graph
        for d, v in graph[dst]:
            next_value = value + v
            if distance[d] > next_value:
                distance[d] = next_value
                heapq.heappush(q, (next_value, d))   # (value, dst)

    # distance 리턴!
    return distance


def solution(n, s, a, b, fares):
    # 조건 : graph 구현
    graph = [[] for _ in range(n + 1)]
    for src, dst, value in fares:
        graph[src].append((dst, value))
        graph[dst].append((src, value))  # 거리 같음
    
    
    dp = [[]] + [dijkstra(i, graph, n, s, a, b, fares) for i in range(1, n+1)]
    for i in dp:
        print(i)
    
    answer = INF
    for i in range(1, n+1):
        temp = dp[s][i] + dp[i][a] + dp[i][b]
        answer = min(answer, temp)

 
    return answer

n = 6  # 6*6 그래프  노드가 1, 2, 3, 4, 5, 6 있다.
s = 4  # 출발지점
a = 6  # a의 도착지점
b = 2  # b의 도착지점
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))