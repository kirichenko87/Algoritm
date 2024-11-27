def factorial(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError
    if number < 1:
        raise "Число должно быть больше нуля"

    mult = 1
    for i in range(1, number + 1, 1):
        mult *= i
    return mult
#
#
# # 1+ n*1 = n + 1 = O(n)
#
# number = int(input("Введите неотрицательное число : "))
# factor_number = factorial(number)
#
# print(factor_number)
#
#
# def fibonacci(lenght: int) -> int:
#     num1 = 0
#     num2 = 1
#
#     for i in range(0, lenght, 1):
#         num2 += num1
#         num1 = num2 - num1
#     return num2
#
#
# number = int(input("Введите число от 0 до 20: "))
# factor = factorial(number)
#
# print(factor)
#
# number = int(input("Введите число которое больше нуля: "))
# fib = fibonacci(number)
#
# print(fib)


#  1+1+n(1+1) = 2n + 2 = n + 2 = O(n)
#
# def count_num_1(lst: list) -> int:
#     count = 0
#     for i in range(0, len(lst), 1):
#         if i == 1:
#             count += 1
#     return count
#
#
# def binar(num: int) -> list:
#     res = []
#     while num != 0:
#         div1 = num % 2
#         res.append(div1)
#         num //= 2
#     rezult = count_num_1(res)
#     return rezult
#
#
# value = int(input("Введите число: "))
# binary = binar(value)
# print(binary)
# # (1+n(1+1+1+1+1) ) + (1+n(1+1+1+ 1)) = (5n + 1) + (4n+1) = n + 1 + n + 1 = n+n = 2n = n


# def polindrom(value: int):
#     result = 0
#     value_old = value
#     while value > 0:
#         res = value % 10
#         value //= 10
#         result = result + res
#         result *= 10
#     result //= 10
#     return result == value_old

# val = int(input("Введите число: "))
# pol = polindrom(val)
# print(pol)

# 1+1+n(1+1+1+1+1+1+1+1+1+1+1)= 11n +2 = n +2 = n

def read_file(path: str):
    file = open(path, "r")
    info_txt = file.readlines()
    file.close()
    return info_txt
read = read_file("DATA.txt")
print(read)
