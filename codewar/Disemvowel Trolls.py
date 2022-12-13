# Trolls are attacking your comment section!
#
# A common way to deal with this situation is to remove all of the vowels from the
# trolls' comments,  neutralizing the threat.
#
# Your task is to write a function that takes a string and return a new string with all vowels removed.
#
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
#
# Note: for this kata y isn't considered a vowel.


def disemvowel(string):
    splitString = list(string)
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for let in string:
        for vow in vowels:
            if let == vow:
                splitString.remove(let)
    return ''.join(splitString)

print(disemvowel("This website is for losers LOL!"))

def disemvowel1(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

print(disemvowel1("This website is for losers LOL!"))


def disemvowel2(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

print(disemvowel2("This website is for losers LOL!"))


