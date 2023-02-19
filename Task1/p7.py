my_list = input("Enter the list to be rotated:").split()

k = int(input("Enter the unit of rotatation:"))

k = int(k % len(my_list))

rotated = my_list[-k:] + my_list[:-k]
    
print(rotated)