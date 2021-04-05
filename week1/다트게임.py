def solution(dartResult):
    temp = dartResult
    temp += '000000'
    arr = []
    
    # 3부분 나눔
    for i in range(0,3):
        if temp[2] == '*' or temp[2] =='#':
            a = temp[0:3]
        elif temp[3] == '*' or temp[3] =='#':
            a = temp[0:4]
        elif temp[2] == 'S' or temp[2] =='D' or temp[2] =='T':
            a = temp[0:3]
        else:
            a = temp[0:2]
        temp = temp.replace(a,'')
        arr.append(a)
    print(arr)
    arr1 = [0]*3

    # 1. 숫자만 빼기
    for i in range(0,3):
        if (arr[i])[1] == '0':
            arr1[i]=10
        else:
            arr1[i] = int((arr[i])[0])
    print(arr1)
    
    # 2. 1차 점수 계산 S, D, T
    for i in range(0,3):
        if arr[i].find('D') != -1:
            arr1[i] = arr1[i]*arr1[i]
        elif arr[i].find('T') != -1 :
            arr1[i] = arr1[i]*arr1[i]*arr1[i]
    print(arr1)

    # 2. 2차 점수 계산 *, #
    for i in range(0,3):
        if arr[i].find('*') != -1:
            arr1[i] = arr1[i]*2
            if i>0:
                arr1[i-1] = arr1[i-1]*2
        elif arr[i].find('#') != -1 :
            arr1[i] = arr1[i]*-1
    print(arr1)

    # return answer
    answer = arr1[0] + arr1[1] + arr1[2]
    return answer

a = "1D2S3T*"
print(solution(a))

"""
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
"""
