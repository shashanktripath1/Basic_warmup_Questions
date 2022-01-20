n=int(input("Enter The Number : "))
s=0
num=n
while(n>0):
    digit=n%10
    s=s+digit
    n=n//10
print("The sum of ",num," is",s)

#############################################

def sod(n):
    s=0
    while(n>0):
        digit=n%10
        s=s+digit
        n=n//10
    return s
n=int(input("Enter The Number : "))
num=n
a=sod(n)
print("The sum of ",num," is",a)
