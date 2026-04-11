import re 

text = "i love coding with python"
pattern = r"coding"
search = re.search(pattern, text)
if search :
    print("pattern found :", search.group())

else :
    print("pattern not found ..")