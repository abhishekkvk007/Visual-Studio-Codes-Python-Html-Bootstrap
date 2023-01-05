import re
txt="The rain in spain 4_!"
x=re.findall(r"\Bai",txt)
print(x)

# \A-^
#\Z-$
