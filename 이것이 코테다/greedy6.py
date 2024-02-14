#무지의 먹방 라이브- 힙을 사용하여 우선순위 큐를 구현할 것.

import heapq
def solution(food_times, k):
    #전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <=k:
        return -1

    #시간이 작은 음식부터 뺴야 하므로 우선순위 큐를 이용
    q =[]
    for i in range(len(food_times)):
        #튜플(음식 시간, 음시 번호) 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_val =0 #먹기 위해 사용한 시간
    pre =0 #직전에 다 먹은 음식 시간
    length = len(food_times) #남은 음식의 개수

    while sum_val + ((q[0][0] - pre)*length)<=k:
        now = heapq.heappop(q)[0]
        sum_val += (now - pre) * length
        length -=1 #다 먹은 음식 제외
        pre = now #이전 음식 시간 재설정


    rslt = sorted(q, key = lambda x: x[1]) #음식 번호 기준으로 정렬
    return rslt[(k - sum_val) % length][1]










