import sys

def input():
    return sys.stdin.readline().rstrip()


class Node:
    def __init__(self,num) -> None:
        self.next = None
        self.num = num

class LinkedList:
    def __init__(self,node):
        self.start = node
        self.end = node
    def extends(self,LL):
        if LL.isEmpty():
            return
        if self.isEmpty():
            self.start = LL.start
            self.end = LL.end
        else:
            self.end.next = LL.start
            self.end = LL.end
        LL.start = None
        LL.end = None
    def isEmpty(self):
        return self.start == None

N,M = map(int,input().split())
used = [LinkedList(Node(i)) for i in range(N+1)]
result = [i for i in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    used[y].extends(used[x])


for num in range(1,N+1):
    curLL = used[num]
    if curLL.isEmpty():
        continue
    node = curLL.start
    result[node.num] = num
    while True:
        node = node.next
        if node == None:
            break
        result[node.num] = num

print(result[1:])