"""
function name : sort_list
function parameters: nums --> a list of numbers
return a sorted version of "nums" 
"""
def sort_list(nums):
    
    return sorted(nums)
"""
function name : find_first_last
function parameters: nums --> a list of numbers
                    target --> a number to find its index
return first occurance of the target and the last index
"""
def find_first_last(nums, target):
    
    nums=sort_list(nums)
    first= nums.index(target)
    
    last= len(nums) - 1 - nums[::-1].index(target)
    return (first, last)

"""
Test code
"""
num_list =list(map(int,input("\nEnter the numbers : ").strip().split()))
target= int(input("Enter the target number: "))

first ,last= find_first_last(num_list, target)

print(first, last)

