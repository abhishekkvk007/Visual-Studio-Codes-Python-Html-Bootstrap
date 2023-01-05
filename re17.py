import re
txt="81345678900"
x=re.findall("[6-9][0-9]{9}",txt)
print(x)
