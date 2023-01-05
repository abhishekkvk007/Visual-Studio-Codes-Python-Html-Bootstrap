import re
txt="The rain in spain 786!"
x=re.findall("[a-zA-Z 0-9!]",txt)
print(x)
