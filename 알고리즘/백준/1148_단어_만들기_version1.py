import sys
from collections import Counter, defaultdict
def input():
    return sys.stdin.readline().rstrip()

def input_layer(flag):
    temp = []
    while True:
        s = input()
        if s == flag:
            break
        temp.append(s)
    return temp


words = input_layer('-')
boards = input_layer('#')


word_cnt = []

for word in words:
    word_cnt.append(Counter(word))


for board in boards:
    board_dict = Counter(board)
    word_use = defaultdict(int)
    for w in board_dict:
        word_use[w] = 0
    for word in word_cnt:

        for w in word:
            if not board_dict.get(w):
                break
            if board_dict[w] < word[w]:
                break
        else:
            for w in word:
                word_use[w] += 1
    min_ans = []
    max_ans = []
    min_val = float('inf')
    max_val = 0
    for w in word_use:
        if word_use[w] <= min_val:
            if word_use[w] == min_val:
                min_ans.append(w)
            else:
                min_ans = [w]
                min_val = word_use[w]
        
        if word_use[w] >= max_val:
            if word_use[w] == max_val:
                max_ans.append(w)
            else:
                max_val = word_use[w]
                max_ans = [w]
    min_ans.sort()
    max_ans.sort()
    print(''.join(min_ans),min_val,''.join(max_ans),max_val)


