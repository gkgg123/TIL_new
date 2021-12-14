import sys
def input():
    return sys.stdin.readline().rstrip()

def init(total_size):
    for i in range(total_size-1,0,-1):
        segment_tree[i] = segment_tree[i<<1] + segment_tree[i<<1|1]

def query(left,right):
    ans = 0

    while left<right:
        if(left&1):
            ans += segment_tree[left]
            left += 1
        if(right&1):
            right -= 1
            ans += segment_tree[right]
        left >>= 1
        right >>= 1
    return ans
T = int(input())

def update(pos,val,total_size):
    segment_tree[pos+total_size] = val
    pos = pos + total_size
    while pos >1:
        segment_tree[pos>>1] = segment_tree[pos] + segment_tree[pos^1]
        pos >>= 1
    

result = []
for _ in range(T):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    segment_tree = [0 for _ in range(2*(N+M))]
    total_size = N+M
    index_list = [0 for _ in range(N+1)]
    for idx in range(N):
        segment_tree[idx+(N+2*M)] = 1
        index_list[idx+1] = idx + M
    init(total_size)
    sub_result = []
    for idx in range(M):
        find_movie_num = arr[idx]
        find_idx = index_list[find_movie_num]
        sub_result.append(str(query(total_size,find_idx + total_size)))
        update(find_idx,0,total_size)
        update(M-1-idx,1,total_size)
        index_list[find_movie_num] = M-1-idx
    result.append(' '.join(sub_result))
sys.stdout.write('\n'.join(result))
