#뱀

n = int(input())
k = int(input())
data = [[0] *(n+1) for _ in range(n+1)]
info =[]

#맵 정보
for _ in range(k):
    row, col = map(int, input().split())
    data[row][col] = 1 #사과가 있다면 1

#방향 회전 정보
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))


snake =[(1,1)] #좌측 상단

#처음에 오른쪽(동쪽)을 보고 있으므로 (동, 남, 서, 북): 시계방향
dx = [0, 1,0,-1] #dx는 상하
dy = [1,0,-1,0]  #dy는 좌우

def turn(dr, c):
    if c == 'L':
        dr = (dr-1)%4
    else:
        dr = (dr+1)%4

def simulate():

    time =0
    idx=0

    while True:
        x,y = snake[0]
        nx = x +dx[dr]
        ny = y +dy[dr]

        #벽에 부딪히거나 뱀 몸에 부딪힌 경우 종료.
        if 1<= nx<=n and 1<= ny<=n and (nx,ny) not in snake:
            snake.insert(0, (nx,ny)) #머리위치(0)에 이동좌표 삽입
            if data[nx][ny] == 1: #사과가 있을 경우.
                data.remove(nx,ny)
            else:
                snake.pop(1) #꼬리 제거
        else:
            break

        x,y = nx,ny
        time +=1

        if idx < l and time == info[idx][0]: #idx번째 요소의 첫 번째 요소(시간)
            dr = turn(dr, info[idx][1]) #idx번째 요소의 두 번째 요소(방향)
            idx += 1

    return time

print(simulate())



