A,B,C = map(int,input().split())
def custom_append(a,b,c):
    global visited,stack,result
    if (a,b,c) not in visited:
        visited.add((a,b,c))
        stack.append((a,b,c))
        if a == 0:
            result.add(c)




def move_bowl(origin,target,target_max):
    if origin+target >= target_max:
        origin = origin+target- target_max
        target = target_max
    else:
        target = origin + target
        origin = 0
    return (origin,target)
visited = set()
visited.add((0,0,C))
stack = [(0,0,C)]
result = set()
result.add(C)

while stack:
    ca,cb,cc = stack.pop()
    if ca:
        # A->B
        na,nb = move_bowl(ca,cb,B)
        custom_append(na,nb,cc)
        # A->C
        na,nc = move_bowl(ca,cc,C)
        custom_append(na,cb,nc)
    if cb:
        # B->C
        nb,nc = move_bowl(cb,cc,C)
        custom_append(ca,nb,nc)
        # B->A
        nb,na = move_bowl(cb,ca,A)
        custom_append(na,nb,cc)
    if cc:
        # C->A
        nc,na = move_bowl(cc,ca,A)
        custom_append(na,cb,nc)
        # C->B
        nc,nb = move_bowl(cc,cb,B)
        custom_append(ca,nb,nc)

result = sorted(list(result))
print(*result)