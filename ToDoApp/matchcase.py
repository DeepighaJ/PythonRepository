#todos = []

while True:
    user_action = input("Type add,show,edit, complete or exit: ")

    match user_action.strip():              #strip method is used to trim trailing spaces in useraction variable
        case 'add':
            todo = input("Enter a todo: ") +"\n" # input function always returns a string even if we enter number its string

            file = open('todos.txt', 'r')  # creates a file and r in read mode
            todos = file.readlines()  # readlines() is to read the lines & return list; readline() reads first line & return string
            file.close()

            todos.append(todo)

            file = open('todos.txt','w')        #creates a file and w in writemode
            file.writelines(todos)              #writeline is to write the list in the file
            file.close()

        case 'show':
            file = open('todos.txt', 'r')  # creates a file and r in readmode
            todos = file.readlines()  # readline is to read the lines and return list
            file.close()
            print(todos)

            # new_todos = []            this part of code can be achieved by list comprehension in otherway like below
            # for item in todos:
            #     new_item = item.strip("\n")
            #     new_todos.append(new_item)
            new_todos = [item.strip("\n") for item in todos]    #List Comprehension

            for index, items in enumerate(new_todos):             #for loop to print todos; enumerate() takes list and print count
               # print(index, '-', items.title())        # o/p will be 0 - Red 1 - Blue i
                #fstring - norder to remove the space between index and - and item we need to use fstrings
                row = f"{index+1}-{items.title()}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit"))   #input returns a String so we need int() to integer
            number = number - 1
            new_todo = input("Enter new todo")
            todos[number] = new_todo        #assigning  todos[index] with new input
            break

        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)  #this removes the item from list for given index

        case 'exit':
            break
        case var:                           # this var can be any variable
            print("You have entered wrong input please enter add or show")

print("Bye!")


