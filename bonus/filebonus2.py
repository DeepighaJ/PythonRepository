# filenames = ['doc1.txt', 'report1.txt', 'presentation1.txt']
#
# for filename in filenames:
#     file = open(f"../files/{filename}",'w')
#     file.write("Hello")
#     file.close()
# ---------------
# filenames = ['a.txt','b.txt','c.txt']
#
# for filename in filenames:
#     file = open(f"../files/{filename}",'r')
#     text = file.read()
#     print(text)
# #-------------------

file = open("../files/data.txt", 'w')

file.write("100.12"+"\n")
file.write("111.23"+"\n")

file.close()


