""" User gets to type the length and width of the rectangle.
write some mathematical expressions in print statements to 
display the area and perimeter of the rectangle."""


length= int(input('What is the length?:'))
width= int(input('What is the width?:'))

area= length*width
perimeter= 2*(length+width)

print('Area:'+ str(area))
print('Perimeter:' + str(perimeter))