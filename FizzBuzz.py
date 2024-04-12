# AdolNerdHub Shinas Vishwagith whatsapp +94725222161
'''
Write a program that prints the numbers from 1 to 100. But for multiples of three,
print "Fizz" instead of the number, and for the multiples of five, print "Buzz". 
For numbers which are multiples of both three and five, print "FizzBuzz"
'''
# This  loop that will iterate through numbers from 1 to 100 . 
for i in range(1,101):
    # checks if the current value of i is divisible by 5 with no remainder.
    five_d=i%5==0
     # checks if the current value of i is divisible by 3 with no remainder.
    three_d=i%3==0
    # checks if both three_d and five_d are True
    if five_d and three_d:
        print("FizzBuzz")
    elif five_d :
        print("Buzz")
    elif three_d :
        print("Fizz")
    else:
        print(i)

