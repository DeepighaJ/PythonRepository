# my_answer = input("What is your answer? ")
# answers = ['Yes', 'No', 'Yes', 'No', my_answer]
#
# while True:
#     print("Hello")

# greeting = "hello"
# print(greeting.upper())

# countries = []
#
# while True:
#     country = input("Enter the country: ")
#     countries.append(country)
#     print(countries)

''' dir and help methods are used in py console to see the list of methods it supports
var=[1,2,3,4]
print(dir(var))
print(help(var.count))

'''
#
# elements = ['a', 'b', 'c']
# print(elements[1])
#
# new = 'x'
# elements[1]=new
# print(elements)
#
# menu = ["pasta", "pizza", "salad"]
#
# for i, j in enumerate(menu):
#     print(f"{i}.{j}")
#

def calculate_time(h,g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)