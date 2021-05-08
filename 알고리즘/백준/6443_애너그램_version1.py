import sys

input = sys.stdin.readline

def combination(ind,len_string,combi):
    if ind == len_string:
        print(combi)
    else:
        for k in range(len_string):
            if visited[k]:
                temp = combi+string_list[k]
                if temp not in record:
                    visited[k] = False
                    record.add(temp)
                    combination(ind+1,len_string,temp)
                    visited[k] = True 



N = int(input())

for _ in range(N):
    string_list = list(input().strip())
    string_list.sort()
    len_string = len(string_list)
    visited = [True]*(len(string_list))
    record = set()
    combination(0,len_string,'')