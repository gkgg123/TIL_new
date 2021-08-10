import sys
def I():
    return sys.stdin.readline().rstrip().split()
N,K = map(int,I());T = list(map(int,I()));A=L=R=B=C=0
while R<N:
    if not T[R]%2:
        C += 1
        R += 1
    elif B<K:
        if T[R]%2:
            B += 1
            R += 1
    else:
        if T[L]%2:
            B -= 1
        else:
            C -= 1
        L += 1
    A = max(A,C)
print(A)

