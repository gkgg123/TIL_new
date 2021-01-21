# 이모티콘 S
# 모두복사
# 클립보드 모두 붙이기
def bfs():
    global S
    stack = [(1,0,0)]

    visited = []
    while stack:
        emo_cnt,clip_cnt,second = stack.pop(0)
        if (emo_cnt,clip_cnt) in visited:
           continue 
        visited.append((emo_cnt,clip_cnt))
        if emo_cnt == S:
            break
        stack.append((emo_cnt,emo_cnt,second+1))
        if emo_cnt and clip_cnt:
            stack.append((emo_cnt+clip_cnt,clip_cnt,second+1))
        if emo_cnt > 2:
            stack.append((emo_cnt-1,clip_cnt,second+1))

    return second


S = int(input())


print(bfs())