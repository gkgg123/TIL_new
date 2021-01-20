# nh7881님 코드 분석

def find_leafs(index,child_nodes):
    # index가 -1이라는 것은 root_node가 remove_node인 경우이니, 그때에는 0을 반환을 해준다.
    if index == -1:
        return 0
    # child_node의 길이가 0인것은 child_Node가 없는 것이므로, leaf_node이다 그러므로 1을 반환해준다.
    if len(child_nodes[index]) == 0:
        return 1
    result = 0
    # 현재 노드인 index의 child_node를 가져와서, 재귀를 실행시켜준다.
    for child_node in child_nodes[index]:
        result += find_leafs(child_node,child_nodes)
    return result



N = int(input())
graph  = list(map(int,input().split()))
# 최상위 노드를 찾아주기 위함이다. 초기값은 node에 존재하지 않는 값으로 해준다.
root_node = -1
remove_node = int(input())
child_nodes = {i:[] for i in range(N)}

for ind in range(N):
    # 우리는 leaf_node를 찾을것이고, 해당 index에 부모 node로 들어온 
    # input값을 반대로 바꿔주는 과정이 필요하다.
    # 만약에 지우는 node와 index가 같으면 굳이 parent을 찾아 child를 넣어주는 과정이 필요없다.
    # 그래서 continue로 넘어가준다.
    # 또한 유일하게 부모가 없는 root_node는 따로 구분을 해준다. if문의 순서가 remove_node가 먼저 앞으로
    # 오는 이유는 remove_node가 root_node일수 있기 때문이다. 이럴때를 구분해주기 위해, remove_node인지 판별하는게 먼저온다.
    # 그외에는 전부 parent_node를 기준으로 child를 추가해주는 방식으로 해준다.
    if remove_node == ind:
        continue
    if graph[ind] == -1:
        root_node = ind
        continue
    child_nodes[graph[ind]].append(ind)

# root_node를 기점으로 leaf_node를 찾는 재귀함수를 실행시켜준다.
print(find_leafs(root_node,child_nodes))