# 백준 - N과 M (1)
# 백트래킹 : 모든 경우의 수를 탐색하는 대신 조건을 걸어서 유망(promising)하지 않은 경우에는 탐색을 중지하고 이전 노드로 돌아가서 다른 경우를 탐색한다.
# 이미 방문한 경우라면 제외하면서 M개를 고른 경우 출력
# https://velog.io/@yusuk6185/%EB%B0%B1%EC%A4%80-15649-N%EA%B3%BC-M-1-%ED%8C%8C%EC%9D%B4%EC%8D%AC-with-%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9
n,m = list(map(int,input().split()))
 
stack = []
#DFS 재귀함수
#stack : 출력되기 이해 숫자가 쌓일 스택
# 출력 조건 : stak 안에  m개의 요소가 쌓인 경우 
# 백트래킹 조건 : 아직 방문하지 않은 경우에만 방문 - 방문하는 경우 stack 에 값을 추가하고 DFS를 다시 실행하여 다음 자리 수로 넘어감
def dfs():
    if len(stack)==m:
        print(' '.join(map(str,stack)))
        return
    
    for i in range(1,n+1):
        if i not in stack:
            stack.append(i)
            dfs()
            stack.pop()
 
dfs()
