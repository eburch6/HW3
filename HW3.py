def numLetterCheck():
    word = "Test String"
    vowel = 0 #vowel count
    consonant = 0 #consonant count

    for letter in word:
        if letter in ("aeiouAEIOU"):
            vowel += 1
        else:
            consonant += 1
    if vowel > consonant:
        return True
    elif consonant > vowel:
        return False
    else:
        return None

print(numLetterCheck())