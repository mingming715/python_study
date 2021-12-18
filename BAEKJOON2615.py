import sys
input = sys.stdin.readline

arr = [[int(x) for x in input().split()] for _ in range(19)]

def count(x, y, color):
    if color == 1:
        for i in range(4):
            nx = x + deltaX[i]
            ny = y + deltaY[i]
            cnt=1

            if nx<0 or ny<0 or nx>=19 or ny>=19:
                continue

            while 0<=nx<19 and 0<=ny<19 and arr[nx][ny]==1:
                cnt+=1

                if cnt == 5:
                    if 0<=nx+deltaX[i]<19 and 0<=ny+deltaY[i]<19 and arr[nx+deltaX[i]][ny+deltaY[i]]==1: #육목 확인1
                        break
                    if 0<=x-deltaX[i]<19 and 0<=y-deltaY[i]<19 and arr[x-deltaX[i]][y-deltaY[i]]==1: #육목 확인2
                        break
                    return 1, x+1, y+1

                nx+=deltaX[i]
                ny+=deltaY[i]
        return FinalColor, FinalX, FinalY
    if color == 2:
        for i in range(4):
            nx = x + deltaX[i]
            ny = y + deltaY[i]
            cnt=1

            if nx<0 or ny<0 or nx>=19 or ny>=19:
                continue

            while 0<=nx<19 and 0<=ny<19 and arr[nx][ny]==2:
                cnt+=1

                if cnt == 5:
                    if 0<=nx+deltaX[i]<19 and 0<=ny+deltaY[i]<19 and arr[nx+deltaX[i]][ny+deltaY[i]]==2:
                        break
                    if 0<=x-deltaX[i]<19 and 0<=y-deltaY[i]<19 and arr[x-deltaX[i]][y-deltaY[i]]==2:
                        break
                    return 2, x+1, y+1

                nx+=deltaX[i]
                ny+=deltaY[i]
        return FinalColor, FinalX, FinalY
    if color == 0:
        return 0, -1, -1

blackSum = whiteSum = 0
deltaY=[0, 1, 1, 1] #하 우하 우 우상
deltaX=[1, 1, 0, -1]

FinalColor=0
FinalX=FinalY=-1

for i in range(19):
    for j in range(19):
        if arr[i][j] == 1:
            FinalColor, FinalX, FinalY = count(i, j, 1)
#            print(FinalColor, FinalX, FinalY)
        elif arr[i][j] == 2:
            FinalColor, FinalX, FinalY = count(i, j, 2)
        else:
            continue

if FinalColor==0:
    print(0)
else:
    print(FinalColor, FinalX, FinalY)