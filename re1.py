import re
txt="The rain in spain"
x=re.search("in",txt)
print(x)
print(x.span())
print(x.start())
print(x.end())
print(x.string)