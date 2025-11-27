l1=[1,2,2,1,3,4,6,3,4]

s1=set()
d=set()

for i in l1:
    if i in s1:
        d.add(i)
    else:
        s1.add(i)

print(d);