names = set()

names.add("Alice")
names.add("Bob")
names.add("Charlie")
names.add("Diana")
names.add("Ethan")

print("Initial names:", names)


if "Charlie" in names:
    names.remove("Charlie")
    names.add("Carlos")

print("After modifying one name:", names)

names.discard("Alice")
names.discard("Bob")

print("After deleting two names:", names)