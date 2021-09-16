import sys

def input():
    return sys.stdin.readline().rstrip()

M = int(input())
all_bit = set(list(map(str,(range(1,21)))))
set_a = set()
for _ in range(M):
    command,*arg = input().split()
    if command == 'add':
        set_a.add(arg[0])
    elif command == 'remove':
        set_a.discard(arg[0])
    elif command == 'toggle':
        if arg[0] in set_a:
            set_a.remove(arg[0])
        else:
            set_a.add(arg[0])
    elif command == 'all':
        set_a |= all_bit
    elif command == 'empty':
        set_a.clear()
    else:
        if(arg[0]) in set_a:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
