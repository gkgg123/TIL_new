import sys
sys.setrecursionlimit(10**5)
def input():
    return sys.stdin.readline().rstrip()

def preorder(s,e,ps,pe):
    if(s>e) or (ps>pe):
        return
    rootindex = number_index[postorder[pe]]
    leftSize = rootindex - s
    print(inorder[rootindex], end=' ')
    preorder(s,rootindex-1,ps,ps+leftSize-1)
    preorder(rootindex+1,e,ps+leftSize,pe-1)
N = int(input())
# left->root->right
inorder = list(map(int,input().split()))
number_index = {num:ind for ind,num in enumerate(inorder)}
# left->right->root
postorder = list(map(int,input().split()))
preorder(0,N-1,0,N-1)