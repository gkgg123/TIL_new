def solution(k,room_number):
    room_dict = {}
    answer = []

    for room in room_number:
        visited = [room]
        while room in room_dict.keys():
            room = room_dict[room]
            visited.append(room)
        answer.append(room)
        for occur_room in visited:
            room_dict[occur_room] = room + 1
    return answer