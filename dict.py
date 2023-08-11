a={"sudarshan" : "7","pratik": "5","pg":"10"}
print(a["sudarshan"])
print(type(a))
print(a["pratik"])

a.popitem()
print(a)

a.pop("pratik")
print(a)

a.copy()
print(a)

a.get(5)
print(a)

a.clear()
print(a)