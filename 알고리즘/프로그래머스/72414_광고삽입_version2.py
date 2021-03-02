def changeSeconds(times):
    return  sum(int(x) * 60 ** i for i, x in enumerate(reversed(times.split(':'))))
def changeString(times):
    hour = times//3600
    minute = (times-hour*3600)//60
    seconds = times%60
    return "%02d:%02d:%02d"%(hour,minute,seconds)

def solution(play_time, adv_time, logs):
    answer = ''
    play_time =  changeSeconds(play_time)
    adv_time = changeSeconds(adv_time)
    time_laps = [0]*(play_time+1)
    diff = [0]*(play_time+1)
    for timeString in logs:
        start_time,end_time = map(changeSeconds, timeString.split('-'))
        diff[start_time] += 1
        diff[end_time] -= 1
    diff_count = 0
    for ind in range(1,play_time+1):
        time_laps[ind] += time_laps[ind-1] + diff_count
        diff_count += diff[ind]

    max_times = time_laps[adv_time]
    max_start_time = 0
    for ind in range(1,play_time+1-adv_time):
        if time_laps[adv_time+ind] - time_laps[ind] > max_times:
            max_times = time_laps[adv_time+ind] - time_laps[ind]
            max_start_time = ind
    answer = changeString(max_start_time)
    return answer