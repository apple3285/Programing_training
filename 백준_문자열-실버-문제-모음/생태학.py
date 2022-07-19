#공부할 것
# 입력에 제한이 없는 경우 알아보기 sys.stdin으로 입력 받는 방법 공부하기
#input 과 sys.stdin차이
##round와 %.f 차이 https://blockdmask.tistory.com/418
import sys
import collections
tree_data = []

for line in sys.stdin:#sys.stdin은 ^Z를 입력받으면 종료되며, 위 결과에서 보다시피 개행문자까지 입력되는걸 볼 수 있다.따라서 strip()이나 rstrip()으로 제거 필요 - https://developeryuseon.tistory.com/90 
    if line == "/n":
        break
    tree_data.append(line.rstrip())

trees_cnt = len(tree_data)
tree_dict = collections.Counter(tree_data)
tree_dict = sorted(tree_dict.items())
#round로 출력하면 실패함 %.f 사용
for tree in tree_dict:
    print(tree[0],"%.4f" %round((tree[1]/trees_cnt)*100,4))


