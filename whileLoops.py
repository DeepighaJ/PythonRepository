from main import userinput

todos = []   #declared a empty list

while True:
    task = input(userinput)
    todos.append(task.capitalize())     #capitalize is a method to convert string initial to uppercase
                                        # append is a method to add items to the list
    todos.append(task.title())          # title is a method to capitalize starting of every word in the string
    print(todos)