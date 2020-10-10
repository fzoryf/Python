#0
hi = 'Hello world!'
print (hi)
print (hi.lower())
print (hi.upper())
#1
def hasVowels(x):

    for v in vowels :
        if v in x :
            return True

    return False

vowels = ['a', 'e', 'i', 'o', 'u']
word = "berry"
not_word = "fghjk"

if hasVowels(word):
  print("The string", word, "has at least one vowel")
else:
  print("The string", word, "does not have any vowels")

if hasVowels(not_word):
  print("The string", not_word, "has at least one vowel")
else:
  print("The string", not_word, "does not have any vowels")
#2
def hasVowels(x):

    for v in vowels :
        if v in x :
            return True

    return False

vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Gimmie a word with some vowels!")

while not hasVowels (word) :
    word = input ('I said a word WITH vowels!')

else:
    print ('Hey',word ,'has some vowels in it! yay!')
#3
vowels = ['a', 'e', 'i', 'o', 'u']


def countVowels(x) :
    counter = 0
    for v in (x):
        if v in vowels:
            counter = counter + 1
    return counter

name1 = "zory"
name2 = "aeiou"

count1 = countVowels(name1)
count2 = countVowels(name2)


print(name1, "has", count1, "vowels in it")
print(name2, "has", count2, "vowels in it")
#4
thelist = []

word = input("Type some words and I'll make a list for ya! Type any variation of 'stop' when you're done")

while not word.lower() == "stop":
  thelist.append(word)
  word = input("Keep em coming!")

if word.lower() == "stop" :
    print("Here's everything you put down: ", thelist )

#5
vowels = ['a', 'e', 'i', 'o', 'u']
def countVowels(x) :
    counter = 0
    for v in (x):
        if v in vowels:
            counter = counter + 1
    return counter
thelist = []

word = input("Type some words and I'll tell you how many vowels they have. \nType any variation of 'stop' when you're done:")
v = 0
while not word.lower() == "stop":
  thelist.append(word)
  word = input("Keep em coming!")

if word.lower() == "stop" :
    for word in thelist:
        v = v + countVowels(word)
    print("Here's everything you put down: ",thelist)
    print ("And the number of vowel in all that is:", v)