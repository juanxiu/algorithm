#문자열 뒤집기

data= input()
cnt0 = 0 #전부 0으로 바꾸는 경우
cnt1 = 0 #전부 1로 바꾸는 경우

if data[0] == '0': #첫 번째 원소에 대해서 처리.
    cnt0 +=1
else:
    cnt1+=1

for i in range(1, len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] =='1': #다음 수에서 1로 바뀌는 경우
            cnt0 +=1
        else:
            cnt1 +=1

print(min(cnt0,cnt1))