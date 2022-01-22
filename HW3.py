import math

#Used help from w3schools and stackoverflow.
def numLetterCheck():
    word = input("Enter word to test.")
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
def cylinderVol():
   height = float(input("Enter height of cylinder."))
   radius = float(input("Enter radius of cylinder."))
   volume = float(height * math.pow(radius, 2) * math.pi)
   return volume

print(numLetterCheck())
print(cylinderVol())
