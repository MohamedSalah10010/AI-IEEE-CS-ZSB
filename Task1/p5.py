str_list = ["apple", "banana"]
first_half = []
second_half = []
for s in str_list:
   
   first_half.append(s[0:len(s)//2])
   second_half.append(s[len(s)//2 if len(s)%2 == 0 else ((len(s)//2)+1):])

first_list=[]
sec_list=[]

first_list.append(first_half)
sec_list.append(second_half)

print(first_list)
print(sec_list)
