import sys

def input():
    return sys.stdin.readline().rstrip()


words = input()



N = len(words)
a,b = map(int,input().split())

words_startIdx = [-1 for i in range(len(words))]
word_length_dict = {}
st_idx = 0
for idx,word in enumerate(words):
    if word == ' ':
        word_length_dict[st_idx] = idx - st_idx
        st_idx = -1
        continue
    if st_idx == -1:
        st_idx = idx
    words_startIdx[idx] = st_idx

word_length_dict[st_idx] = N-st_idx 
    
for w in range(a,b+1):
    s = 0
    
    answer = []
    while s<N:
        answer.append(word_length_dict[s])
        next_s = s + w-1
        if next_s<N:
            if words_startIdx[next_s] == -1:
                s = next_s+1
            elif next_s+1 == N:
                break
            elif words_startIdx[next_s+1] == -1:
                s = next_s+2
            else:
                s = words_startIdx[next_s]
        else:
            break
    print(sum(answer)+len(answer)-1)
                


