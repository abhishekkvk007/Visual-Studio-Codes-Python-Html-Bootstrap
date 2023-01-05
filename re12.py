import re
txt="The rainnn i spainnnnnnn"
x=re.findall("in{,4}",txt)
print(x)
