def solution(name):
    N = len(name)
    cnt_list = [0]*N
    for index in range(N):
        min_cnt = min(ord(name[index]) - ord('A'),ord('Z') - ord(name[index])+1)
        cnt_list[index] = min_cnt
    result = 0
    idx = 0
    while True:
        result += cnt_list[idx]
        cnt_list[idx] = 0
        if sum(cnt_list) == 0:
            break
        dx = 1
        while True:
            if idx+dx<N and cnt_list[idx+dx]:
                idx = idx + dx
                result += dx
                break
            if cnt_list[idx-dx]:
                idx = idx -dx
                if idx <0:
                    idx = N + idx
                result += dx
                break
            dx += 1
    return result

a = solution('JAN')
print(a)