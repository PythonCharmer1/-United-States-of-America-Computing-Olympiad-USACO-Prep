# Python 3.7
# This Program solves the New Alphabet USACO problem
# By: Yusuf Ali


import string

special = ["@","8","(","|)","3","#","6","[-]","|","_|","|<","1","[]\/[]","[]\[]","0","|D","(,)","|Z","$","][","|_|","\/","\/\/","}{","`/","2"]

letters = []
for i in string.ascii_lowercase:
    letters.append(i)

language = dict(zip(letters,special))

def listtostring(s):
    str1 = ""
    return (str1.join(s))


def secret (language,input):
    input = input.lower()
    input_list = []
    result = []
    for i in input:
        input_list.append(i)
    for i in input_list:
        if i ==  " ":
            result.append(" ")
            continue
        if i == "!":
            result.append("!")
            continue
        if i ==".":
            result.append(".")
            continue
        if i =="?":
            result.append("?")
            continue
        result.append(language.get(i))
    return listtostring(result)

print(secret(language,"This is a good program"))