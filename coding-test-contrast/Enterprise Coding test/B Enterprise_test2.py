# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys


def dfs(x, y, tmp):
    global N, arr_input, v, ans
    v[x][y] = True      # True로 방문 표시

    # 방향 벡터 사용 
    dx = [0, 0, 1, -1]  
    dy = [1, -1, 0, 0] 

    if x == N - 1 and y == N - 1:
        ans.append(tmp)

    else : 
        # 방향 벡터 dx,dy -> 0,1,2,3 이므로 range(4)
        for i in range(4):

            # 범위 지정
            if x + dx[i] >= 0 and x + dx[i] < N and y + dy[i] >= 0 and y + dy[i] < N:

                # v list value False 이고 arr_input value 1 방문할 수 있는 곳이라면 ~ 
                if v[x + dx[i]][y + dy[i]] == False and arr_input[x + dx[i]][y + dy[i]] == 1:
                    tmp += 1
                    dfs(x + dx[i], y + dy[i], tmp)   # dfs(0,1,1) 재귀 호출

                    v[x + dx[i]][y + dy[i]] = False  # v[0][1] = False  
                    tmp -= 1



# --------------- main ----------------------
ans = []
N = int(sys.stdin.readline())
arr_input = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 2차원 배열 list ->  [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0], [1, 1, 1, 1, 1]]
v = [[False for _ in range(N)] for _ in range(N)]  # [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]


dfs(0,0,0)
print(min(ans) + 1)