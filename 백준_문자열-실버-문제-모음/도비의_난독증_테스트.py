#백준 2204 : 도비의 난독증 테스트(https://www.acmicpc.net/problem/2204)
import sys

for line in sys.stdin:
    n = int(line.rstrip())
    #0이 입력되면 종료
    if n == 0:
        break
    words={}
    # 대소문자 구분하지 않고 정렬하기 위해 {입력 단어 원본 : 소문자로 변환한 입력 단어} 형식의 딕셔너리로 저장
    for id in range(n):
        word = sys.stdin.readline().rstrip()
        words[word] = word.lower()
    #딕셔너리의 value 기준으로 정렬하여 사전상 오름차순 만들기
    sorted_words = sorted(words.items(),key = lambda x :x[1])
    #가장 앞서는 단어의 key(원본) 출력
    print(sorted_words[0][0])
