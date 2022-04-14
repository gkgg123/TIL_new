import sys
sys.setrecursionlimit(10000)
def input():
    return sys.stdin.readline().rstrip()


FF,FS,SF,SS = map(int,input().split())
if FF + FS == 0:
    print(SS+min(SF,1))
elif FS == 0:
    print(FF)
else:
    print(FF + min(SF,FS) * 2 + SS  + int(FS>SF)) 