from os import listdir

PerkList = listdir("./Perks")
finalPerkList = []
for i in PerkList:
    print(i.split('_')[1].split('.')[0])

# print(finalPerkList)
# print(PerkList)