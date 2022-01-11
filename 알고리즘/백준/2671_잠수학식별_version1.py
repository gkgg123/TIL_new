import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(idx,first_flag,zero_cnt,two_flag):
    if idx == N:
        if first_flag == 2 or two_flag>1:
            result = 'SUBMARINE'
            print(result)
            exit()
        return
    else:
        if first_flag == 0 and two_flag == 0:
            if input_string[idx] == 0:
                dfs(idx+1,first_flag,zero_cnt,two_flag+1)
            else:
                dfs(idx+1,first_flag+1,zero_cnt,two_flag)
        if first_flag:
            if first_flag == 1 and input_string[idx] == 0:
                dfs(idx+1,first_flag,zero_cnt+1,two_flag)
            elif first_flag == 1 and input_string[idx] == 1 and zero_cnt >=2:
                dfs(idx+1,first_flag+1,zero_cnt,two_flag)
            elif first_flag == 2 and input_string[idx] == 1:
                dfs(idx+1,first_flag,zero_cnt,two_flag)
                dfs(idx+1,1,0,0)
            elif first_flag == 2 and input_string[idx] == 0:
                dfs(idx+1,0,0,1)
        elif two_flag:
            if two_flag%2 and input_string[idx] == 1:
                dfs(idx+1,first_flag,zero_cnt,two_flag+1)  
            elif two_flag%2 ==0 and input_string[idx] == 0:
                dfs(idx+1,first_flag,zero_cnt,two_flag+1)
            elif two_flag%2 == 0 and input_string[idx] == 1:
                dfs(idx+1,1,0,0)
input_string = list(map(int,input()))
N = len(input_string)
idx = 0
result = "NOISE"
dfs(0,0,0,0)
print(result)    