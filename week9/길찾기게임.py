# 트리깊이 1000제한 풀기위함
import sys

# class 생성
# id, x, y(입력), left, right
class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None
    
    # sort 함수에 적용됨 (lt : <)
    def __lt__(self, other):
        if (self.y == other.y):
            return self.x < other.x
        # 큰 y 순서대로
        return self.y > other.y
    
def addNode(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            addNode(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            addNode(parent.right, child)

def preorder(ans, node):
    # none 이면 끝냄
    if node is None:
        return
    ans.append(node.id)
    preorder(ans, node.left)
    preorder(ans, node.right)

def postorder(ans, node):
    # none 이면 끝냄
    if node is None:
        return
    postorder(ans, node.left)
    postorder(ans, node.right)
    ans.append(node.id)

def solution(nodeinfo):
    # 트리깊이 1000 제약 해제(파이썬 기본 1000)
    sys.setrecursionlimit(1500)
    
    size = len(nodeinfo)
    nodelist = []
    for i in range(size):
        nodelist.append(Node(i+1, nodeinfo[i][0], nodeinfo[i][1]))
    # lt 규칙에 따라 정렬됨
    nodelist.sort()

    # root 설정
    root = nodelist[0]

    # 노드 추가 : left, right
    for i in range(1, size):
        addNode(root, nodelist[i])

    answer = [[], []]
    # 순회
    preorder(answer[0], root)
    postorder(answer[1], root)
    return answer


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))