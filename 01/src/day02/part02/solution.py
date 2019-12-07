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
    for i in range(0, len(program_codes), 4):
        if program_codes[i] == 1:
            program_codes[program_codes[i+3]] = program_codes[program_codes[i+1]] + program_codes[program_codes[i+2]]
            continue
        if program_codes[i] == 2:
            program_codes[program_codes[i+3]] = program_codes[program_codes[i+1]] * program_codes[program_codes[i+2]]
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
