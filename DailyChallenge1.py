# Create a function that removes all capital letters and punctuation in a string. Return the clean string.

import string
def clean_string(s):
    a = str()
    for i in s:
        if i.isupper() == False and i not in string.punctuation:
            a += i
    return a

print(clean_string("Abc.De!@f13J"))
print("Testing~")