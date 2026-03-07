name = " DeepighaJapamony  "
details =("All carrots are to be sliced longitudinally.\n "
          "Among common varieties root shapes range from globular to long, with lower ends blunt to pointed.\n "
          "Besides the orange-coloured roots, white-, yellow-, and purple-fleshed varieties are known.\n")
print(len(name))

for i,j in enumerate(name):     #string also can be enumerated
    print(i,j)

print(len(name))
print(name.strip())         #this trims the forward and backward trailing spaces
print(name.lstrip())        # trims the first trailing spaces
print(name.rstrip())        # trims the last trailing spaces
print(name.capitalize())    # Capitalize first letter
print(name.title())         # Capitalize whole word
print(name.upper())         # Capitalize whole word
print(name.lower())         # lowercase whole word
print(name.split('a',2))    #Split the word for first 2 times of character 'a' then dont split
print(name.split(' '))      # split by space
print(name.rsplit('a'))
print(details.splitlines(keepends=True))
print(name.casefold())
print(name.count('a'))
print(name.__contains__("pig"))
print(name.center(25,"b"))
print(name.index("pig"))
print(details.partition("to"))
print(name.join("rajesh"))
print(name[9:]) #slicing or making a substring from index 9 till end
