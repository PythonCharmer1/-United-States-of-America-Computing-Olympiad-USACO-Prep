# By Yusuf Ali
# This is a very basic program
# It takes any string for this case the string is "aexiretretergfddxvdshbewrerevwrwvou"
# What this program does is that it takes the string an returns the number of vowels in this program

string = "aexiretretergfddxvdshbewrerevwrwvou"

def Vowels(string):
    counter = 0
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            counter += 1
        else:
            continue

    return counter

    
print(Vowels(string))