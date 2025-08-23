fileData = input("Enter text to write to the file: ")
try:
    file1 = open('output.txt', 'w')
    file1.write(fileData)
    file1.close()
except: 
    print("Write failed!")
finally:
    print("Data successfully written to output.txt.")

fileAppend = input("Enter additional text to append: ")
try:
    file1 = open('output.txt', 'a')
    file1.write(fileAppend)
    file1.close()
except: 
    print("Append Failed")
finally:
    print("Data successfully appended.")


try:
    file1 = open('output.txt', 'r')
    fileRead = file1.read()
    print(fileRead)
    file1.close()
except: 
    print("Read Failed")



