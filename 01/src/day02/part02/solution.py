import copy

def get_input():
    with open('input') as f:
        return list(map(
            lambda x: int(x),
            f.read().replace('\n', '').split(',')
        ))

def set_inputs(noun, verb, program_codes):
    program_copy = copy.copy(program_codes)
    program_copy[1] = noun
    program_copy[2] = verb
    return program_copy

def execute(program_codes):
    skip_step = 0
    for i in range(len(program_codes)):
        if skip_step > 0:
            skip_step -= 1
            continue
        if program_codes[i] == 1:
            program_codes[program_codes[i+3]] = program_codes[program_codes[i+1]] + program_codes[program_codes[i+2]]
            skip_step = 3
            continue
        if program_codes[i] == 2:
            program_codes[program_codes[i+3]] = program_codes[program_codes[i+1]] * program_codes[program_codes[i+2]]
            skip_step = 3
            continue
        if program_codes[i] == 99:
                return program_codes[0]

def process(program_codes):
    for noun in range (0, 99):
        for verb in range(0, 99):
            codes = set_inputs(noun, verb, program_codes)

            if execute(codes) == 19690720:
                return 100 * noun + verb

if __name__ == "__main__":
    codes = get_input()
    print (process(codes))
