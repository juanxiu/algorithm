#만들 수 없는 금액

n = int(input())
data = list(map(int, input().split()))
data.sort() #오름차순 정렬

target =1  #target 변수 설정하기!!
for x in data:
    if target<x: #타킷변수가 화폐단위보다 더 클 때, 업데이트한다.
        break
    target +=x #이렇게 업데이트한 이후의 target -1까지 모두 금액을 만들 수 있다는 말이다.

print(target)

