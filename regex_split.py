import re 

text = "banana,oraange,apple,grape"
pattern = r","
split_result = re.split(pattern, text)
print(f"the split result is : {split_result}")