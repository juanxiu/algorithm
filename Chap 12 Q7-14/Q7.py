#럭키 스트레이트

n= input() #입력 데이터는 문자열임.
length = len(n)

left = 0
right = 0

# 연산자 //: 정수 몫.. %: 나머지
for i in range(length//2):  #range: 0이상 length//2 미만.
    left = int(n[i]) #정수형으로 변환.

for j in range(length//2, length): #range: length//2이상 length 미만
    right =int(n[i])

if left == right:
    print("LUCKY")
else:
    print("READY")
