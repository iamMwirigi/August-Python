# import os

a = 10
print(a)

file = open('myData.txt', '')
print(file)


# writeDoc = open("myData.txt","a" )
# writeDoc.write("\n This is a write test, \n Hello world")


# newDoc = open("NewDoc.txt", "w")
# newDoc.write("This is  a new document that we have created, Edited Text")

# os.remove("NewDoc.txt")



















try:
    file = open('myData.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print("File Not Found")
finally:
    print("This is Awesome")