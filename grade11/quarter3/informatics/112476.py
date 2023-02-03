line = input()
used_symbols = []
new_line = ''

for symb in line:
    if symb not in used_symbols:
        new_line += symb
        used_symbols += symb

print(new_line)