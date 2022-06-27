import sys
sys.setrecursionlimit(10001)
def input():
    return sys.stdin.readline().rstrip()

def solve(st,ed):
    if st>=ed:
        return
    if st == ed-1:
        postorder.append(str(inorder[st]))
        return
    idx = st+1
    while idx<ed:
        if inorder[st]<inorder[idx]:
            break
        idx += 1
    solve(st+1,idx)
    solve(idx,ed)
    postorder.append(str(inorder[st]))
        
inorder = []
postorder = []
while True:
    try:
        node = int(input())
        inorder.append(node)
    except:
        break
solve(0,len(inorder))
print('\n'.join(postorder))