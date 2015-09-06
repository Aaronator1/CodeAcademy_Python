__author__ = 'aaronmsmith'
__author__ = 'aaronmsmith'

with open("text.txt", "w") as textfile:
	textfile.write("Success!")



# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()


# Try to read from the file
print read_file.read()
read_file.close()




my_file=open("output.txt","r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

#
# f=open("/users/aaronmsmith/pycharmprojects/output.txt","r+")
# print f.readline()
# print f.readline()
# print f.readline()
# f.close()



my_file=open("output.txt","r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

#
# f=open("/users/aaronmsmith/pycharmprojects/output.txt","r+")
# print f.readline()
# print f.readline()
# print f.readline()
# f.close()
