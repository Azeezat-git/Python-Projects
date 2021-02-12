print("Hello There! You are welcome to ZEE Gaming Center")

name = input("What is your name: ")
age = input("How old are you? ")

lives = 10

if int(age) >= 18:
    print("Good", name, "you are old enough to play")

    wants_to_play = input("Dou you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's play. You are starting with", lives, "Lives")

        left_or_right = input("Do you want to go left or right (Left/Right)? ").lower()
        if left_or_right == "left":
            ans = input("Do you want to swim around or across (Across/Around) ?").lower()
            if ans == "Around":
                print("You went around and reached the other side o the lake")

            elif ans == "Across":
                print("You went across the river and you lost 5 lives")
                lives -= 5
            ans =input("You reached a junction, do you go to a house or river (House/River)? ").lower
            if ans == "house":
                print("You got to the house and got bit by their dog, you lost 5 lives").lower
                lives -= 5

                if lives <= 0:
                    print("You lost all lives and out of the game!")
                
                else:
                    print("You survived against all odds warrior")
            
            
            else:
                print("You go to a river, fell in, and drowned. You lost!")





        else:
            print("Sorry", name, "Right isn't always the right way to go!")
    



    else:
        print("Have a good day,", name)


else:
    print("Sorry", name, "you are too young for this")

