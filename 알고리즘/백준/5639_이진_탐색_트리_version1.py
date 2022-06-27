import sys
sys.setrecursionlimit(10005)
def input():
    return sys.stdin.readline().rstrip()

def make_tree():
    tree = {root:[0,0]}
    stack = [root]
    for i in range(1,len(preorder)):
        node = preorder[i]
        parent = stack[-1]
        if node < parent:
            tree[parent][0] = node
        else:
            while stack and stack[-1]<node:
                parent = stack.pop()
            tree[parent][1] = node
        stack.append(node)
        tree[node] = [0,0]
    return tree

def postorder(node):
    if tree[node][0] != 0:
        postorder(tree[node][0])
    if tree[node][1] != 0:
        postorder(tree[node][1])
    print(node)

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

root = preorder[0]
tree = make_tree()
postorder(root)