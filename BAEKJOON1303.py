import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, color):
    q = deque()
    cnt=0
    q.append((x, y))
    visited[x][y]=True
    while q:
        standardX, standardY = q.popleft()
        for i in range(4):
            nx = standardX + deltaX[i]
            ny = standardY + deltaY[i]
            
            if 0<=nx<M and 0<=ny<N:
                if visited[nx][ny]==False and arr[nx][ny]==color:
                    cnt+=1
                    visited[nx][ny]=True
                    q.append((nx, ny))
    
    return cnt+1

deltaX=[1, 0, -1, 0]
deltaY=[0, 1, 0, -1]
N, M = map(int, input().split())
MAX = 100
if not (1 <= N <= MAX and 1 <= M <= MAX):
    print('Not in range')

arr = [list(input().rstrip('\n')) for _ in range(M)]
visited = [[False]*N for _ in range(M)]
#print(visited)
#print(arr)
white_sum = blue_sum = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == False and arr[i][j] == 'W':
            white_sum += bfs(i, j, 'W') ** 2
        elif visited[i][j] == False and arr[i][j] == 'B':
            blue_sum += bfs(i, j, 'B') ** 2
            
print(white_sum, blue_sum)