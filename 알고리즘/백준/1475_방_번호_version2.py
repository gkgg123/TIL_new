N = input()
room_number = [0]*10

for number in N:
    room_number[int(number)] += 1
a = room_number[6]+room_number[9]
b = (room_number[6]+room_number[9])//2
room_number[6],room_number[9] = b,a-b

print(max(room_number))