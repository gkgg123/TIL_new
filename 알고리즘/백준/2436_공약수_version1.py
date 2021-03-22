def gcd(A,B):
    if not A%B:
        return B
    return gcd(B,A%B)


N, M = map(int,input().split())
ab = M//N
list_a = []
last_N = int(ab**(1/2))
for number_a in range(last_N,0,-1):
    if not ab%number_a:
        number_b = ab//number_a
        if gcd(number_a,number_b) == 1:
            list_a.extend([number_a,number_b])
            break
print(*[ i*N for i in list_a])