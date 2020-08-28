# By Yusuf Ali
# This program is a Basic execution of the Queue Data Type
# A Queue is a First In First Out data type
# This program uses a basic list as an Quene Data Type

Quenue = []

def add(input):
    Quenue.append(input)

def getrid():
    Quenue.remove(Quenue[0:1])

add(0)
add(3)
add(6)
add(9)
getrid()
