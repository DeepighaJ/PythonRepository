emotions = [ "happy","sad","angry","embarrass","disguise","excited" ]

print("The length of the list is ",len(emotions))   # to get size of the list

for i in emotions:                                  # for loop to iterate over the list
    print(i)
emotions.sort()
print(emotions)
emotions.sort(reverse=True)
print(emotions)
input_index= int(input("Enter the index need to be retrieved: "))
print("The index of the list: ",emotions[input_index])

print("The index of the item 'disguise' is ", emotions.index("disguise"))
emotions.__setitem__(1,"anxious")
emotions[5]= "Mad"         # we can use this syntax to set item and python interpreter internally calls line 12 setitem internally
print(emotions)
print(emotions.__getitem__(2))
emotions.remove("excited")
emotions.pop(4)

for i,j in enumerate(emotions):# enumerate itself a tuple of emotions and index [(0,"happy"),(1,"sad"),(2,"angry)]
    print(i+1,j)
#-------------------------------------------------------------
#List Comprehension - when u try to update/modify work on the same list the use list comprehension
numbers = ['10','19.3','21']
numbers = [float(num) for num in numbers] #here i convert each item into float and update the same in the same list numbers.
print(sum(numbers)) # sum is a function that take iterable(list,tuple/set) and returns a sum of its elements

colors = ['red','blue','green','yellow','white','black','purple']
colors = [item.title() for item in colors] #here i make each items uppercase and update the items in same colors list
print(colors)
#-------------------------------------------------------------
#List Slicing
print(colors[1:4])  #sublist is make from 1 to 3, excluding 4
#-------------------------------------------------------------