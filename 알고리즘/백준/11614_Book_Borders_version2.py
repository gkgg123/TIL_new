import sys

def input():
    return sys.stdin.readline().rstrip()


words = input()



N = len(words)
a,b = map(int,input().split())

words_startIdx = [-1 for i in range(1000000)]
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
    
    cnt = 0
    while s<N:
        while s<N and words_startIdx[s] == -1:
            s += 1
        s = words_startIdx[s]
        cnt += word_length_dict[s]
        s = s + w
        cnt += 1
    print(cnt-1)
                


