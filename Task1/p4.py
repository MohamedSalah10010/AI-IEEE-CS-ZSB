def solution(list1,target):  
        length = len(list1)  
          
        for i in range(length-1):  
            for j in range(i+1, length):  
                if list1[i]+list1[j] == target:  
                    new_list = i, j  
                    return new_list  
        return None  
  

num_list =list(map(int,input("\nEnter the numbers : ").strip().split()))
target= int(input("Enter the target number: "))
#lst= [1, 2, 4, 5, 11]  
#target = 6  

result = solution(num_list, target)

if result is not None:
    print("The indices of the first two numbers that add up to the target number are:", result)
else:
    print("No such pair of numbers exists.")



