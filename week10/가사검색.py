class Trie:
    def __init__(self):
        # 자식
        self.child = dict()
        # 갯수
        self.count = 0

        # 삽입
    def insert(self, s):
        # 현재
        curr = self
        for ch in s:
            curr.count += 1
            # 없으면 새로 만들어줌
            if ch not in curr.child:
                curr.child[ch] = Trie()
            # 아래로 내려감
            curr = curr.child[ch]
        curr.count += 1
    
    def search(self, s):
        curr = self
        for ch in s:
            if ch == '?':
                return curr.count
            # 없으면 0 리턴
            if ch not in curr.child:
                return 0
            # 밑으로 내려감
            curr = curr.child[ch]
        return curr.count

def solution(words, queries):
    a = 'abcd'
    print(a[::-1])
    TriedRoot = [Trie() for _ in range(10000)]
    ReTriedRoot = [Trie() for _ in range(10000)]
    answer = []

    for s in words:
        TriedRoot[len(s)-1].insert(s)
        ReTriedRoot[len(s)-1].insert(s[::-1])
    
    for s in queries:
        if s[0] != '?':
            answer.append(TriedRoot[len(s)-1].search(s))
        else:
            answer.append(ReTriedRoot[len(s)-1].search(s[::-1]))
    
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))