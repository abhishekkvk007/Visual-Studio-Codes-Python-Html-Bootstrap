import re
txt="The rain in spain 4_!"
x=re.findall("\D",txt)
print(x)

# \A-^
#\Z-$
