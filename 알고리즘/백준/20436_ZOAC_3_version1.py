import sys

def input():
    return sys.stdin.readline().rstrip()

def distance(a,b):
    x1,y1 = keyboard[a]
    x2,y2 = keyboard[b]
    return  abs(x1-x2) + abs(y1-y2)
def dfs(idx,cnt):
    global L,R
    if idx == len(word):
        return cnt
    if word[idx] in mo:
        dis = distance(word[idx],R)
        R = word[idx]
        return dfs(idx+1,cnt+dis)
    else:
        dis = distance(word[idx],L)
        L = word[idx]
        return dfs(idx+1,cnt+dis)

keyboard = {
    'q' : [0,0],
    'w' : [0,1],
    'e' : [0,2],
    'r' : [0,3],
    't' : [0,4],
    'y' : [0,5],
    'u' : [0,6],
    'i' : [0,7],
    'o' : [0,8],
    'p' : [0,9],
    'a' : [1,0],
    's' : [1,1],
    'd' : [1,2],
    'f' : [1,3],
    'g' : [1,4],
    'h' : [1,5],
    'j' : [1,6],
    'k' : [1,7],
    'l' : [1,8],
    'z' : [2,0],
    'x' : [2,1],
    'c' : [2,2],
    'v' : [2,3],
    'b' : [2,4],
    'n' : [2,5],
    'm' : [2,6]
}
mo = set('yuiophjklbnm')
L,R = input().split()
result = float('inf')
word = list(input())

print(dfs(0,0)+len(word))