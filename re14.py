import re
txt="main main in spain"
x=re.findall("^(The|main)",txt)
print(x)
