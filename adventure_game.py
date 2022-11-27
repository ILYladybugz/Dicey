name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go LEFT or RIGHT. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can WALK around it or SWIM accross? Type WALK to walk around and SWIM to swim accross. ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and died of dehydration.")

    else:
        print("Not a valid option. You loose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to CROSS it or head BACK? ")

    if answer == "back":
        print("You head back and loose your way")

    elif answer == "cross":
        print("You cross the bridge and meet a stranger. Do you talk to them? (Yes/No) ")

        if answer == "yes":
            print("You talk to the stranger and make a new friend. You WIN!")
        
        elif answer =="no":
            print("You ignore the stanger and they are offended. You loose!")
        
        else:
            print("Not a valid option. You loose.")  

    else:
        print("Not a valid option. You loose.")  

else:
    print("Not a valid option. You loose.")

print("Thanks for playing", name)