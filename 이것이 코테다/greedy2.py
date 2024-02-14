#곱하기 혹은 더하기

data = input()

rslt = int(data[0]) #첫 번째 요소를 먼저 대입해주기.


for i in range(1,len(data)):
    num = int(data[i]) #입력값이 분리되지 않았다면, 요소별로 나누어 생각하기.
    if num <=1 or rslt <=1: #num과 rslt 구분하기.
        rslt +=num #두 수 중에서 하나라도 0 혹은 1인 경우 더하기 수행.
    else:
        rslt *=num

print(rslt)
