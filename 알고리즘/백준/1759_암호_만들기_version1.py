# 1759 암호 만들기
def check(input_val,vowel):
    
    check_list = [0,0]
    for val in input_val:
        if val in vowel:
            check_list[0] += 1
        else:
            check_list[1] += 1

    if check_list[0] >= 1 and check_list[1] >= 2:
        return True
    else:
        return False 




def dfs(cnt,ind,result):
    global vowel
    if ind == C:
        if cnt == L and check(result,vowel):
            total.append(result)
            return
    else:
        dfs(cnt+1,ind+1,result+input_list[ind])
        dfs(cnt,ind+1,result)




L,C = map(int,input().split())
vowel = 'aeiou'
input_list = list(input().split())
input_list.sort()

total = list()
dfs(0,0,'')
for val in total:
    print(val)