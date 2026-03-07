def readfile():
    with open('todos.txt','r') as file_local:  # Context manager, this doesnt need to f.close(), this block automatically closes file
        todos_local = file_local.readlines()
    return todos_local

def writefile():
    with open('todos.txt', 'w') as file_write:
        file_write.writelines(todos)


while True:
    user_action = input("Type add,show,edit, complete or exit: ")
    user_action = user_action.strip() #strip method is used to trim trailing spaces in useraction variable

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = readfile()

        todos.append(todo+'\n')

        writefile()

    elif user_action.startswith("show"):
        todos = readfile()
        print(todos)

        new_todos = [item.strip("\n") for item in todos]    #List Comprehension

        for index, items in enumerate(new_todos):             #for loop to print todos; enumerate() takes list and print count
            row = f"{index+1}-{items.title()}"
            print(row)

    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])  #input returns a String so we need int() to integer
            number = number - 1

            todos = readfile()
            print('Here is the existing todos',todos)

            new_todo = input("Enter new todo")
            todos[number] = new_todo  + '\n'      #assigning  todos[index] with new input

            print('Here is how it will be',todos)

            writefile()
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9: ])

            todos = readfile()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)  #this removes the item from list for given index

            writefile()

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("You have entered wrong input, Command not Valid")

print("Bye!")


