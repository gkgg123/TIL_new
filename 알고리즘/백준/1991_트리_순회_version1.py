def preorder(key):
    if tree[key] == ('.','.'):
        result[0] += key
        return
    result[0] += key
    if tree[key][0] != '.':
        preorder(tree[key][0])
    if tree[key][1] != '.':
        preorder(tree[key][1])

def inorder(key):
    if tree[key] == ('.','.'):
        result[1] += key
        return
    if tree[key][0] != '.':
        inorder(tree[key][0])
    result[1] += key
    if tree[key][1] != '.':
        inorder(tree[key][1])
def postorder(key):
    if tree[key] == ('.','.'):
        result[2] += key
        return
    if tree[key][0] != '.':
        postorder(tree[key][0])
    if tree[key][1] != '.':
        postorder(tree[key][1])
    result[2] += key


tree = {}


N = int(input())
for _ in range(N):
    root,left,right = input().split()
    tree[root] = (left,right)
result = ['','','']
preorder('A')
inorder('A')
postorder('A')

for answer in result:
    print(answer)