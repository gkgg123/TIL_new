# 12851 숨바꼭질

N,M = map(int,input().split())
times = 0
ways = 0
prev_vistied = {N : 1}
visited = [True]*100001
if N == M:
    ways = 1
while not ways:
    new_visited = {}
    for number in prev_vistied:
        for new_number in [number-1,number+1,2*number]:
            if 0<= new_number <= 100000 and visited[new_number]:
                if new_number == M:
                    ways += prev_vistied[number]
                else:
                    if new_visited.get(new_number):
                        new_visited[new_number] += prev_vistied[number]
                    else:
                        new_visited[new_number] = prev_vistied[number]
    for visited_number in new_visited:
        visited[visited_number] = False
    prev_vistied = new_visited
    times += 1 

print(times)
print(ways)