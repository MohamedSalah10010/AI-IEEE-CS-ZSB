import p4

def create_filtered_file(data):
    with open('filtered.txt', 'w') as f:
        f.write("id, name, age\n")
        for id, info in data.items():
            if info['grade'] != 0:
                name = info['name']
                birthyear = info['birthyear']
                age = 2023 - birthyear
                f.write(f"{id}, {name}, {age}\n")


create_filtered_file(p4.x)