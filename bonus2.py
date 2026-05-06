#Tuples are immutable, Less memory usage and Faster iteration, Safer for fixed data

tup = (10,20,20,30,48)

for t in tup:
    print(t)

print(tup.count(20))
print(tup.index(20))
t1 =(1,2)
t2 =(3,4)

#help(tuple)

print(len(tup))
print(min(tup))
print(max(tup))
print(sum(tup))
print(sorted(tup))
print(sorted(tup,reverse=True))
print(t1+t2)


