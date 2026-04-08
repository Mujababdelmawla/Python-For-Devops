import re 

def extract_phone_numbers(filename):
    with open(filename, 'r') as file:
        text = file.read()
        phone_pattern = r'\d{3}-\d{3}-\d{4}'
        phone_numbers = re.findall(phone_pattern, text)
        return phone_numbers


phone_numbers = extract_phone_numbers('contact.txt')
print(phone_numbers)