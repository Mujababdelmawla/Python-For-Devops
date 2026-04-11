import re 

text = "the car with the red colour is faster than the white one"
pattern = r"red"
replacement = "blue"
new_text = re.sub(pattern, replacement, text)
print(f"the modified text is : {new_text}")