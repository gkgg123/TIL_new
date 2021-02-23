class Node():
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.prev = None
        self.next = None

class Tree():
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodesize = 0

    def insert(self,data):
        newNode = Node(data)
        if self.head:
            if self.nodesize == 1:
                if self.head.data > newNode.data:
                    self.tail = newNode
                    self.head.next = self.tail
                    self.tail.prev = self.head
                else:
                    smallNode = self.head
                    self.head = newNode
                    self.head.next = smallNode
                    self.tail = smallNode
                    self.tail.prev = self.head
            else:
                start = self.head
                ind = 0
                flag = False
                while True:
                    if self.nodesize != ind:
                        prevNode = start.prev
                        if start.data < newNode.data:
                            flag = True
                            if ind == 0:
                                self.head.prev = newNode
                                newNode.next = self.head
                                self.head = newNode
                            else:
                                prevNode.next = newNode
                                newNode.next = start
                                start.prev = newNode
                    else:
                        flag = True
                        newNode.prev = self.tail
                        self.tail.next = newNode
                        self.tail = newNode
                    if flag:
                        break
                            
                        
                    ind += 1
        else:
            self.head = newNode
            self.tail = newNode
        self.nodesize += 1

    def popleft(self):
        if self.nodesize:
            if self.nodesize > 1:
                start = self.head
                self.head = start.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
            self.nodesize -= 1
    def pop(self):
        if self.nodesize:
            if self.nodesize > 1:
                end = self.tail
                self.tail = end.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
            self.nodesize -= 1
    def print(self):
        if self.nodesize:
            return [self.head.data, self.tail.data]
        else:
            return ['EMPTY']

T = int(input())



for _ in range(T):
    N = int(input())
    a = Tree()
    for _ in range(N):
        command, val = input().split()
        if command == 'I':
            a.insert(int(val))
        else:
            if val == '-1':
                a.pop()
            else:
                a.popleft()
    print(*a.print())

