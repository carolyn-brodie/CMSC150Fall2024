# ## 1 23 4
# list1 = [1,2, 3, 4, 5]
# for item in list1:
#     print("hi")

# print(range(5))
# print(list(range(5)))
# for item in range(11,6,-1):
#     print(item, end = " ")


for number in range(10,101,2):
    print(number, end = " ")
    
print()

for number in range(10,101):
    if number % 2 == 0:
        print(number, end = " ")
#
#
# ##loop through 10 numbers with range
# for number in range(1,11):
#     print(number, end = " ")
# print()
#
# #loop through numbers 1 through 10 with range (not 0-9)
#
#
#
# ##Second method for looping through 1 through 10
# for number in range(10):
#     print(number + 1, end = " ")