#q1
def taxes(sal):
    if sal<=30000:
        return sal-sal*0.05
    elif sal<=70000:
        return sal-sal*0.10
    else:
        return sal-sal*0.25

sal=int(input("enter salary"))

print(taxes(sal));
