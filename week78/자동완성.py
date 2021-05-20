def solution(words):
    answer = 0
    words.sort()
    lens = len(words)

    for i in range(lens):
        cnt = 0
        # 첫번째
        if i==0:
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    break
                if words[i][j] == words[i+1][j]:
                    cnt += 1
                else:
                    break
            if cnt == len(words[i]):
                answer += cnt
            else:
                answer += cnt + 1
        # 마지막
        elif i==(lens-1):
            for j in range(len(words[i])):
                if j >= len(words[i-1]):
                    break
                if words[i][j] == words[i-1][j]:
                    cnt += 1
                else:
                    break
            if cnt == len(words[i]):
                answer += cnt
            else:
                answer += cnt + 1
        # 중간
        else:
            cntfront = 0
            cntback = 0
            # 앞 비교
            for j in range(len(words[i])):
                if j >= len(words[i-1]):
                    break
                if words[i][j] == words[i-1][j]:
                    cntfront += 1
                else:
                    break
            if cntfront != len(words[i]):
                cntfront += 1
            # 뒤 비교
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    break
                if words[i][j] == words[i+1][j]:
                    cntback += 1
                else:
                    break
            if cntback != len(words[i]):
                cntback += 1
            answer += max(cntfront, cntback)

    return answer


words = ["abc","def","ghi","jklm"]
print(solution(words))