from sys import exit


n_input = input()
n = int(n_input)

def bochka():
    print(n, 'bochka')
    exit()
def bochki():
    print(n, 'bochki')
    exit()
def bochek():
    print(n, 'bochek')
    exit()

if len(n_input) == 1:
    if n == 1:
        bochka()
    elif 2 <= n <= 4:
        bochki()
    elif 5 <= n <= 9:
        bochek()
elif len(n_input) >= 2:
    if 10 <= int(n_input[-2:]) <= 20:
        bochek()
    elif int(n_input[-1:]) == 1:
        bochka()
    elif 2 <= int(n_input[-1:]) <= 4:
        bochki()
    elif 5 <= int(n_input[-1:]) <= 9:
        bochek()