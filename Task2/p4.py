#import re

def read_users_file(filename):
    users = {}

    with open(filename, 'r') as f:
        contents = f.read()
        lines = contents.splitlines()[1:]
     
        for line in lines:
            user_info = line.split(" ")  # Split the line into its constituent parts
            user_id = int(user_info[0])
            user_name = user_info[1]
            try: 
                user_grades = int(user_info[2])
            except ValueError:
                user_grades=0
            user_birthyear=int(user_info[4])
            user_gender=user_info[6]
            # Create a dictionary for the user and add it to the dictionary of all users
            user = {'name': user_name, 'grade': user_grades,'birthyear':user_birthyear, 'gender':user_gender }
            users[user_id] = user
            
    return users

def remove_NA (dict_x):
    for key, value in list(dict_x.items()):
        if value['grade'] == 0:
            del x[key]
    
    return dict_x

def oldest(dict_x):
    remove_NA(dict_x)
    oldest=dict_x[1].get('birthyear')
    for i in dict_x:
        if dict_x[i].get('birthyear') < oldest:
            oldest = dict_x[i].get('birthyear')
    return oldest

def avg(dict_x):
    remove_NA(dict_x)
    result=counter=0
    for i in dict_x:
        result += dict_x[i].get('grade') 
        counter+=1
    avg=result/ counter
    return avg

def highest(dict_x):
    remove_NA(dict_x)
    highest=0
    for i in dict_x:
        if x[i].get('grade') > highest:
            highest+= x[i].get('grade')
            index=i
    return x[index].get('gender')



x=read_users_file("grades.txt")

print(x)
print(oldest(x))

print(avg(x))

print(highest(x))