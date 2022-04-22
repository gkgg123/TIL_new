import sys

def input():
    return sys.stdin.readline().rstrip()


N,K = map(int,input().split())
arr = list(map(int,input().split()))
multitap = set()

answer = 0
for i in range(K):
    cur_num = arr[i]
    if cur_num in multitap or len(multitap) <N:
        multitap.add(cur_num)
    else:
        remove_num_list = []
        for inner_num in multitap:
            val = float('inf')
            for next_ind in range(i+1,K):
                if arr[next_ind] == inner_num:
                    val = next_ind
                    break
            remove_num_list.append((val,inner_num))

        remove_num_list.sort()
        _,remove_num = remove_num_list.pop()
        multitap.remove(remove_num)
        multitap.add(cur_num)
        answer += 1
print(answer)

        


