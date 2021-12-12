import sys

def input():
    return sys.stdin.readline().rstrip()

def check():
    right = len(palidrome)-1
    left = 0
    if len(set(palidrome)) == 1:
        return -1
    for mid in range((right-left)//2):
        if palidrome[left+mid] != palidrome[right-mid]:
            return len(palidrome)
    
    return len(palidrome)-1

palidrome = input()
print(check())