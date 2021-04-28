def solution(numbers, hand):
    answer = []
    hands_position = [(3,0),(3,2)]
    dial_position = {}
    hand = hand[0].upper()
    hand_dict = {'R':1,'L':0}
    for i in range(9):
        x = i//3
        y = i%3
        dial_position[i+1] = (x,y)
    dial_position['*'] = (3,0)
    dial_position['#'] = (3,2)
    dial_position[0] = (3,1)
    left_number = [1,4,7]
    right_number = [3,6,9]
    for k in numbers:
        if k in left_number:
            answer.append('L')
            hands_position[0] = dial_position[k]
        elif k in right_number:
            answer.append('R')
            hands_position[1] = dial_position[k]
        else:
            target_x,target_y = dial_position[k]
            left_distance = abs(target_x - hands_position[0][0]) + abs(target_y - hands_position[0][1])
            right_distance = abs(target_x - hands_position[1][0]) + abs(target_y - hands_position[1][1])
            if left_distance < right_distance:
                answer.append('L')
                hands_position[0] = (target_x,target_y)
            elif left_distance > right_distance:
                answer.append('R')
                hands_position[1] = (target_x,target_y)
            else:
                answer.append(hand)
                hands_position[hand_dict[hand]] = (target_x,target_y)

    answer = ''.join(answer)
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")