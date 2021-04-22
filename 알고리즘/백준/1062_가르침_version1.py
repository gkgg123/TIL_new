from itertools import combinations

N,K = map(int,input().split())
ord_dict = {}
if K <5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()
else:
    # 2**승으로 만들어 주기 위한 곳
    for k in range(26):
        ord_dict[chr(k+97)] = k

    K = K - 5
    comb_bits = 0
    # 무조건 있는 애들을 기본적으로 comb_bits로 만들어준다.
    for k in ['a','n','t','i','c']:
        comb_bits = comb_bits + 2**ord_dict[k]
    word_list = []


    for _ in range(N):
        # 앞뒤 고정 부분은 필요없으니 자른다.
        temp = set(list(input())[4:-4])
        word_list.append(temp)
    # 고정적으로 잇는 부분 제외하고 나머지를 뽑는다.
    combi_word = set(ord_dict.keys()) - set(['a','n','t','i','c'])
    result = 0
    for pick_words in combinations(combi_word,K):
        check_bits = comb_bits
        for pick_word in pick_words:
            # OR 연산을 해줘서 BIT 형식으로 만들어준다.
            check_bits = check_bits | 1<< ord_dict[pick_word]

        word_cnt = 0
        for word in word_list:
            for wo in word:
                # 만약에 AND 연산을 했는데 False가 나오면 그만둔다.
                if not (check_bits & 1<<ord_dict[wo]):
                    break
            else:
                word_cnt += 1
        result = max(word_cnt,result)
                
    print(result)