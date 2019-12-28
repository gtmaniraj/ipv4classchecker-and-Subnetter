#wap to check a entered number is even or odd

def evenodd(data):
    if (data%2 == 0):
        print("Entered data {} is even".format(data))
    else:
        print("Entered data {} is odd ".format(data))

data=input("Enter the data: ")
data = int(data)
evenodd(data)
