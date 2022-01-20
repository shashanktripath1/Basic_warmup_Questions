binary_number=int(input("Enter The Binary Number : "))
i=0
decimal_number=0
n=binary_number
while(binary_number!=0):
    remainder=binary_number%10
    decimal_number=decimal_number+remainder*(2**i)
    binary_number=binary_number//10
    i=i+1
print("The Decimal equivalent of ",n," is ",decimal_number)
