# import os
# file = open("myData.txt", "r")

# print(file.read())

# # Write a new file
# newFile = open("filename.txt", "w")
# newFile.write("We add the content of that file")

# # Removing/deleting files
# os.remove("filename.txt",)










# Error handling and exception

# try:
#     file = open("myDataer.txt", "r")
#     print(file.read())
# except FileNotFoundError:
#     print("Oops! This file does not exist")
# finally:
#     print("It's was nice seeing you")



try:
    file = open("myData.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("This file is not found")
finally:
    print("Any Statement")





# Example 2 of Error Handling

# a = 56
# b = 0

# # print(a/b)

# try:
#     # print(a/b)
#     k = int(input("Please Enter a Number: "))
# except ZeroDivisionError:
#     print("This is not Possible")
# except ValueError:
#     print("Please enter a number")
# finally:
#     print("Thank you for using our Calculator")