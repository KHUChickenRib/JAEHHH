
def checkcheck(time,li):
    cnt=0
    # 3602003
    start=time
    # 3603003
    end=time+1000
    for i in li:
        # 3604002 > 3602003 and 3602003 < 3603003
        if i[1] >= start and i[0] < end:
            cnt += 1
    return cnt

def solution(lines):
    start = []
    end = []
    time = []
    li = []
    for i in range(len(lines)):
        """ 리스트 추가 """
        # 걸린 시간 s 제거 추가
        # [2000, 2000]
        time.append(int(float(lines[i].split()[2][:-1])*1000))
        # end 시간 추가
        # [3604002, 3607000]
        endTemp = lines[i].split()[1]
        endTemp = int(endTemp[0:2])*60*60*1000+int(endTemp[3:5])*60*1000+int(float(endTemp[6:])*1000)
        end.append(endTemp)
        # start 시간 추가
        # [3602003, 3605001]
        start.append(end[i]-time[i]+1)

        # 최종 list 
        # [[3602003, 3604002], [3605001, 3607000]]
        li.append([start[i], end[i]])

    # 리스트 1개일때 1개 반환    
    if len(end) == 1:
        return 1

    print(li)
    # max 계산
    max1 = 1
    for i in li:
        # 1, 3602003, 3604002
        max1 = max(max1,checkcheck(i[0],li),checkcheck(i[1],li))
    return max1

"""
lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
"""
lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))