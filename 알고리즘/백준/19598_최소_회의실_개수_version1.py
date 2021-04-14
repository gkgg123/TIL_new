import heapq
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort()
# 끝나는 시간들을 저장해놓는 배열
end_time_list = []
for start_time,end_time in arr:
    if end_time_list:
        # 가장 빨리 끝나는 시간보다, 시작시간이 더 큰 경우, 회의실을 대체해서 쓸수 있다.
        if end_time_list[0] <= start_time:
            heapq.heappop(end_time_list)
        # 그리고 회의실에 새 끝나는 시간을 넣어준다.
        heapq.heappush(end_time_list,end_time)
    else:
        heapq.heappush(end_time_list,end_time)
print(len(end_time_list))