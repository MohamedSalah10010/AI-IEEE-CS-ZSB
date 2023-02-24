
num_list =list(map(int,input("\nEnter the numbers : ").strip().split()))

even_count= len(list(filter(lambda x: (x%2 == 0) , num_list)))

print("The even numbers in this list is: {}".format( even_count))