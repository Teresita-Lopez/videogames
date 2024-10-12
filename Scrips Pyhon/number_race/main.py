'''Scrips description: Number race
dev: Teresita López
date: 13/09/24
'''

from random import randint
import os

 
status_menu = True

def main_menu():
    global statues_opts
    status_opts = True 
    print (":::MAIN MENU:::")
    print ("[1].START GAME")
    print ("[2].Help")
    print  ("[3].exit")  
    
    while status_opts:
        opt = int (input(" Press any option: "))
        if opt < 1 or opt > 3:
            print(" Error. press any options between1 and 3")
    
        else: 
            status_opts = False 
    return opt 
while status_menu:
    os.system('Clear')
    op=main_menu()
    if op==1:
        os.system('Clear')
        print(":::Welcome to number to race:::")
        
        
        players = int(input("Press number of players [1,4]:   "))
        
        print (":::level main::::")
        print("[1].Basic")
        print("[2].Intermediant")
        print("[3].Advance") 
        print("[4].Expert")
        opt = int(input("Press any option:   "))
         
        if opt == 1:
            pos= 20
        elif opt == 2:
            pos= 30
        elif opt == 3:
            pos= 50  
        else:
            pos = 100  
            
            
        # Start Game 
        status_game= True 
        roll_count =0
        roll_acum=0
        while status_game:
            key = input ("Press any key to roll dice...")
        
            dice1 = randint (1,6)
            dice2 = randint (1,6) 
            
            
            print (f"Dice 1: {dice1}")
            print (f"Dice 2: {dice2}")
            total = dice1 + dice2
            print (f"Total:{total}")
            
            roll_count  += 1  # roll_count +1
            roll_acum +=  total # roll_acum + total
            print (f"Total games:{roll_acum}")
            
            
            if roll_acum >= pos:
                print(":::YOU WIN, CONGRATULATION::: ")
                status_game = False 
                
            os.system('pause')
                
        print(":::STATITICS:::")
        print(f"TOTAL ROLLS: {roll_count}")        
        print(f"TOTAL DICES: {roll_acum}")     
                    
    
        key= input("Press any key to go to the main menu")
    elif op ==  2:
        print(" Help under construction") 
        key = (" Press any key to go to the main menu ")
    else: 
        print (" see 'u later")  
        key = input("press any key to exit...") 
        break  
