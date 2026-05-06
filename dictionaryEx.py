#Dictionary are used like map in Java with Key and Value pairs
#get(), items(), keys(), values(), update(), pop() are most used methods in interviews.
#Used a lot in API response validation, JSON handling

place={
    "USA": "Washington",
    "India": "Delhi",
    "UK": "London",
    "Russia": "Mosco",
    "Japan": "Tokyo",
    "China": "Beijing"
}

print(len(place))
print(type(place))
print(sorted(place))
print(place.get("Japan"))
print(place.values())
print(place.keys())
print(place.items()),
print(place.update({"Russia":"Moscow"}))
print(place.pop("China"))
print(place.popitem())
print(place)
place["France"]="Paris"
print(place)

for p in place:
    print(f"Country {p}")
    print(f"Capitals of {p} is {place.get(p)}")


