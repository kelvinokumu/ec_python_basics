def getNumbers(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum
    
# get user  input then type cast to int   
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

ans = getNumbers(num1, num2)
print(ans)