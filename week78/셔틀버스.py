def solution(n, t, m, timetable):
    minutes = []
    first = 540     # 첫차시간
    answer = 0
    for time in timetable:      # 분단위 계산
        a = time.split(':')
        minute = int(a[0]) * 60 + int(a[1])
        minutes.append(minute)
    minutes.sort()    # 대기자 정렬

    for i in range(0, n):   # 버스 운행
        count = 0           # 다음차 대기자 수
        for j in range(0, len(minutes)):    # 대기자수 계산
            if minutes[j] <= (first + (i*t)):
                count += 1
                if count == m:
                    break

        if i == n-1:    # 막차
            if count >= m:
                answer = minutes[m-1] -1   # 막차마지막탑승
            else:
                answer = first + (i * t)   # 막차시간탑승
            break
        else:           # 앞차 대기자 탑승
            if count >= m:
                minutes[:m] = []    # 정원 채워서 보내기
            else:
                minutes[:count] = []    # 대기자수 만큼 보내기

    # str변환
    mok = answer//60
    na = answer%60
    if mok < 10:
        mok = '0' + str(mok)
    else : 
        mok = str(mok)
    if na < 10:
        na = '0' + str(na)
    else:
        na = str(na)
    answer = mok + ':' + na
    return answer

""" 5번, 20번 오류
def solution(n, t, m, timetable):
    # 기본설정
    answer = 540
    # 분 단위로 초기화
    # [540, 540, 540, 540]
    temp = []
    for i in range(len(timetable)):
        temp.append(int(timetable[i][0:2])*60 + int(timetable[i][3:5]))
    temp.sort()
    
    # 1,가장늦게타면 탈 수 있을 때 설정  
    # 10 60 45 -> 18:00 -> 1080
    # 2 10 2 -> 9:10 -> 550
    if n > 2:
        answer = (n-1)*t + 540

    # 2. 셔틀 탈 수 없는 크루 제거
    # [480, 549, 550]
    # [549, 550]
    i = 0
    answertemp = 540
    # [480]
    temp2 = []
    mcnt = 0
    if n==1:
        for i in range(len(temp)):
            if temp[i] > 540:
                temp2.append(temp[i])
        # 제거
        for i in temp2:
            temp.remove(i)
    temp2=[]
    # n > 1
    if n>1:
        # 큰 것 계산
        for i in range(len(temp)):
            if temp[i] > 540+(n-1)*t:
                temp2.append(temp[i])
        answer = 540+(n-1)*t
        # 제거
        for i in temp2:
            temp.remove(i)
        temp2=[]
        # 작은 것 계산
        for i in range(n-1):
            for j in range(len(temp)):
                if mcnt == m:
                    mcnt = 0
                    break
                if answertemp > temp[j]:
                    temp2.append(temp[j])
                    mcnt += 1
            
            for k in temp2:
                temp.remove(k)
            temp2 = []
            answertemp += t
            
    if len(temp)-m >= 0:
        answer = temp[m-1] -1
    
    
    # str변환
    mok = answer//60
    na = answer%60
    if mok < 10:
        mok = '0' + str(mok)
    else : 
        mok = str(mok)
    if na < 10:
        na = '0' + str(na)
    else:
        na = str(na)
    answer = mok + ':' + na
    

    return answer
""" 

n = 1
t = 1
m = 1
timetable = ["24:00"]
print(solution(n,t,m,timetable))
