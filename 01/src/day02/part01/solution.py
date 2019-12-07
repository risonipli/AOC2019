import copy

def get_input():
    with open('input') as f:
        return list(map(
            lambda x: int(x),
            f.read().replace('\n', '').split(',')
        ))

def program_alarm_1202(program_codes):
    program_copy = copy.copy(program_codes)
    program_copy[1] = 12
    program_copy[2] = 2
    return program_copy

def process(program_codes):
    for i in range(0, len(program_codes), 4):
        if program_codes[i] == 1:
            program_codes[program_codes[i+3]] = program_codes[program_codes[i+1]] + program_codes[program_codes[i+2]]
            continue
        if program_codes[i] == 2:
            program_codes[program_codes[i+3]] = program_codes[program_codes[i+1]] * program_codes[program_codes[i+2]]
            continue
        if program_codes[i] == 99:
                return program_codes


if __name__ == "__main__":
    assert process([1,0,0,0,99]) == [2,0,0,0,99]
    assert process([2,3,0,3,99]) == [2,3,0,6,99]
    assert process([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert process([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

    intcode_program = program_alarm_1202(get_input())
    print(intcode_program)
    print(process(intcode_program))