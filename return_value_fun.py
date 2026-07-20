def sum_sub_mul_div(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f
t=sum_sub_mul_div(10,3)
print("the result are")
for i in t:
    print(i,end=", ")
