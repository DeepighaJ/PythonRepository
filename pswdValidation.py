pswd = input("Enter a password : ")

result ={}      #dictionary in python which has key and value like map in java

if len(pswd) >=8:
    result["length"]=True
else:
    result["length"]=False

digit = False
for i in pswd:
    if i.isdigit():
        digit=True

result["digits"]=digit

uppercase = False
for i in pswd:
    if i.upper():
        uppercase=True

result["upper-case"]=uppercase

print(result)

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")