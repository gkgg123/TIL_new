import sys


class Node():
    def __init__(self,key=None,data=None):
        self.key = key
        self.data = data
        self.depth = 0
        self.child_node = {}
class Trie():
    def __init__(self):
        self.rootnode = Node()
    
    def insert(self,arr):
        cur_node = self.rootnode

        for node in arr:
            if node not in cur_node.child_node.keys():
                cur_node.child_node[node] = Node(node)
            cur_node.child_node[node].depth = cur_node.depth+1
            cur_node = cur_node.child_node[node]
        cur_node.data = 'END'
    def print(self):
        cur_node = self.rootnode
        stack = sorted(cur_node.child_node.values(),key= lambda x : (x.key),reverse=True)
        result = ''
        while stack:
            node = stack.pop()

            current_depth = node.depth
            result = '--'*(current_depth-1)+node.key
            print(result)
            if node.data == None:
                child_node = sorted(node.child_node.values(),key= lambda x : (x.key),reverse=True)
                stack.extend(child_node)

input = sys.stdin.readline
N = int(input())
trie = Trie()
for _ in range(N):
    N,*arr = input().split()
    N = int(N)
    trie.insert(arr)

trie.print()