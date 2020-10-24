#0
import urllib.request
import random

def choose_word():
  file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/coolWords.txt"
  my_file = urllib.request.urlopen(file_name)
  long_string = my_file.read()
  long_string = long_string.decode("utf-8")
  word_list = long_string.split("\n")
  return random.choice(word_list)

#had a idea to use return random.choice(word_list) for this instead of the index but each instance of chooseword it would choose a different word i think

#1
rWord= choose_word()
blanks_list = [rWord]
length = len(rWord)

for spaces in range (length) :
  blanks_list.append(" _ ")
blanks_list.remove(rWord)
#2
#Find way to let user know how many letters are in the word from the list maybe with len() function inside chooseword
#Or will the blanks be displayed and cue the user first
#problems with isdigit


print("Let's play some hangman! \nHere's all the info I can give you on this word: \n", blanks_list)

def guess_check(x):


  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  while x.isdigit() :
      x = input ("This is hangman not sudoku! \nNow enter a letter this time: ")



  while (len(x) != 1 or x not in alphabet) :
      x = input ("I said single letter!!!! Not character, not letterS! \n LETTER:")
      while x.isdigit() :
          x = input ("This is hangman not sudoku! \nNow enter a letter this time: ")
  if (len(x) == 1 and x in alphabet) :
    return x






#make usedwrongletters list to hold all of the incorrect guesses so they dont repeat
#Should i put a counter in printbody or a seperate function that sends to printbody that is counting the wrong answers and how would i do either

#3 takes in wrong guesses and prints the appropriate thingy
num = 0
def printbody(num) :

    if num == 0 :
   #no stick figure all correct guesses
        print("____\n|   |\n|\n|\n|\n|\n----------")
        print(" Your stick person is safe... for now...")


    elif num == 1 :
    #head, only one incorrect guess
        print("____\n|   |\n|   o\n|\n|\n|\n----------")
        print("uhoh! don't get aHEAD of yourself!")


    elif num == 2 :
    #3 head and body, two incorrect guesses
        print("____\n|   |\n|   o\n|   |\n|\n|\n----------")
        print("Your stick body is forming!!!")


    elif num == 3 :
    #4 head, body, and right arm, 3 incorrect guesses
        print("____\n|   |\n|   o\n|   |\ \n|\n|\n----------")
        print("Hey, your stick person is actually looking allRIGHT")


    elif num == 4 :
    #5 head, body, both arms, 4 incorrect guesses
        print("____\n|   |\n|   o\n|  /|\ \n|\n|\n----------")
        print("At least your stick person can give hugs now?")

    elif num == 5 :
    #6 head, body, arms, and right leg, 5 incorrect guesses
        print("____\n|   |\n|   o\n|  /|\ \n|    \ \n| \n----------")
        print("I'm gonna be honest things arent looking too good for you right now...")

    elif num == 6 :
    #7 all limbs lost :( 6 incorrect guesses + losing statement
        print("____\n|   |\n|   o\n|  /|\ \n|  / \ \n| \n----------")
        print("andddd I think they're dead, this is awkward")


my_list = list(rWord)

wrong_guesses = []

#3 need to accomplish: list of wrong guesses that adds, counter for printbody to refer to, transform guesses to lowercase?
def ifWrong(x):

  printbody(num)
  wrong_guesses.append(x)
  print ("Here are your wrong guesses:", wrong_guesses )


#4 need to accomplish: put letters into blank_list placements, figure out how to count reoccuring letters, print new blank list with corresponding letters
def ifRight(x):

  indices = [i for i, l in enumerate(rWord) if l == x]
  for i in indices :
    blanks_list[i] = x
  strblanks = ""
  strblanks = strblanks.join (blanks_list)
  print(strblanks)
  printbody(num)

#5 implement guess_check
while num != 6 :
  guess = input("Enter a single letter guess:")
  guess_check(guess)
  if guess in my_list :
    ifRight(guess)
    print("You guessed correct!")

    if " _ " not in blanks_list :
      print ("You won!")
      break
  if not guess in my_list :
    guess_check(guess)
    num = num + 1
    guess = ifWrong(guess)
    print ("try again")

if num == 6 :
  print ("You lost :( Better luck next time!")
  print ("The correct answer was:", rWord)
