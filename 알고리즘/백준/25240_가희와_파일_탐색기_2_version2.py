import sys

def input():
    return sys.stdin.readline().rstrip()
U,F = map(int,input().split())
user_dict = {}
for _ in range(U):
    user,*groups = input().split()
    if groups and ',' in groups[0]:
        groups = groups[0].split(',')
    groups = set(groups)
    groups.add(user)
    user_dict[user] = groups

command_list = ['','X','W','WX','R','RX','RW','RWX']
file_dict = {}
for _ in range(F):
    filename,order,owner,group = input().split()
    file_dict[filename] = [order,owner,group]


Q = int(input())
result = []
querys = [input().split() for _ in range(Q)]
for user,filename,query in querys:
    possilbe = set()
    orders = file_dict[filename][0]
    if user == file_dict[filename][1]:
        for ind in range(3):
            possilbe.update(command_list[int(orders[ind])])
    elif file_dict[filename][2] in user_dict[user]:
        for ind in range(1,3):
            possilbe.update(command_list[int(orders[ind])])
    else:
        possilbe.update(command_list[int(orders[2])])

    if query in possilbe:
        result.append('1')
    else:
        result.append('0')

sys.stdout.write('\n'.join(result))