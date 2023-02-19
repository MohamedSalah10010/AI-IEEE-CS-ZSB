my_dict = {"A":[20,30,100,49],
           "B":[00,199,201,29],
           "C":[40,90,69,18]
          }
max_range = 0
max_key = None
for key, value in my_dict.items():
    value_range = max(value) - min(value)
    if value_range > max_range:
       max_range = value_range
       max_key = key


print("The key with the biggest range is:", max_key)
