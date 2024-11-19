f = open('data.txt', 'r')
print(f.readline(), end="")
print(f.readline())
print(f.readline())

# How to write Data

write = open("write", "w")
write.write("Code with Evans, This is evansify") # This writes data once and this data file can be replaced

# How To Append a File
# write = open("write", "a")
# write.write(" This is Awesome") # This writes data once and this data file can be replaced


# Merge data from different files
for data in f:
    write.write(data)


# Reading an Image
image = open("Intasend.png", "rb")
# for i in image:
#     print(i)

# Copying the image into another file

copyImg = open("My Image.png", "wb")
for i in image:
    copyImg.write(i)