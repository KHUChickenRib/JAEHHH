def solution(msg):
    answer = []
    #사전
    dic = []
    # A~Z 입력
    for i in range(0, 26):
        dic.append(chr(65+i))

    # 왼쪽 위치
    # KAKAO 라면, KA, AK, KAO로 나눠지게
    r = 0  
    for i in range(0, len(msg)):
        for j in range(r+1, len(msg)+1):
            # 사전에 없으면 추가
            if msg[r:j] not in dic:
                answer.append(dic.index(msg[r:j-1])+1)
                dic.append(msg[r:j])
                r += j-r-1
                break
    answer.append(dic.index(msg[r:])+1)
    return answer

msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))