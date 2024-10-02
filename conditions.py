# simple condition 
money = 2000

if money > 1000:
    print ("hello")

else : 
    print (" hi there ")

#condition 

money = -10

if money > 1000:
    print ("hello")

elif money > 0: 
    print ("hola !!")

else : 
    print (" hi there ")


#conditions

age = 28 
if age >= 18:
    print ("can drive")
else:
    print("connot drive ")


message = "can drive " if age >= 18 else "cannot"
print (message)        

# logical operators
is_hungry = True
has_money = True
restraunt_open = True 
meeting_friends = False

if is_hungry and has_money : 
    print ("i want food ")

if has_money and has_money or meeting_friends :
    print ("i want food ")