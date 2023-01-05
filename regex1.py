import re
txt="The winners are spain"
x=re.search("^The.*spain$",txt)
if x:
    print("format is correct")
else:
    print("format is incorrect")
        