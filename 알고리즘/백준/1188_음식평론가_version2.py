import functools
n,m = map(int,input().split())
@functools.lru_cache()
def gdc(n,m):
    if not n%m:
        return m
    return gdc(m,n%m)

print(m-gdc(n,m))