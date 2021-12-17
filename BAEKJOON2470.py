import sys
input = sys.stdin.readline
N = int(input())
Yongaeks = list(map(int, input().split()))
Yongaeks.sort()
# print(Yongaeks)
start, end = 0, N-1
results = 2e+9+1
answer=[]

while start < end:
    startTag = Yongaeks[start]
    endTag = Yongaeks[end]
    SUM = startTag + endTag
    if abs(SUM) < results:
        results = abs(SUM)
        answer = [startTag, endTag]
    
    if SUM < 0:
        start=start+1
    else:
        end=end-1
    
print(answer[0], answer[1])