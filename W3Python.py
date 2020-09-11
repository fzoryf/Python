
#Question0
for hi in range (5):
    print ("HELLO WORLD")
#Question 1
number1 = int ( input ( "Enter a number" ))
number2 = int ( input ( "Enter another number" ))
if number1 < number2 :
    print ( " Well" , number1, "is smaller than" , number2 )
if number2 < number1 :
    print ( "Seems like" , number2, "is smaller than ", number1 )
#Question 2
number1 = int ( input ( "Enter a number" ))
number2 = int ( input ( "Enter another number" ))
number3 = int ( input ( "Enter ANOTHER number" ))
if number1 > number2 > number3 or number3 > number2 > number1 :
    print ( "Seems like" , number2, "is the second largest number " )
if number2 > number1 > number3 or number3 > number1 > number2 :
    print ( "Seems like" , number1, "is the second largest number " )
if number1 > number3 > number2 or number2 > number3 > number1 :
    print ( "Seems like" , number3, "is the second largest number " )
#Question3
counter = 0
def is_it_even(number):
  if(number % 2 == 0):
    return True
    va = [3, 2, 8, 9, 17, 24]
    if is_it_even(for va in [3, 2, 8, 9, 17, 24]):
    counter + 1
  else:
    return False
print ( "There are" , counter, "even numbers" )

