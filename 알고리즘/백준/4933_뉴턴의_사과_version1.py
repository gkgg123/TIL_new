import sys

def input():
    return sys.stdin.readline().rstrip()


def make_tree(arr):
    stack = []
    tree = {}

    for k in arr:
        if k == 'nil':
            stack.append(k)
        elif k!= 'end':
            right = stack.pop()
            left = stack.pop()
            if left != 'nil':
                tree[left] = k
            if right != 'nil':
                tree[right] = k
            stack.append(k)
        else:
            root = stack.pop()
            tree[root] = 'None'
    return tree


# 두 트리가 비어있다 혹은 두 트리의 루트가 같다.

T = int(input())

for _ in range(T):
    A_postorder = list(input().split())
    B_postorder = list(input().split())
    A_Tree = make_tree(A_postorder)
    B_Tree = make_tree(B_postorder)
    

    for key in A_Tree:
        if A_Tree[key] != B_Tree.get(key,'False'):
            print('false')
            break
    else:
        print('true')
