try:
    file1 = open('sample.txt','r')
    file_read = file1.read()
    print(file_read)
    file1.close()
except FileNotFoundError:
    print("Error: The file `sample.txt` was not found")
