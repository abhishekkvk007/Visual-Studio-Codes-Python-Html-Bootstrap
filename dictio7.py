a=100#global scope variable
def fun():
    global b
    b=200
    print(b)
    print(a)
print(a)

fun()
print(b)
