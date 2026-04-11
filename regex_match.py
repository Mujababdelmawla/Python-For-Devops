import re 

text = "devops and cloud journey has been an interesting journey"
pattern = r"devops"
match = re.match(pattern, text)
if match :
    print("match is found : ", match.group())

else :
    print("no match")