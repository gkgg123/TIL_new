import sys
sys.setrecursionlimit(1000000)
def solution(k, room_number):
    assign_room_keys = {}

    def find(room_number):
        nonlocal assign_room_keys
        if not assign_room_keys.get(room_number):
            return room_number
        else:
            assign_room_keys[room_number] = find(assign_room_keys[room_number])
            return assign_room_keys[room_number]
    
    answer = []
    for room_number in room_number:
        find_roomnumber = find(room_number)
        answer.append(find_roomnumber)
        assign_room_keys[find_roomnumber] = find(find_roomnumber+1)
    
    return answer

solution(10,[1,3,4,1,3,1])