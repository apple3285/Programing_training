'''첫번째 시도 : 딕셔너리와 startswith,endswith를 사용
효율성 테스트 1,2,3 통과 못함 
1 - > 모두 '?' 인 경우 처리
3 - > 같은 쿼리가 있는 경우 처리
2는 효율성 통과 못함 트리를 사용해야한다고 함
=> 이코테 답지 보고 공부해야함
'''
import re
def solution(words, queries):
    answer = []
    word_dict = {}
    answer_dict = {}
    for word in words:
        len_word = len(word)
        if len_word in word_dict.keys():
            word_dict[len_word].append(word)
        else:
            word_dict[len_word] = [word]

    for querie in queries:
        cnt=0
        len_querie = len(querie)
        if querie in answer_dict.keys():
            cnt = answer_dict[querie]
        elif len_querie in word_dict.keys():
            candidate_words = word_dict[len_querie]
            clean_querie = re.sub("\?", "", querie)
            if len(clean_querie)==0:
                cnt=len(candidate_words)
            elif querie[0] == "?":
                for word in candidate_words:
                    if word.endswith(clean_querie) :
                        cnt+=1
            elif querie[-1] == "?":
                for word in candidate_words:
                    if word.startswith(clean_querie):
                        cnt+=1
        answer_dict[querie] = cnt
        answer.append(cnt)
    return answer
#startswith() : 문자열이 인자로 전달된 문자열로 시작하는지 확인
# endswith(): 문자열이 인자로 전달된 문자열로 끝나는지 확인
#정규식에서 물음표는 메타 문자이기 때문에 앞에 '\'를 써줘야함
