import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "ROCK vs PAPER -> PAPER WINS \n"
      + "ROCK vs SCISSORS -> ROCK WINS \n"
      + "PAPER vs SCISSORS -> SCISSORS WINS \n")
 
while True:
     
    print("ENTER YOUR CHOICE \n 1 - ROCK \n 2 - PAPER \n 3 - SCISSORS \n")
    choice=int(input("ENTER YOUR CHOICE :"))
    while choice > 3 or choice <1:
      choice=int(input('ENTER A VALID CHOICE PLEASE ☺'))
    if choice == 1:
        choice_name= 'ROCK'
    elif choice == 2:
        choice_name= 'PAPER'
    else:
        choice_name= 'SCISSOR'
         
    print('USER CHOICE IS \n',choice_name)
    print('NOW ITS COMPUTER TURN....')
     
    comp_choice = random.randint(1,3)
     
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
         
    if comp_choice == 1:
        comp_choice_name = 'ROCK'
    elif comp_choice == 2:
        comp_choice_name = 'PAPER'
    else:
        comp_choice_name = 'SCISSOR'
    print("COMPUTER CHOICE IS \n", comp_choice_name)
    print(choice_name,'Vs',comp_choice_name)
   
    if choice == comp_choice:
        print('ITS A DRAW',end="")
        result="DRAW"  
    if (choice==1 and comp_choice==2):
        print('PAPER WINS =>',end="")
        result='PAPER'
    elif (choice==2 and comp_choice==1):
        print('PAPER WINS =>',end="")
        result='PAPER'  
    if (choice==1 and comp_choice==3):
        print('ROCK WINS =>\n',end= "")
        result='ROCK'
    elif (choice==3 and comp_choice==1):
        print('ROCK WINS =>\n',end= "")
        result='ROCK'    
    if (choice==2 and comp_choice==3):
        print('SCISSORS WINS =>',end="")
        result='SCISSORS'
    elif (choice==3 and comp_choice==2):
        print('SCISSORS WINS =>',end="")
        result='ROCK'
    if result == 'DRAW':
        print("<== ITS A TIE ==>")
    if result == choice_name:
        print("<== USER WINS ==>")
    else:
        print("<== COMPUTER WINS ==>")
    print("DO YOU WANT TO PLAY AGAIN? (Y/N)")

    ans = input().lower
    if ans =='N':
        break

print("THANK YOU FOR PLAYING")