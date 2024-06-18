#Task 1
#Identify errors in code and fix them >>>> 3 errors the first one is on the "number = input" line the number needs to equal an int with an input inside parentheses asking the question, one on the elif statement an "=" id needed for proper syntax
# the othe error was on the else statement the "number < 0" statement is not needed being that it is an else statement it defeats the purpose.


number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")