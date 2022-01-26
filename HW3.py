from decimal import DivisionByZero
import math
import os

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
def csvMaker(lis):
    tempStr = ', '.join(lis)
    return tempStr

#Help from StackOverflow, W3Schools, and Python Docs
def csvList(listOfLists):
    f = open("././Software_Engineering/hw3/temp.csv", "w")
    for i in listOfLists:
        temp = csvMaker(i)
        f.write(temp + "\n")
    f.close()
    return os.path.abspath('temp.csv')

#help from W3Schools
def reverseCsvList(file):
    lines = file.read()
    listoflists = lines.split("\n")
    file.close()
    return listoflists
    
def divisionErrorCatcher(num1, num2):
    try:   
        temp = num1 / num2
        print("Answer=", temp, "Succesful Division.")
    except(ZeroDivisionError):
        print("Divide by zero error.")
    
#help from W3Schools
def duplicateRemover(listOfNums):
    temp = []
    for i in listOfNums:
        if i not in temp:
            temp.append(i)
    return temp

def directoryCreator():
    directory = "hw3-folder"
    parent = "/home/eburch6/Software_Engineering/hw3"
    path = os.path.join(parent, directory)
    os.mkdir(path)

lis = ["Alligator", "Mask", "Gladiator", "Bellybutton", "Handle"]
list1 = ["Crocodile", "Face", "Centurion"]
list2 = ["Sheath", "Button", "Random"]
list3 = ["Supercalifragilistic", "Nevada", "Las Vegas"]
listOfLists = [list1, list2, list3]
listOfNums = [1,5,3,5,2,1,5,9,8,7,6,1,0]
f = open("././Software_Engineering/hw3/temp.csv", "r")
print(numLetterCheck("Word"))
print(cylinderVol(5, 5))
print(csvMaker(lis))
print(csvList(listOfLists))
print(reverseCsvList(f))
divisionErrorCatcher(5,0)
print(duplicateRemover(listOfNums))
directoryCreator()