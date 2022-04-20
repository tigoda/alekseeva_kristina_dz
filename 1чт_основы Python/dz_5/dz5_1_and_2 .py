# def odd_nums(max_num):
#     for num in range(1, max_num + 1):
#         if num % 2 != 0:
#             yield num
#
#
# odd_num = odd_nums(15)
# print(next(odd_num))
# print(next(odd_num))
# print(next(odd_num))
# print(next(odd_num))
# print(next(odd_num))
# print(next(odd_num))
# print(next(odd_num))
# print(next(odd_num))
# print(next(odd_num))

number = (num for num in range(1, 15 + 1) if num % 2 != 0)
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
