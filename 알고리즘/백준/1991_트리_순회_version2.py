import sys
input = sys.stdin.readline

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    print(root.val, end = '')
    if root.left != '.':
        preorder(tree[root.left])
    if root.right != '.':
        preorder(tree[root.right])

def inorder(root):
    if root.left != '.':
        inorder(tree[root.left])
    print(root.val, end = '')
    if root.right != '.':
        inorder(tree[root.right])

def postorder(root):
    if root.left != '.':
        postorder(tree[root.left])
    if root.right != '.':
        postorder(tree[root.right])
    print(root.val, end = '')
    

n = int(input())
tree = {}
for i in range(n):
    data = list(input().strip().split())
    tree[data[0]] = Node(data[0], data[1], data[2])

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])