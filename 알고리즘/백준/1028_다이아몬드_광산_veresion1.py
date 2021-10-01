import sys
def input():
    return sys.stdin.readline().rstrip()


R,C = map(int,input().split())

arr = [[0 for _ in range(C+1)]]

for _ in range(R):
    temp = [0]+list(map(int,list(input())))

    arr.append(temp)


right_down = [[0 for _ in range(C+2)] for _ in range(R+2)]
left_down = [[0 for _ in range(C+2)] for _ in range(R+2)]
right_up = [[0 for _ in range(C+2)] for _ in range(R+2)]
left_up = [[0 for _ in range(C+2)] for _ in range(R+2)]

for x in range(R,0,-1):
    for y in range(1,C+1):
        if arr[x][y]:
            left_down[x][y] = left_down[x+1][y-1] + 1
            right_down[x][y] = right_down[x+1][y+1] + 1


for x in range(1,R+1):
    for y in range(1,C+1):
        if arr[x][y]:
            right_up[x][y] = right_up[x-1][y+1] + 1
            left_up[x][y] = left_up[x-1][y-1] + 1


result = 0
for x in range(1,R+1):
    for y in range(1,C+1):
        max_size = min(right_down[x][y],right_up[x][y])
        if max_size<=result:
            continue
        for gap in range(max_size,0,-1):
            if y + gap*2-2 >C:
                continue
            if gap<result:
                continue
            cur_size = min(left_up[x][y + gap*2-2],left_down[x][y + gap*2-2])
            if cur_size>=gap:
                if result < gap:
                    result = gap
                break

print(result)


