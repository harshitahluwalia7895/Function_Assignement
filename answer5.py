def fact(num):
    if num<=1:
        return 1
    else:
        return num*fact(num-1)
dict={}
ch='y'
while ch=='y':
    n=int(input("Enter number to find factorial of: "))
    f=fact(n)
    dict[n]=f

    ch=input("Do you want to find more factorials?? y/n : ")

print("The dictionary for all your inputs and their factorials are Listed below as: ")
print(dict)
