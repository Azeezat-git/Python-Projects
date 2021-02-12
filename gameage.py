print("Hello There! You are welcome to Zee Online Gaming Center")

name = input("What is your name? ")
age = input("How old are you age? ")

lives = 10

if int(age) >= 18:
    print("Welcome", name, "you are old enough to play")
    

    wants_to_play = input("Do you want to play? (Yes/No) ").lower()
    if wants_to_play == "yes":
        print("You are starting with", lives, "Lives. So let's play")
       
        left_or_right= input("Do you wanna go left or right (Left/Right)").lower()
        if left_or_right == "right":
            print("You fell down and lost! Right isn't the only way!")
        
        elif left_or_right == "left":
            ans = input("Nice, you followed the path and reach a lake.....Do you swim or go across (Across/around)? ").lower()

            if ans == "around":
                print("You went around and reach the other side of the lake")

            elif ans == "across":
                print("Sorry....You managed to get across, but were bit by a fish and lost 5 lives.")
                lives -= 5
            ans = input("You notice ahouse and a river, which do you go? (River/House)? ").lower()
            if ans == "house":
                print("You go to the house and got bit by their dog, you lose 5 lives!")
                lives -= 5

                if lives <= 0:
                    print("You now have 0 lives and you lost the game")
                else:
                    print("You survived against all odds warrior!")
            else:
                print("You fell in the river and lost!")



          
        else:
            print("Your input is wrong!")
    
    
    
    else:
        print("Have a good day", name)







else:
     print("Sorry", name,"you are not old enough to play.")   



