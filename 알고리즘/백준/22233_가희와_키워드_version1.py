import sys

def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())

origin_set = set([input() for _ in range(N)])

result = []
for _ in range(M):
    input_list = list(input().split(','))

    for input_str in input_list:
        if input_str in origin_set:
            origin_set.remove(input_str)
        
    result.append(len(origin_set))

for answr in result:
    sys.stdout.write(f'{answr}\n')