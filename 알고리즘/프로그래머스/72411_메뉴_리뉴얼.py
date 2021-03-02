from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    orders = list(map(sorted,orders))
    for course_cnt in course:
        temp = []
        for order in orders:
            temp += combinations(order,course_cnt)
 
        dict_item = Counter(temp)
        if dict_item:
            max_value = max(dict_item.values())
            max_dict = dict_item.most_common()
            if max_value > 1:
                for key,value in max_dict:
                    if value < max_value:
                        break
                    else:
                        answer.append(''.join(key))
    answer.sort()
    return answer


solution(["XYZ", "XWY", "WXA"],[2,3,4])