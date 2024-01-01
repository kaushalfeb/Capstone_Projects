import os
from time import sleep

rec = tuple()
stud = []
for x in range(5):
    name = input("Enter name of subject ")
    marks = int(input("Marks: "))
    rec = (name,marks)
    stud.append(rec)
    print("Added")
print(rec)
os.system('cls')

for y in range(10):
    print("Sorting the list marks wise")
    os.system('cls')
    print("Sorting the list marks wise.")
    os.system('cls')
    print("Sorting the list marks wise..")
    os.system('cls')
    print("Sorting the list marks wise...")
    os.system('cls')


for j in range(len(stud)):
    for i in range(len(stud)-j-1):
        if stud[i][1] > stud[i+1][1]:
            temp = stud[i]
            stud[i] = stud[i+1]
            stud[i+1] = temp

for x in stud:
    print(x)