

"""
This program asks the user for three ingredients,
three amounts, and a number of servings, and
determines how much of each ingredient is needed
to serve the specified number of servings.
"""

firstin=input('the name of first ingredient:')
firstinounce=float(input('How many ounces are there?:'))
secondin=input('the name of second ingredient:')
secondinounce=float(input('How many ounces are there?:'))
thirdin=input('the name of first ingredient:')
thirdinounce=float(input('How many ounces are there?:'))
servnum=int(input('how many serves are there?:'))

print('Total ounces of '+ firstin + ':'+ str(firstinounce*servnum))
print('Total ounces of '+ secondin + ':'+ str(secondinounce*servnum))
print('Total ounces of '+ thirdin + ':'+ str(thirdinounce*servnum))