import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()


U,F = map(int,input().split())
group_dict = defaultdict(set)
user_dict = {}
for _ in range(U):
    user,*groups = input().split()
    if groups and ',' in groups[0]:
        groups = groups[0].split(',')
    groups = set(groups)
    groups.add(user)
    for group in groups:
        group_dict[group].add(user)
    user_dict[user] = set(groups)
command_list = ['','X','W','WX','R','RX','RW','RWX']

file_dict = {}
file_order = {}
for _ in range(F):
    filename,order,owner,group = input().split()
    file_dict[filename] = {
        'owner' : owner,
        'group' : group,
        'group_member' : group_dict[group],
        'order' : []
    }
    temp = set()
    for ind in range(2,-1,-1):
        temp.update(command_list[int(order[ind])])
        file_dict[filename]['order'].append(set(temp))
    file_dict[filename]['order'] = list(reversed(file_dict[filename]['order']))

Q = int(input())
result = []
for _ in range(Q):
    user,filename,query = input().split()

    if user == file_dict[filename]['owner']:
        result.append(str(int(query in file_dict[filename]['order'][0])))
    elif file_dict[filename]['group'] in user_dict[user]:
        result.append(str(int(query in file_dict[filename]['order'][1])))
    else:
        result.append(str(int(query in file_dict[filename]['order'][2])))

sys.stdout.write('\n'.join(result))