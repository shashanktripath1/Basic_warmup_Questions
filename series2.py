#wap to print the sum of the series---1/1**2+1/2**2+1/3**2+----`1/n**2
n=int(input("Enter The Number : "))
s=0.0
for i in range(1,n+1):
    a=1.0/(i**2)
    s=s+a
print("The sum of 1/1**2+1/2**2+1/3**2+----`1/n**2 is ",s)
