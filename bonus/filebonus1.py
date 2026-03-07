contents = ["All carrots are to be sliced "
            "longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt","report.txt","presentation.txt"]

for content,filename in zip(contents,filenames):            #zip function allows you to iterate over multiple iterables in parallel
    file = open(f"../files/{filename}","w")                    # contents,filenames are tuples of zip
    file.write(content)
    file.close()

inputtext = input("Add a new member: ")

file = open("../files/members.txt",'r')
existing = file.readlines()
file.close()

existing.append("\n"+ inputtext + "\n")

file = open("../files/members.txt",'w')
file.writelines(existing)
file.close()

