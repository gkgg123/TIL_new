import sys
input = sys.stdin.readline
def permutation(ind,C,string_list,particle_order):
    global result
    if ind == C:
        if len(string_list)>0:
            result.add(''.join(string_list))
        else:
            result.add('EMPTY')
        return
    else:
        for i in range(1,N+1):
            command_order = particle_order[i]
            if command_order >= len(order_list[i]):
                continue
            else: 
                if not visited[i][command_order]:
                    order_num = order_list[i][command_order]
                    new_stringlist = string_list[:]
                    check_error = False
                    for order in card_command[order_num]:
                        if order[0] == 'ADD':
                            new_stringlist.append(order[1])
                        else:
                            remove_index = int(order[1])
                            if len(new_stringlist) > remove_index:
                                new_stringlist.pop(remove_index)
                            else:
                                check_error = True
                                break
                    if check_error:
                        result.add('ERROR')
                        continue
                    else:
                        visited[i][command_order] = True
                        particle_order[i] += 1
                        permutation(ind+1,C,new_stringlist,particle_order)
                        visited[i][command_order] = False
                        particle_order[i] -= 1


N,C = map(int,input().split())

order_list = [[] for _ in range(N+1)]

for ind in range(1,N+1):
    input_list = list(map(int,input().split()))
    order_list[ind] = input_list[1:]



card_command = [[] for _ in range(C+1)]


for ind in range(1,C+1):
    commands = list(input().rstrip().split(','))
    temp = []
    for command in commands:
        new_command = list(command.split(' '))
        temp.append(new_command)
    card_command[ind] = temp

result = set()
visited = [[False for _ in range(len(order_list[ind]))] for ind in range(N+1)]
particle_order = [0 for _ in range(N+1)]
permutation(0,C,[],particle_order)
result = list(result)
result.sort()
for i in range(len(result)):
    sys.stdout.write(result[i]+'\n')