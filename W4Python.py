#Question 0
def hiw():
    print ( "Hello World!" )

hiw()

#Question 1
def hk5():
    for hk5 in range ( 5 ) :
        print ( "hello kitty is angry" )

hk5()

#Question2
number = int (input ( "Find out how angry hello kitty is by typing a number" ))
print ( "hello kitty is" )

def hk5():
    for hk5 in range ( number ) :
        print ( "VERY" )



hk5()

print ( "ANGRY!!!!!" )

#Question3
lets = int (input ( "Enter a number and I'll square it for you cause I'm smart like that" ))

def square(number):
    answer = number * number
    return answer

x = square ( lets )
print ( x )

#Question4 "none" appearing after is issue
hm = int (input ( "Tell me a number and I'll tell YOU if it's bigger than ten." ))

def bigger10(number):

    if number > 10 :
        print ( " ", hm, " is bigger than 10! " )
    else :
        print ( " 10 is bigger than your number " )


x = bigger10 ( hm )
print ( x )

#Question5

(x) = int (input ( "Gimmie a number!" ))
(y) = int (input ( "Gimmie another number and I'll tell you which of the two is bigger"))
def bigger(x, y):

    if x > y :
        print ( " ", x, " is bigger! " )
        return x
    if y > x :
        print ( " ", y, " is bigger! " )
        return y


z = bigger ( x, y )
print ( z )

#Question6
(x) = int (input ( "Enter your age!" ))
(y) = int (input ( "Now enter your best friends age"))
def bigger(x, y):

    if x > y :
        print ( "You are older and:", x,  "years old!" )
        return x
    if y > x :
        print ( "Your friend is older at: ", y,  "years old!" )
        return y


z = bigger ( x, y )

#Question7