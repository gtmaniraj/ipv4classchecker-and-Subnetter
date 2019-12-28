file_path=str(input("Enter the path of file name to be read : "))
file=open(file_path,"r")
for line in file:
    print(line.rstrip())
