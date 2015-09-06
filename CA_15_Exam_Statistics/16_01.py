
a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1
print bin(desired)

# # Lambda Expressions
# garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
# message=filter(lambda s: s!="X",garbled)
# print message

#
# # list slicing
# garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
# nongarbled=garbled[::-2]
# print nongarbled

# Comprehending Conditionals
# threes_and_fives=[x for x in range(1,16) if x % 3==0 or x % 5==0]
# print threes_and_fives


# __author__ = 'aaronmsmith'
# squares=[x**2 for x in range(1,11)]
# print squares
# print filter(lambda x: x>30 and x<70, squares)


# languages = ["HTML", "JavaScript", "Python", "Ruby"]
# print filter(lambda s: s=="Python", languages)

#
# to_21=range(1,21)
# odds=to_21[::2]
# print odds


#
# my_list=range(1,101)
# backwards_by_tens=my_list[100:0:-10]
# print backwards_by_tens

# my_list = range(1, 11)
# backwards=my_list[::-1]
# # Add your code below!
# print backwards


# my_list = range(1, 11) # List of numbers 1 - 10
#
# # Add your code below!
# print my_list[::2]

#
# cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 == 0]
#
#
# print cubes_by_four





# doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]
#
# # Complete the following line. Use the line above for help.
# even_squares = [x**2 for x in range(1,11) if (x) % 2 == 0]
#
# print even_squares



# my_dict = {
#     "Name":"Aaron",
#     "Age":44,
#     "BDFL":True
#
# }
#
# for item in my_dict.items():
#     print item[0] + " " + str(item[1])

# my_dict = {
#     "Name":"Aaron",
#     "Age":44,
#     "BDFL":True
#
# }
#
# for key in my_dict.keys():
#     print key + " " + str(my_dict[key])

# my_dict = {
#     "Name":"Aaron",
#     "Age":44,
#     "BDFL":True
#
# }
# print my_dict.items()
# print my_dict.keys()
# print my_dict.values()