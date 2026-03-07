def get_average():
    with open("../files/tempdata.txt",'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values] #list comprehension
    average_lc= sum(values)/len(values)
    return average_lc

average = get_average()
print(average)