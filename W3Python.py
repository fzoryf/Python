
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
  else:
    return False


va = [3, 2, 8, 9, 17, 24]
for current in [3, 2, 8, 9, 17, 24]:
    if is_it_even (current) :
        counter = counter + 1



print ( "There are" , counter, "even numbers" )
#Question3.2
counter = 0
def is_it_even(number):
  if(number % 2 == 0):
    return True
  else:
    return False

number0 = int ( input ( "Type 1 number" ))
number1 = int ( input ( "Type 1 number" ))
number2 = int ( input ( "Type 1 number" ))
number3 = int ( input ( "Type 1 number" ))
number4 = int ( input ( "Type 1 number" ))

va = [number0 , number1 , number2 , number3 , number4]
for current in [number0, number1, number2, number3, number4] :
    if is_it_even(current) :
        counter = counter + 1

print ( "There are" , counter, "even numbers" )
#Question4
counter = 0
def is_it_even(number):
  if(number % 2 == 0):
    return True
  else:
    return False
number = int(input("I am going to count how many even numbers you enter! Type 0 when done."))
while number != 0 :
    number = int(input("Type another number."))
    if is_it_even(number) :
        counter = counter + 1
else:
    print ("You entered", counter, "even numbers")
#Question5
number = 8
print("Guess what number I'm thinking of!")


for guessesTaken in range(1, 1000000):
    print("C'mon guess what it is already!")
    guess = int(input())

    if guess < number:
        print("TOO HIGH!!!")
    elif guess > number:
        print("too low :(")
    else:
        break

if guess == number:
    print("You guessed it! Finally!!")