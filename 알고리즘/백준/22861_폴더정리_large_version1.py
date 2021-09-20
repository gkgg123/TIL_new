import sys
from collections import defaultdict,Counter
def input():
    return sys.stdin.readline().rstrip()


def dfs(name):
    global result
    temp = Counter()
    for files in folder_dict[name]['file']:
        if files not in temp:
            temp[files] = 0
        temp[files] += 1
    
    for folder in folder_dict[name]['folder']:
        temp += dfs(folder)
    result[name] = [len(temp),sum(temp.values())]
    return temp

N, M = map(int,input().split())

folder_dict = {'main':{'file' : defaultdict(int), 'folder' : []}}
parent_dict = {}
for _ in range(N+M):
    uppper,lower,isFolder = input().split()
    if uppper not in folder_dict:
        folder_dict[uppper] = {'file' : defaultdict(int), 'folder' : []}
    if isFolder == '1':
        folder_dict[uppper]['folder'].append(lower)
        parent_dict[lower] = uppper
        if lower not in folder_dict:
            folder_dict[lower] = {'file' : defaultdict(int), 'folder' : []}
    else:
        folder_dict[uppper]['file'][lower] += 1



K = int(input())

for _ in range(K):
    before,after = input().split()
    before_folder = before.split('/')[-1]
    after_folder = after.split('/')[-1]
    before_items = folder_dict[before_folder]
    before_parent = parent_dict[before_folder]
    del parent_dict[before_folder]
    del folder_dict[before_folder]
    folder_dict[before_parent]['folder'].remove(before_folder)
    for key in before_items:
        if key == 'file':
            for name in before_items[key]:
                if name not in folder_dict[after_folder][key]:
                    folder_dict[after_folder][key][name] += 1
        else:
            for name in before_items[key]:
                folder_dict[after_folder][key].append(name)
                parent_dict[name] = after_folder


result = {}
dfs('main')

Q = int(input())

for _ in range(Q):
    last_folder = input().split('/')[-1]
    print(*result[last_folder])