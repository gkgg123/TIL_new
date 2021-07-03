import sys
input = sys.stdin.readline

N = int(input())


problem_dict = {}
re1_dict = {}

for _ in range(N):
    pb_num,l_num = map(int,input().split())
    re1_dict[(l_num,pb_num)] = 1
    problem_dict[pb_num] = l_num


M = int(input())

for _ in range(M):
    command,*arg = input().split()

    if command == 'add':
        pb_num,l_num = map(int,arg)
        problem_dict[pb_num] = l_num
        re1_dict[(l_num,pb_num)] = 1
    elif command == 'recommend':
        flag = int(arg[0])
        if flag > 0:
            keys = max(re1_dict.keys())
        else:
            keys = min(re1_dict.keys())
        print(keys[1])
    else:
        pb_num = int(arg[0])
        l_num = problem_dict[pb_num]
        del problem_dict[pb_num]
        del re1_dict[(l_num,pb_num)]