tlist=["apple","banana","cherry"]
print(tlist)
print(tlist[1])
for x in tlist:
    print(x)

tlist = ["apple", "banana", "cherry"]
tlist.append("orange")
print(tlist)

tlist.insert(2,"guava")
print(tlist)

tlist.remove("guava")
print(tlist)
tlist.pop()
print(tlist)
del tlist[0]
print(tlist)

tlist.clear()
print(tlist)