def reverse(paramString):
    reverseString = ''
    for i in range(len(paramString)):
        letter = paramString[i]
        reverseString = letter + reverseString
    return reverseString

def countVowels(paramString):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    countV = 0
    for i in range(len(paramString)):
        if paramString[i] in vowels:
            countV = countV + 1
    return countV

def isPalindrom(paramString):
    reverseString = reverse(paramString)
    if paramString == reverseString:
        return True
    else:
        return False