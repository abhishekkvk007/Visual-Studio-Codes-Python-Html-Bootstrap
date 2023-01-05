import re
txt="The rain in spain 4_!"
x=re.findall("in\b",txt)
print(x)

# \A-^
#\Z-$
