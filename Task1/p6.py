data = {}

rows = input("Enter boys and girls with their age separated by commas in each row: ").split()


for row in rows:
    entries = row.split(",")
    for entry in entries:
        name, age = entry.split(":")
        data[name] = int(age)


print(data)
