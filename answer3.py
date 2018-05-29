def table(num,lim,t):
    if lim==1:
        t.insert(0,num)

    else:
        t.insert(0,num*(lim))
        table(num,lim-1,t)
t=[]
table(12,10,t)
for i in t:
    print(i)
