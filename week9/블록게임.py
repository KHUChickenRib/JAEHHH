# 직사각형(6개) 중 0이 2개 들어간 것 찾기
def find(board, i, j, a, b):
    N = len(board)
    if i+a > N:
        return False
    if j+b > N:
        return False
    cnt = 0
    for x in range(i, i+a):
        for y in range(j, j+b):
            if board[x][y] == 0:
                cnt += 1
    if cnt == 2:
        return True

# 같은 도형으로 이루어져 있는지
# ex) 0 2 0 2 2 2
def same(board, i, j, a, b):
    N = len(board)
    arr = []
    for x in range(i, i+a):
        for y in range(j, j+b):
            arr.append(board[x][y])
    arr.sort()
    cnt = arr.count(arr[-1]) # 4개 
    if cnt == 4:
        return True
    else:
        return False

def changeposi(board, i, j, a, b):
    N = len(board)
    posi = True
    for x in range(i, i+a):
        for y in range(j, j+b):
            if board[x][y] == 0:
                # 위에 다 0
                for z in range(x):
                    if board[z][y] != 0:
                        posi = False
    # 변경
    if posi == True:
        for x in range(i, i+a):
            for y in range(j, j+b):
                board[x][y] = 0
        return True
    else:
        return False


def solution(board):
    answer = 0
    N = len(board)
    while 1:
        goz = False # 한바퀴 돌아도 변경 없으면 종료
        # 검색 시작 #
        for i in range(N):
            for j in range(N):
                if find(board, i, j, 2, 3): # 가로로 긴 2*3
                    if same(board, i, j, 2, 3): # 같은 도형으로 이루어져 있는지
                        if changeposi(board, i, j, 2, 3): # 변경
                            answer += 1
                            goz = True
                        
                if find(board, i, j, 3, 2): # 세로로 긴 3*2
                    if same(board, i, j, 3, 2):
                        if changeposi(board, i, j, 3, 2): # 변경
                            answer += 1
                            goz = True
        ### 
        # 검색 시 삭제 되는것 없으면 종료
        if goz == False:
            break
    return answer
board =     [[0, 0, 0, 0, 0]
          , [0, 0, 0, 0, 0], 
            [0, 4, 0, 3, 0], 
            [0, 4, 3, 3, 3], 
            [0, 4, 4, 0, 0]]
# board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
print(solution(board))