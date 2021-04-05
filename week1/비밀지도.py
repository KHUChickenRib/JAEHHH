def solution(n, arr1, arr2):
    cnt = -1
    answer = []
    while(1):
        cnt+=1
        if cnt==n:
            break


        ## 한줄씩
        a = (format(arr1[cnt], 'b'))
        b = (format(arr2[cnt], 'b'))
        temp = ['0']*n
        j=0
        for i in range((n-len(a)), n):
            temp[i] = a[j]
            j+=1

        j=0
        for i in range((n-len(b)), n):
            if temp[i]=='1':
                j+=1
            else:
                temp[i] = b[j]
                j+=1
        ##
        
        result=''.join(temp)
        result=result.replace('1','#')
        result=result.replace('0',' ')
        
        answer.append(result)
    return answer

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

print(solution(n, arr1, arr2))


"""
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
"""