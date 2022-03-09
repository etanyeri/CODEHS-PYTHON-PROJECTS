
"""This program asks the user for a number. Report whether
that number is positive, zero, or negative."""


user_num=int(input('What is your number?'))
print('Enter a number: ' + str(user_num))
if user_num<0:
    print('That number is negative!')
elif user_num>0:
    print('That number is positive!')
else:
    print("That number is zero!")