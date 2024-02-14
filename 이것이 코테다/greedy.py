# 모험가 길드

n = int(input())

data = list(map(int, input().split())) #입력받은 공포도
data.sort() #오름차순 정렬

rslt = 0 #총 그룹의 수
cnt =0 #현재 그룹에 포함된 모험가의 수

for i in data: #공포도를 낮은 것부터 확인
    cnt+=1 #현재 그룹에 해당 모험가를 포함시키기
    if cnt >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        rslt +=1 #총 그룹 수 증가시키기
        cnt =0 #현재 그룹에 포함된 모험가의 수 초기화

print(rslt) #총 그룹의 수 출력






