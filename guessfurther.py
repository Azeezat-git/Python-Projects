from random import randint

goal = randint(1,10) 

guess_count = 3

while guess_count > 0:     
    guess = int(input("Please guess the number:"))     
    if guess == goal:         
        print("Congratulations you won! You got the random number " + str(goal) + " correctly")         
        break     
    
    elif  guess < goal:         
        guess_count-=1         
        print(" Too low! Incorrect! You have  %d tries left!"%guess_count)
        #break

    elif guess > goal:         
        guess_count-=1         
        print("Too high! Incorrect! You have %d tries left!"%guess_count)
        #break
    
    #else:         
        #guess_count-=1         
        #print("Incorrect! %d guess_count left!"%guess_count)

