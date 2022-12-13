# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).
#
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

# alphabet = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w', 'e', 'r',
#             't', 'y', 'u', 'i', 'o', 'p']
alphabet = "abcdefghijklmnopqrstuvwxyz"
def is_pangram(s):

    for i in alphabet:
        if i not in s.lower():
            return False
    return True

print(is_pangram("This isn't a pangram!"))