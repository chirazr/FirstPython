print(1)
print(2)
print(3)
print(4)
print(5)

#while loop repeatedly executes a block of code as long as a given condition is True

number = 1
while number <= 5:
    print(number)
    number= number+1
print("done")

# for loop Used for iterating over items in a sequence. It is finite and ends when all items are iterated

#1st number 0
for number in range(5):
    print(number)


#start 1 to 5 (length-1) 
for number in range(1,6):
    print(number)


#characters 
#string (EOL)

for character in "chiraze":
    print(character)


#nested loops

for x in range (5):
    for y in range(5):
        print (x,y)
    