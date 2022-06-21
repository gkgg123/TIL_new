import sys
def input():
    return sys.stdin.readline().rstrip()
def next_lines(lines,shift):
    for i in range(len(lines)):
        lines.append(lines[i] + ' ' + lines[i])
    for i in range(shift):
        lines[i] = ' '*shift + lines[i] + ' '*shift


def sol(height):
    lines = ['  *  ',
            ' * * ',
            '*****']
    i = 0
    while height>3:
        next_lines(lines,3*(2**i))
        height /=2
        i += 1
    sys.stdout.write('\n'.join(lines)+'\n')

N = int(input())

sol(N)