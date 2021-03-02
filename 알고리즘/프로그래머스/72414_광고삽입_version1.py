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
    for timeString in logs:
        start_time,end_time = map(changeSeconds, timeString.split('-'))
        time_laps[start_time] += 1
        time_laps[end_time] -= 1

    for ind in range(1,play_time+1):
        time_laps[ind] += time_laps[ind-1]
    max_times = sum(time_laps[:adv_time])
    max_start_time = 0
    current_sum_times = max_times
    for ind in range(1,play_time+1-adv_time):
        current_sum_times = current_sum_times - time_laps[ind-1] + time_laps[ind+adv_time-1]
        if current_sum_times > max_times:
            max_times = current_sum_times
            max_start_time = ind
    answer = changeString(max_start_time)
    return answer

solution("99:59:59","25:00:00",	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])