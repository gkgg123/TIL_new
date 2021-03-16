from datetime import datetime
import time
import math

def check(times,li):
    cnt = 0
    start = times
    end = times + 1000
    for ot_st,ot_en in li:
        if ot_en >= start and ot_st <end:
            cnt += 1
    return cnt

def solution(lines):
    answer = 0
    time_list = []
    standard_time = "2016-09-15 00:00:00.000"
    standard_time_stamp = time.mktime(datetime.strptime(standard_time,'%Y-%m-%d %H:%M:%S.%f').timetuple())
    for line in lines:
        input_strip = line.split(' ')
        times = ' '.join(input_strip[:2])
        time_range = float(input_strip[-1][:-1])
        timestamp = time.mktime(datetime.strptime(times,'%Y-%m-%d %H:%M:%S.%f').timetuple())
        timestamp = timestamp + int(input_strip[1].split('.')[1])/1000
        end_time = round(timestamp - standard_time_stamp,3)
        start_time = round(end_time - time_range,3)
        time_list.append((start_time*1000+1,end_time*1000))
    for st,en in time_list:
        answer = max(answer,check(st,time_list),check(en,time_list))

    return answer




if __name__ == '__main__':
    input_list = [["2016-09-15 00:00:00.000 3s"],
    ["2016-09-15 23:59:59.999 0.001s"],
    ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"],
    ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"],
    ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"],
    ["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]]
    output_list = [1,1,1,2,7,1]

    for i in range(len(input_list)):
        answer = solution(input_list[i])
        if answer == output_list[i]:
            print('정답입니다.')
        else:
            print(f'올바른 정답 :{output_list[i]}')
            print(f'출력된 정답 : {answer}')

            print('오답입니다')
