import math
import os
from subprocess import list2cmdline

#Used help from w3schools and stackoverflow.
def numLetterCheck(word):
    vowel = 0 #vowel count
    consonant = 0 #consonant count

    for letter in word: #loops through all letters in the word
        if letter in ("aeiouAEIOU"):
            vowel += 1
        else:
            consonant += 1
    if vowel == consonant:
        return None
    else:
        return vowel > consonant

#Used python documentation for help.
def cylinderVol(height, radius):
   volume = float(height * math.pow(radius, 2) * math.pi) #equation for volume of cylinder 
   return volume

#Help from StackOverflow and W3schools
def csvMaker(list):
    tempStr = ', '.join(list)
    return tempStr

#Help from StackOverflow, W3Schools, and Python Docs
def csvList(listOfLists):
    f = open("csv.txt", "w")
    for i in listOfLists:
      temp = csvMaker(i)
      f.write(temp + "\n")
    f.close()
    return os.path.abspath('csv.txt')
    

list = ["Alligator", "Mask", "Gladiator", "Bellybutton", "Handle"]
list1 = ["Crocodile", "Face", "Centurion"]
list2 = ["Sheath", "Button", "Random"]
list3 = ["Supercalifragilistic", "Nevada", "Las Vegas"]
listOfLists = [list1, list2, list3]
print(numLetterCheck("Word"))
print(cylinderVol(5, 5))
print(csvMaker(list))
print(csvList(listOfLists))