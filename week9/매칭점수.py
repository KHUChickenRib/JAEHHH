import re # 정규표현식
from collections import defaultdict # 키가 초기화 안돼 있어도 삽입 시 기본값으로 설정. 오류안남

def solution(word, pages):
    answer = []
    # 단어 소문자
    word = word.lower()
    # 기본점수, 외부링크수
    database = defaultdict(list) # list로 defaultdict 설정
    # 어떤 외부 링크가 참조되었는지 저장
    ext_link = defaultdict(list)

    for page in pages:
        # url 추출
        #   <meta property="og:url" content="https://careers.kakao.com/interview/list"/>
        # [1.] meta 분리
        # [<meta property="og:url" content="https://careers.kakao.com/interview/list"]
        meta = re.findall("<meta property=[\"]og:url.*[\"]", page)[0] # list형식이므로 0을 반환
        # [2.] content의 url 추출
        # content="https://careers.kakao.com/interview/list"
        content = re.findall("content=.*[\"]", meta)[0].replace("content=", '') # content의 URL
        
        body = re.findall("<body>.*</body>", page, re.DOTALL)[0] # DOTALL : \n 까지 포함
        # 외부링크
        external_links = re.findall('<a href\S*"', body) # 외부 링크
        # 외부링크수
        ext_cnt = len(external_links)
        base_score = 0
        texts = re.findall("[a-zA-Z]+", page) #단어별로 구분
        # 기본점수
        for text in texts:
            if text.lower() == word:
                base_score += 1
            
        for i in range(ext_cnt):
            external_links[i] = external_links[i].replace("<a href=", "")  # 불필요한 부분 삭제
            ext_link[external_links[i]].append(content)  # 외부링크의 데이터에 현재 content를 추가
        
        # 점수 저장. [기본점수, 외부링크수]
        database[content][0:2] = [base_score, ext_cnt]

        
    for data in database:
        base_score, ext_cnt = database[data]
        ext_score = 0
        for ext in ext_link[data]:
            a, b = database[ext]
            ext_score += (a / b)
        match_score = base_score + ext_score
        answer.append(match_score)

    return answer.index(max(answer))
            
                
#word = "Muzi"
#pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

word = "blind"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

print(solution(word, pages))