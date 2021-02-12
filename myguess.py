secret = "baby"
guess = ""
guess_count = 3

while guess_count > 0:
    guess = input(("Someone that was just being delivered is called a: "))
    if guess == secret:
        print("Genius you got the response " + secret + " right!")
        break
    else:
        guess_count-=1
        print("Wrong i gave you a clue already dude. You have %d left!" %guess_count)

    
