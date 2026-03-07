file = open("../files/report.txt","r")
content =file.read()
print(content)
file.close()
#Context manager, this doesn't need to f.close(), this block automatically closes file code
with open("../files/report.txt","r") as file:
    content = file.read()
    print(content)