import itertools
from pprint import pprint


COMMANDS_DICT = {
    '1': '+2',
    '2': '*2',
    '3': '*3'
}

FIRST_NUMB = 2
LAST_NUMB = 28
REQUIRED_NUMB = 6
FORBIDDEN_NUMB = 0


def verify_path():
    pass


def execute_program(program: str):
    global COMMANDS_DICT
    global FIRST_NUMB
    path = [FIRST_NUMB]
    for command in program:
        next_number = int(eval(str(path[-1]) + COMMANDS_DICT[command]))
        path.append(next_number)
        if next_number >= LAST_NUMB:
            break
    return path


def main():
    combinations = []
    for command_length in range(1, 15):
        current_combinations = list(itertools.product('123', repeat=command_length))


if __name__ == '__main__':
    # main()
    print(execute_program('112323232321231231231223131231232312313'))
