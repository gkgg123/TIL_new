N = int(input())
K = int(input())
arr = list(map(int,input().split()))
arr.sort()
diff = [0]*N
for i in range(N-1):
    diff[i] = arr[i+1] - arr[i]

diff.sort()
print(sum(diff[:len(diff)-(K-1)]))
