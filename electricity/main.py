import pandas as pd

df = pd.read_csv("house_electricity_consumption_1111.csv")

# LIST OPERATIONS
mylist = list(df["Temperature"].head())
print("List:", mylist)
mylist.append(30)
print("Append:", mylist)
mylist.insert(1, 25)
print("Insert:", mylist)
mylist.remove(25)
print("Remove:", mylist)
mylist.pop()
print("Pop:", mylist)
print("Index:", mylist.index(mylist[0]))
print("Length:", len(mylist))

# TUPLE OPERATIONS
mytuple = tuple(df["Occupants"].head())
print("Tuple:", mytuple)
print("First:", mytuple[0])
print("Last:", mytuple[-1])
print("Slice:", mytuple[:3])
print("Length:", len(mytuple))
print("Count:", mytuple.count(mytuple[0]))
print("Index:", mytuple.index(mytuple[0]))

# SET OPERATIONS
myset = set(df["Occupants"])
print("Set:", myset)
myset.add(8)
print("Add:", myset)
myset.discard(8)
print("Discard:", myset)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric:", set1 ^ set2)

# DICTIONARY OPERATIONS
mydict = df.iloc[0].to_dict()
print("Dictionary:", mydict)
print("Temperature:", mydict["Temperature"])
print("Humidity:", mydict.get("Humidity"))
mydict["House"] = "Home"
print("Add:", mydict)
mydict["Occupants"] = 5
print("Update:", mydict)
print("Keys:", mydict.keys())
print("Values:", mydict.values())
print("Items:", mydict.items())
mydict.pop("House")
print("Pop:", mydict)
print("Length:", len(mydict))
print("Columns:", list(df.columns))
print("Rows:", len(df))
print("Shape:", df.shape)