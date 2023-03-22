# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 2 == 0:
#         return f(n / 2)
#     return 1 + f(n - 1)


# for n in range(1, 1001):
#     if f(n) == 12:
#         print(n)
#         break


my_list = ["huesos", "zalupa", "pidor", "junior_python_dev"]


for index in range(len(my_list)):
    print(index, my_list[index])

print()

for pair in enumerate(my_list):
    print(pair)
