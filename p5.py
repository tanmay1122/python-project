wining_number=50
number=int(input("choose a number between 1 to 100 :-"))
if number==wining_number:
    print("your win the game!!!!!")
else:             # nexted if else
    print("you not win the game!!!")    
    if wining_number > number:
        print("u are too low!!")
    else:
        print("u are too high!!")
   
    