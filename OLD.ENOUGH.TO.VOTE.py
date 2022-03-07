"""This program that reports whether or not someone is old 
enough to vote in the U.S. """


voters_age=int(input('What is your age?: '))
#  if the person’s age is at least 18
legal_age= 18
print('Age: '+ str(voters_age))

if voters_age>=legal_age:
    print('You are old enough to vote')
else:
    print('You are not old enough to vote')