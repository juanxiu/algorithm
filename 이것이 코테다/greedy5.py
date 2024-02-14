#볼링공 고르기

n,m = map(int,input().split())
data = list(map(int, input().split()))
data.sort()

cnt =0

for i in range(0,len(data)-1):
    for j in range(i+1, len(data)): #인덱스를 i+1까지 해야지!
        if data[i] == data[j]:
            continue
        else:
            cnt+=1

print(cnt)


