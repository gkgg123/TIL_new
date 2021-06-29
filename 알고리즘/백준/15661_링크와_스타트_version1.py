    import sys
    from itertools import combinations
    def input():
        return sys.stdin.readline().rstrip()


    N = int(input())


    arr = [list(map(int,input().split())) for _ in range(N)]
    row = [sum(i) for i in arr]
    col = [sum(i) for i in zip(*arr)]
    new_arr = [i+ j for i, j in zip(row, col)]
    total_sum = sum(new_arr)//2
    result = float('inf')
    for num in range(1,N//2+1):
        for combi in combinations(new_arr,num):
            result = min(result,abs(total_sum-sum(combi)))
            if result == 0:
                break
        if result == 0:
            break
    print(result)
