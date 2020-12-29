# FOR LOOPS EXERCISES

# # Ex. 1
# # Enter your name, save it in name variable and save in result_1 variable your name repeated 3 times (use loops)
#
# name_1 = 'Aleksandr'
# result_1  = ''
# for _ in range(3):
#     result_1 += name_1
# print(result_1)
#

# TODO: Here is your code


# Ex. 2
# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then save in result_2 variable your name repeated as many times as number_1 is
# (use loops)
# name_2 =    'Aleksandr'
# number_1 = 10
# result_2 = ''
#
# for _ in range(number_1):
#     result_2 += name_2
# print(result_2)




# Ex. 3
# Enter a random string, which includes only digits. Write code which find a sum of digits in this string and save it
# into result_3 variable

# string_number_1 = '5cdg43f562vx756'
# result_3 = 0
#
# for char in string_number_1:
#     if char.isdigit():
#         result_3 += int(char)
# print(result_3)

# Ex. 4
# Create code which sums up all even numbers between 2 and 100 (include 100) and save it in result_4 variable

result_4 = 0

for number in range(2,101, 2):
    result_4 += number

print(result_4)

