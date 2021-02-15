# 매출하락 최소화

def solution(sales,links):
    N = len(sales)
    sales = [0]+sales
    tree = [[] for _ in range(N+1)]
    for parents,child in links:
        tree[parents].append(child)
    loss_sale = [[0]*2 for _ in range(N+1)]
    # loss_sale[x][0] = x번 노드가 참석하는 경우
    # loss_sale[x][1] = x번 노드가 불참석하는 경우
    def dfs(node):
        nonlocal loss_sale,tree,sales
        if not tree[node]:
            loss_sale[node][0] = sales[node]
            return

        for child_node in tree[node]:
            dfs(child_node)
            loss_sale[node][0] += min(loss_sale[child_node][0],loss_sale[child_node][1])

        
        loss_sale[node][0] += sales[node]
        atamp_loss = float('inf')
        for child_node in tree[node]:
            atamp_loss = min(loss_sale[child_node][0]-loss_sale[child_node][1],atamp_loss)
        loss_sale[node][1] = max(0,atamp_loss) + loss_sale[node][0] - sales[node]
    dfs(1)
    return min(loss_sale[1])






if __name__ == '__main__':
    input_list = [[[14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]],
    [[5, 6, 5, 3, 4],[[2,3], [1,4], [2,5], [1,2]]],
    [[5, 6, 5, 1, 4],[[2,3], [1,4], [2,5], [1,2]]],
    [[10, 10, 1, 1],[[3,2], [4,3], [1,4]]]
    ]
    output_list = [44,6,5,2]
    for ind,val in enumerate(input_list):
        sales,links = val
        answer = solution(sales,links)
        if output_list[ind] != answer:
            print(f'{ind}번 입력에 대하여 틀렸습니다.')
            print(f'correct_answer : {output_list[ind]}')
            print(f'your answer : {answer}')
        else:
            print(f'{ind}번 입력에 대하여 맞았습니다.')