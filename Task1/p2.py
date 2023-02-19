num_list = []

# get input from user
while True:
        num = input("Enter an integer (press 'q' to quit): ")
        if num == 'q':
            break
        num_list.append(int(num))

def is_symmetric(lst):
    n = len(lst)
    for i in range(n):
        if lst[i] != lst[n-i-1]:
            return False
    return True


if is_symmetric(num_list):
    print("The list is symmetric")
else:
    print("The list is not symmetric")
