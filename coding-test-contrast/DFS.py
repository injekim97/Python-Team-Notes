# dfs 특정한 노드 방문한 뒤 연결된 모든 노드 방문
def dfs(x,y) :

    # 주어진 범위에서 벗어나는 경우 종료
    # 즉 x,y 가 0또는 -1 보다 같거나 작을 경우와 N,M 크기보다 x,y가 클경우 종료
    if x <= -1 or x >= N or y <= -1 or y >= M :
        return False

    # 혀재 노드를 아직 방문하지 않았다면    
    if graph[x][y] == 0 :
        graph[x][y] = 1 # 값을 1로 부여하여 방문처리 

        # 상,하,좌,우의 위치들을 모두 재귀로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# ------------------------- main ---------------------------------
N, M = map(int, input().split()) # N * M 공백으로 구분 하여 입력



# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(N) :
    graph.append(list(map(int, input()))) # 공백 없이 0,1로 주어진 조건 값에 맞게 입력



# 모든 노드(위치)에 음료수 채우기
cnt = 0
for i in range(N) :
    for j in range(M):

        # 현재 위치에서 dfs 수행
        if dfs(i,j) == True :
            cnt += 1 # 방문처리가 되었다면 카운트 

print(cnt)