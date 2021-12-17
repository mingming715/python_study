import sys
input = sys.stdin.readline

word = list(input().rstrip())
i=0

while i < len(word):
    if word[i]=='<': #열린 괄호를 만날 경우
        while 1:
            i=i+1
            if(word[i]=='>'):
                break
        i=i+1
    elif word[i].isalnum():
        startRev = i
        tmp = []
        while i<len(word) and word[i].isalnum():
            tmp.append(word[i])
            i=i+1
        tmp.reverse()
        word[startRev:i] = tmp

    else:
        i=i+1

print("".join(word))