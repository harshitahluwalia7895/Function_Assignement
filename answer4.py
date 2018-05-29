def power(a,b):
    if b==1:
        return a
    else:
        return a*power(a,b-1)
a=int(input("Enter a in a**b: "))
b=int(input("Enter b in a**b: "))
print(power(a,b))
