def myfun(n):
    return lambda a:a*n
res=myfun(10)#lambda a:a*10
res2=myfun(2)#lambda a:2*10
print(res2)   