from itertools import combinations

N,K = map(int,input().split())
ord_dict = {}

for k in range(26):
    ord_dict[chr(k+97)] = k

K = K - 5
if K <0:
    print(0)
    exit(0)
else:
    origin_word = set(['a','n','t','i','c'])
    word_bit_list = list()
    combination_word = set()
    answer = 0
    for _ in range(N):
        temp = set(list(input())[4:-4]) - origin_word
        if len(temp) == 0:
            answer += 1
        elif len(temp) <=K:
            word_bit = 0
            for w in temp:
                word_bit = word_bit + 2**ord_dict[w]
            word_bit_list.append(word_bit)
            combination_word |= temp

    word_lens = len(combination_word)
    if K > word_lens:
        K = word_lens
    chk_cnt = 0
    for pick_words in combinations(combination_word,K):
        cnt = 0
        temp = 0
        for pick_word in pick_words:
            temp = temp + 2**ord_dict[pick_word]
        for word_bit in word_bit_list:
            if word_bit & temp == word_bit:
                cnt += 1

        chk_cnt = max(chk_cnt,cnt)

    print(answer + chk_cnt)