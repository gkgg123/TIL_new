import sys

def input():
    return sys.stdin.readline().rstrip()


N,K = map(int,input().split())



print(((N-1)*N//2)*1/K)