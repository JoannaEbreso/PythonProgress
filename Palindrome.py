import string

original_string=input("Enter a string: ")
modified_string=original_string.lower()

bad_char= string.whitespace + string.punctuation

for char in modified_string:
    if char in bad_char:
        modified_string= modified_string.replace(char,'')

if modified_string == modified_string[::-1]:
    print("Original String: {}\n \
           Modified String: {}\n \
           Reversed String: {}\n \
           It is a Palindrome!" . format(original_string, modified_string,modified_string[::-1]))
else:
    print("Original String: {}\n \
           Modified String: {}\n \
           Reversed String: {}\n \
           It is not a Palindrome!" . format(original_string, modified_string,modified_string[::-1]))
