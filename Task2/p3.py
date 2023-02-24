def largest_sum(nums):
    best=0
    sub=[]    
    for i in nums:
        if best+i > best:
            best+=i
            sub.append(i)
    return (sub, best)

def smallest_sum(nums):
    
    min_num1= min(num_list)
     
    num_list.pop(num_list.index(min_num1))

    min_num2=min(num_list)
    
    sub=[min_num1, min_num2]
    
    least = min_num1+ min_num2
    return (sub, least)

num_list =list(map(int,input("\nEnter the numbers : ").strip().split()))

largest=largest_sum(num_list)    
least= smallest_sum(num_list)

print("the sub array with the largest sum is: {} and its sum is:{}".format(largest[0],largest[1]))

print("the sub array with the smallest sum is: {} and its sum is:{}".format(least[0],least[1]))
