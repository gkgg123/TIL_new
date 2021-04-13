def find_K(k,n,reversal):
    if n == 0:
        return reversal%2
    else:
        if k >= 2**(n-1):
            return find_K(abs(2**(n-1)-k),n-1,reversal+1)
        else:
            return find_K(k,n-1,reversal)

k = int(input())
k = k-1
print(find_K(k,60,0))