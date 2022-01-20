n=int(input("Enter The Number : "))
s=0
num=n
while(n>0):
    d=n%10
    s=s+(d**3)
    n=n//10
if(s==num):
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
