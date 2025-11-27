def ngg(n,g=23):
    if (g-n<5):
        return "Too low"
    if (g-n==0):
        return "Correct"
    if (g-n>5):
        return "Too High"

n=int(input("Enter any no"))

print(ngg(n));
