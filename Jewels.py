# By Yusuf Ali
# This program solves the Jewels and Stones programmming question
# The J string is the letters that want to find in the S sting
# The program returns the amount of letters in S that are also in J

j = "Aab"
s = "CDAbBaBcBabC"

def JewelsInStones (jewels, stone):
    list_of_jewels = []
    for i in jewels:
        list_of_jewels.append(i)

    list_of_stone = []
    for itm in stone:
        list_of_stone.append(itm)

    counter = 0
    for t in list_of_jewels:
        for x in list_of_stone:
            if x == t:
                counter += 1
            else:
                continue
    return counter

print(JewelsInStones(j,s))