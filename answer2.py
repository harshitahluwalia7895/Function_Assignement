def perfect(number):
    num=0
    for i in range(1,number):
        if number%i==0:
            num+=i
    else:
        if num==number:
            return True
    return False
for i in range(1,1000):
    if perfect(i):
        print(i)
