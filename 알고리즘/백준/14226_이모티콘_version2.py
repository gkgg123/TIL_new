


S = int(input())

Set_emo_clip = set()
Set_emo_clip.add((1,0))
flag = False
time = 0
while True:
    time += 1
    temp_set = set()
    for emo_cnt,clip_cnt in Set_emo_clip:
        if (emo_cnt,emo_cnt) not in Set_emo_clip:
            temp_set.add((emo_cnt,emo_cnt))
        if (emo_cnt+clip_cnt,clip_cnt) not in Set_emo_clip:
            temp_set.add((emo_cnt+clip_cnt,clip_cnt))
            if emo_cnt+clip_cnt == S:
                flag = True
                break
        if emo_cnt > 0 and (emo_cnt-1,clip_cnt) not in Set_emo_clip:
            temp_set.add((emo_cnt-1,clip_cnt))
            if emo_cnt-1 == S:
                flag = True
                break
    if flag:
        break
    Set_emo_clip = Set_emo_clip | temp_set
print(time)