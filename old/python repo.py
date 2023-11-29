speed_mi = input("Enter speed in Miles: ")
speed_km = 1.6*float(speed_mi)
print(speed_mi, "miles per hour equals", speed_km, "kilometers per hour.")
if speed_km >= 10600:
    print("Warning! You're above the limit.")
    print("Please come back whole again. XXX ")
elif speed_km <= 50:
    print("Warning! You're going too slow!")
else:
    print("You're within the limit.")
    print("See you!")


month = input("enter month")

if month == "December" or month == "January" or month == "February" or month == "March" or month == "April":
    print("Winter is here.")
elif month == "May" or month == "June" or month == "July" or month == "August":
    print("Summer is here.")
else:
    print("Winter is close.")


i = 0
while i < 3:
    print("Count")
    i = i+1


count = 0
while count < 10:
    print('*'*(4+count))
    count = count+1
    if count == 5:
        print("$#_-_&^_#$")
****
*****
******
*******
********
$#_-_&^_#$
*********
**********
***********
************
*************


carmake = input("Enter car make: ")
while carmake != "quit":
    if carmake == "Toyota":
        print("The price is 4000 to 1000.")
    elif carmake == "Honda":
        print("The price is Honda.")
    elif carmake == "Suzuki":
        print("The price is cheap")
    else:
        print("That's not a Japanese car.")
    carmake = input("Enter car make: ")
Enter car make: Honda
The price is Honda.
Enter car make: Suzuki
The price is cheap
Enter car make: Toyota
The price is 4000 to 1000.
Enter car make: lkjasd
That's not a Japanese car.
Enter car make: quit



import random
correctnum = random.randint(1, 20)

num = input("Guess between 1 and 20. Z to quit ")
num = int(num)
while num != 0:
    if num == correctnum:
        print("You WIN")
    elif num == "Z":
        break
    else:
        input("Guess between 1 and 20. Z to quit ")
        num = int(num)

GAME not working now




import random
grades = [75, 71, 82, 90, 68, 65, 88, 73, 77, 51]

id = random.randint(0, 9)
print("Enter")
print(grades[id])

Prints the nth random number in the list 



grades = [75, 71, 82, 90, 68, 65, 88, 73, 77, 51]
i = 0
while i < len(grades):
    if grades[i] >= 80:
        print((grades[i]), "=", "A")
    elif grades[i] < 80 and grades[i] > 70:
        print((grades[i]), "=", "B")
    else:
        print((grades[i]), "= C")
    i = i+1
print("The machine is at your service.")

75 = B
71 = B
82 = A
90 = A
68 = C
65 = C
88 = A
73 = B
77 = B
51 = C
The machine is at your service.


import requests
kittens = requests.get("http://placekitten.com/")
print(kittens.text[559:1000])

                      __     __,
                      \,`~"~` /
      .-=-.           /    . .\
     / .-. \          {  =    Y}=
    (_/   \ \          \      / 
           \ \        _/`'`'`b
            \ `.__.-'`        \-._
             |            '.__ `'-;_
             |            _.' `'-.__)
              \    ;_..-`'/     //  \
              |   /  /   |     //    |
              \  \ \__)   \   //    /
               \__)