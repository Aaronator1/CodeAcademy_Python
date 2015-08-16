__author__ = 'aaronmsmith'

def shout(phrase):
    if phrase == phrase.upper():
        return "You're Shouting!"
    else:
        return "Can you speak up?"


print shout(input("a "))

