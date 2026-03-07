filenames = ["1.Raw Data.txt","2.Reports.txt","Presentations.txt"]
#strings are immutable and list are mutable ie filename[1]="_" like this we cannot assign and replace a string this is error
#Section 4: 42 bonus example refer for mutable immuatble

for filename in filenames:
    filename = filename.replace(".","-",1)  #replace the first occurance only
    print(filename)


filenames = ["1.doc","1.report","1.presentation"]

filenames = [filename.replace(".","-") + ".txt" for filename in filenames] #List Comprehension
print(filenames)

