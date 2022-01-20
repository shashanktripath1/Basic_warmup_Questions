decimal_number=int(input("Enter The Decimal Number : "))
i=0
binary_number=0
n=decimal_number
while(decimal_number!=0):
    remainder=decimal_number%2
    binary_number=binary_number+remainder*(10**i)
    decimal_number=decimal_number//2
    i=i+1
print("The Binary Equivalent of ",n," is ",binary_number)
    
