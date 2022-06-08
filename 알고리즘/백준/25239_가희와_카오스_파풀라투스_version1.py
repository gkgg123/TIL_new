import sys

def input():
    return sys.stdin.readline().rstrip()

def convert(t):
    h,m = t.split(':')
    return 60*int(h) + int(m)
def check(t):
    t = t%720
    t = t//60
    return t//2
ST = input()

S_Time = convert(ST)
area = list(map(int,input().split()))
area_visitd = [0 for _ in range(6)]
L = int(input())
time_dict = {
    '10MIN' : 10,
    '30MIN' : 30,
    '50MIN' : 50,
    '2HOUR' : 120,
    '4HOUR' : 240,
    '9HOUR' : 540
}
for _ in range(L):
    x, commands = input().split()
    x_s,x_T = x.split('.')
    if int(x_s) >= 60:
        break
    if commands == '^':
        area_number = check(S_Time)
        area_visitd[area_number] = 1
    else:
        spend_time = time_dict[commands]
        S_Time += spend_time
    if area_visitd.count(0) == 0:
        break
answer = 0
for ind in range(6):
    if not area_visitd[ind]:
        answer += area[ind]

answer = min(answer,100)
print(answer)