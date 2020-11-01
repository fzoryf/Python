#1
import urllib.request



def count_lines(x) :
  line_count = 0
  file_name = x
  my_file = urllib.request.urlopen(file_name)
  for line in my_file :
    line = line.decode("utf-8")
    for line in my_file :
      line_count = line_count + 1
  return line_count

file_name1 = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/Sonnets.txt"
answer1 = count_lines(file_name1)


print("First file number of lines:" , answer1)

#2

import urllib.request
def lines_with_word(x, y) :

  line_count = 0

  file_name = x
  word = y
  my_file = urllib.request.urlopen(file_name)
  for line in my_file :
    line = line.decode("utf-8")
    if word in line :
      line_count = line_count + 1
  return line_count

file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/Sonnets.txt"
answer1 = lines_with_word(file_name, "monuments")

print("monuments appears in ", answer1, "lines")

answer2 = lines_with_word(file_name, "war")

print("war appears in ", answer2, "lines")

#3
import urllib.request
def lines_with_word(x, y) :

  line_count = 0

  file_name = x
  word = y
  my_file = urllib.request.urlopen(file_name)
  for line in my_file :
    line = line.decode("utf-8")
    line = line.lower()
    if word in line :
      line_count = line_count + 1
  return line_count


file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/Sonnets.txt"
answer1 = lines_with_word(file_name, "shall")

print("Shall appears in ", answer1, "lines")


#4
import urllib.request
def word_count(x, y) :

  w_count = 0
  word = y
  file_name = x
  my_file = urllib.request.urlopen(file_name)

  my_file = my_file.read()
  my_file = my_file.decode("utf-8")
  my_file = my_file.lower()
  no_line_breaks = my_file.replace("\n", " ")

  list_of_words = no_line_breaks.split()

  for z in list_of_words :
    if z == word :
      w_count = w_count + 1
  return w_count

file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/Sonnets.txt"
answer1 = word_count(file_name, "monuments")

print("monuments appears ", answer1, "times")

answer2 = word_count(file_name, "war")

print("war appears times", answer2, "times")


#5
import urllib.request
def word_count(x, y) :

  w_count = 0
  word = y
  file_name = x
  my_file = urllib.request.urlopen(file_name)

  my_file = my_file.read()
  my_file = my_file.decode("utf-8")
  my_file = my_file.lower()

  nlb = my_file.replace("\n", " ")


  nlb2 = nlb.replace(",", " ")


  nlb3 = nlb2.replace(".", " ")


  nlb4 = nlb3.replace('"', " ")


  nlb5 = nlb4.replace("'", " ")


  nlb6 = nlb5.replace(":", " ")


  nlb7 = nlb6.replace(";", " ")


  nlb8 = nlb7.split()


  for z in nlb8 :
    if z == word :
      w_count = w_count + 1
  return w_count

file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/Sonnets.txt"
answer1 = word_count(file_name, "memory")

print("memory appears ", answer1, "times")

answer2 = word_count(file_name, "fuel")

print("fuel appears times", answer2, "times")

#6
import urllib.request
def word_count(x, y) :

  w_count = 0
  word = y
  file_name = x
  my_file = urllib.request.urlopen(file_name)

  my_file = my_file.read()
  my_file = my_file.decode("utf-8")
  my_file = my_file.lower()

  nlb = my_file.replace("\n", " ")


  nlb2 = nlb.replace(",", " ")


  nlb3 = nlb2.replace(".", " ")


  nlb4 = nlb3.replace('"', " ")


  nlb5 = nlb4.replace("'", " ")


  nlb6 = nlb5.replace(":", " ")


  nlb7 = nlb6.replace(";", " ")


  nlb8 = nlb7.split()


  for z in nlb8 :
    if z == word :
      w_count = w_count + 1
  return w_count

file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/Sonnets.txt"
answer1 = word_count(file_name, "memory")

print("memory appears ", answer1, "times")

answer2 = word_count(file_name, "fuel")

print("fuel appears times", answer2, "times")

#7
import urllib.request
def word_count(x, y) :

  w_count = 0
  word = y
  file_name = x
  my_file = urllib.request.urlopen(file_name)

  my_file = my_file.read()
  my_file = my_file.decode("utf-8")
  my_file = my_file.lower()

  nlb = my_file.replace("\n", " ")
  nlb2 = nlb.replace(",", " ")
  nlb3 = nlb2.replace(".", " ")
  nlb4 = nlb3.replace('"', " ")
  nlb5 = nlb4.replace(":", " ")
  nlb6 = nlb5.replace(";", " ")
  nlb7 = nlb6.split()


  for z in nlb7 :
      w_count = w_count + 1
  return w_count



def word_frequency(x, y, z) :
 w_count = 0
 word = y
 total = z
 file_name = x
 my_file = urllib.request.urlopen(file_name)

 my_file = my_file.read()
 my_file = my_file.decode("utf-8")
 my_file = my_file.lower()

 nlb = my_file.replace("\n", " ")
 nlb2 = nlb.replace(",", " ")
 nlb3 = nlb2.replace(".", " ")
 nlb4 = nlb3.replace('"', " ")
 nlb5 = nlb4.replace("'", " ")
 nlb6 = nlb5.replace(":", " ")
 nlb7 = nlb6.replace(";", " ")
 nlb8 = nlb7.split()


 for a in nlb8 :
  if a == word :
    w_count = w_count + 1
 print (w_count)
 freq = (w_count / total) * 100
 return freq


print ("Hello! I'm gonna tell you the frequency of a word in a file you give me.")
file_name = input("First, I'm going to want you to copy and paste your file link here: ")
word = input("Now, enter the word you'd like me to check the frequency of: ")
file_words = word_count(file_name, word)
print ("The total number of words is:", file_words)
frequency = word_frequency(file_name, word, file_words)

print (word, "appears in", frequency, "% of the entire file.")