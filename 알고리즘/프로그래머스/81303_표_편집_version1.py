import heapq
def solution(n, k, cmds):
    answer = ''
    def inverse(num):
        return -num
    max_heap = list(map(inverse,range(k)))
    min_heap = list(range(k,n))
    deleted = ['O' for _ in range(n)]
    deleted_stack = []
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)
    for cmd in cmds:
        command = cmd.split()
        if len(command)>1:
            num = command[1]
            command = command[0]
            num = int(num)
            if command == 'D':
                for _ in range(num):
                    heapq.heappush(max_heap,-heapq.heappop(min_heap))
            else:
                for _ in range(num):
                    heapq.heappush(min_heap,-heapq.heappop(max_heap))
        else:
            command = command[0]
            if command == 'C':
                delete_num = heapq.heappop(min_heap)
                deleted_stack.append(delete_num)
                deleted[delete_num] = 'X'
                if len(min_heap) == 0:
                    heapq.heappush(min_heap,-heapq.heappop(max_heap))
            else:
                restore_num = deleted_stack.pop()
                deleted[restore_num] = 'O'
                if min_heap[0] > restore_num:
                    heapq.heappush(max_heap,-restore_num)
                else:
                    heapq.heappush(min_heap,restore_num)
    answer = ''.join(deleted)
    return answer



solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])