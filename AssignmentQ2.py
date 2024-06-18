#Task 1: Identify the Greastest
#Write a program that asks user for 3 number andthe program should identify and print out the largest number


number_1 = int(input("Enter the first number. :"))
number_2 = int(input("Enter the second number. :"))
number_3 = int(input("Enter the third number. :"))

#Find the largest number

largest = max(number_1, number_2, number_3)

# Print Result

print(f"The largest number is: {largest}")




#Task 2 conttinue task one to find the smallest number input by user

smallest = min(number_1, number_2, number_3)


# Print Result

print(f"The smallest number is: {smallest}")



#Task 3 Enhance your program to handle cases where two or all of the numbers are equal

# I am going to use an if statement to get and print the result along with f brackets inside my print statement to show the result of which numbers are equal and largest or if all equal

if number_3 == number_2 > number_1:
    print(f"Two numbers are equal and the largest: Number 3 and Number 2 {number_3, number_2}")
elif number_1 == number_3 > number_2:
    print(f"Two numbers are equal and the largest: Number 1 and Number 3 {number_1, number_3}")
elif number_1 == number_2 > number_3:
    print(f"Two numbers are equal and the largest: Number 1 and Number 2 {number_1, number_2}")
elif number_1 == number_2 == number_3:
    print(f"All numbers are equal: Numbers 1, 2 and 3 {number_3, number_2, number_1}")
