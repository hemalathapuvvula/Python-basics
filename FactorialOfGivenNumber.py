#Factorial of a given number
number=int(input("Enter the numbers:"))
factorial=1
if number<0:
    print("Factorial cant be caluculated for a negative number")
else:
    if number==0:
        factorial=1
        print("The factorial of 0(zero) is:", factorial)
    else:
        for value in range(1,number+1):
            factorial=factorial*value
        print("Entered number is:", number)
        print("factorial of",number, "is",factorial)
