import sys
def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())

route = list(map(int,input().split()))
cnt = [0 for _ in range(N+1)]
for ind in range(M-1):
    prev_city, next_city = route[ind], route[ind+1]
    if next_city < prev_city:
        prev_city,next_city = next_city,prev_city
    cnt[next_city] -= 1
    cnt[prev_city] += 1
result = 0
for city in range(1,N):
    cnt[city] += cnt[city-1]
    ticket,ic_ticket, ic_card = map(int,input().split())
    ticket_pay = ticket* cnt[city]
    ic_pay = ic_ticket * cnt[city] + ic_card
    if ic_pay > ticket_pay:
        result += ticket_pay
    else:
        result += ic_pay
print(result)