#todos = []

while True:
    user_action = input("Type add,show,edit, complete or exit: ")

    match user_action.strip():              #strip method is used to trim trailing spaces in useraction variable
        case 'add':
            todo = input("Enter a todo: ") +"\n" # input function always returns a string even if we enter number its string

            # file = open('todos.txt', 'r')  # creates a file and r in read mode
            # todos = file.readlines()  # readlines() is to read the lines & return list; readline() reads first line & return string
            # file.close()
            #         or the below context manage code

            with open('todos.txt','r') as file:         #Context manager, this doesnt need to f.close(), this block automatically closes file
                todos = file.readlines()

            todos.append(todo)

            # file = open('todos.txt','w')        #creates a file and w in writemode
            # file.writelines(todos)              #writeline is to write the list in the file
            # file.close()

            with open('todos.txt','w') as file:
                file.writelines(todos)

        case 'show':
            # file = open('todos.txt', 'r')  # creates a file and r in readmode
            # todos = file.readlines()  # readline is to read the lines and return list
            # file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
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

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            print('Here is the existing todos',todos)

            new_todo = input("Enter new todo")
            todos[number] = new_todo  + '\n'      #assigning  todos[index] with new input

            print('Here is how it will be',todos)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            break

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)  #this removes the item from list for given index

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        case 'exit':
            break
        case var:                           # this var can be any variable
            print("You have entered wrong input please enter add or show")

print("Bye!")


