def find_brackt():
    for ind,command in enumerate(commands):
        if command == '[':
            bracket.append((ind,1))
        elif command == ']':
            bracket.append((ind,-1))
    brind = 0
    temp = []
    while brind < len(bracket): 
        if bracket[brind][1] == 1:
            temp.append(bracket[brind][0])
        else:
            open_bracket = temp.pop()
            bracket_couple[bracket[brind][0]] = open_bracket
            bracket_couple[open_bracket] = bracket[brind][0]
        brind += 1

def go():
    global command_index,string_index,pointer
    if commands[command_index] == '-':
        arr[pointer] = arr[pointer]-1
        if arr[pointer]<0:
            arr[pointer] = 255
    elif commands[command_index] == '+':
        arr[pointer] = arr[pointer] + 1
        if arr[pointer] > 255:
            arr[pointer] = 0
    elif commands[command_index] == '<':
        pointer -= 1
        if pointer < 0:
            pointer = memorysize -1
    elif commands[command_index] == '>':
        pointer += 1
        if pointer == memorysize:
            pointer = 0
    elif commands[command_index] == '[':
        if arr[pointer] == 0:
            command_index = bracket_couple[command_index]
    elif commands[command_index] == ']':
        if arr[pointer] != 0:
            command_index = bracket_couple[command_index]
    elif commands[command_index] == '.':
        pass
    else:
        if string_index == inputsize:
            arr[pointer] = 255
        else:
            arr[pointer] = ord(strings[string_index])
            string_index += 1
    command_index += 1

T = int(input())
MAX_NUMBER = 50000000
for tc in range(T):
    memorysize,codesize,inputsize = map(int,input().split())
    pointer = 0 # 포인터가 가리키는 index
    arr = [0]*memorysize
    command_cnt = 0  # 명령 횟수
    commands = list(input())
    strings = list(input())
    command_index = 0  # 명령어의 위치
    string_index = 0
    result = 'Terminates'
    bracket = []
    bracket_couple = {}
    find_brackt()
    loop_flag = False
    loop_idx = float('inf')
    while command_cnt <= MAX_NUMBER and command_index < codesize:
        command_cnt += 1
        go()
    if command_index == codesize:
        print('Terminates')
    else:
        loop_idx = min(command_index,loop_idx)
        while command_cnt >0:
            command_cnt -= 1

        print(f'Loops {loop_idx-1} {bracket_couple[loop_idx-1]}')