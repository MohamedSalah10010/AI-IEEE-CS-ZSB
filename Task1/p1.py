num_list = []

# get input from user
while True:
        num = input("Enter an integer (press 'q' to quit): ")
        if num == 'q':
            break
        num_list.append(int(num))
# sort the list
num_list.sort()

# get the second largest and second smallest numbers
second_largest = num_list[len(num_list)-2]
second_smallest = num_list[1]

# print the results
print("\nSecond largest number in the list is:", second_largest)
print("\nSecond smallest number in the list is:", second_smallest)