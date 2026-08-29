def factorial(number):
    if number==0 or number==1:
        print("factorial(",number,")=1")
        return 1
    else:
        print("factorial(",number,")=",number,"*factorial(",number-1,")")
        result=number*factorial(number-1)
        return result
number=(int(input(" enter a number:")))
if number<0:
    print("factorial is not possible for negative number:")
else:
    print("Recursive calls")
    result=factorial(number)
    print("Given number:",number)
    print("factorial of",number,"is",result)
