class MonsterFight():
    import random
    import time
    player_health = 100
    player_mana = 100
    monster_health = 100
    fight = ""
    
    def __init__(self):
        pass
     
    def attack(self):
        import random
        from IPython.display import clear_output
        import time
        if self.monster_health >=1:
            x = random.randint(1,10)
            if x > 2:
                if self.monster_health <=0:
                    print ("The Monster is DEAD")
                    self.fight = False
                else:
                    self.monster_health-=20
                    print ('You hit the monster for -20 health') #\nMonster health:', self.monster_health)
#                    time.sleep(3)
#                    clear_output()
            elif x <= 2:
                self.player_critical()
                if self.monster_health <=0:
                    print ("The Monster is DEAD")
                    self.fight = False
                else:    
                    print ('You have dealt a CRITICAL for -40 health') #\nMonster health:',  self.monster_health)
#                    time.sleep(3)
#                    clear_output()
        else:
            return 'The monster is dead'
        
    
    
    def heal(self):
        import random
        x = random.randint(1,10)
        if x > 2 and self.player_health < 100:
            self.player_health+=20
            self.player_mana-=10
            if self.player_health > 100:
                z = abs(100 - self.player_health)
                self.player_health-=z
                print("\n")
                print(f"You have casted heal. You have recovered {z} health \n \nYour health:", self.player_health, "\nYour mana:", self.player_mana)
            else:
                print(f"You have casted heal. You have recovered 20 health \n \nYour health:", self.player_health, "\nYour mana:", self.player_mana)
        elif x <= 2 and self.player_health < 100:
            self.critical_heal()
            self.player_mana-=10
            if self.player_health > 100:
                z = abs(100 - self.player_health)
                self.player_health-=z
                print("\n")
                print(f"You have casted a CRITICAL HEAL. You have recovered {z} health \n \nYour health:", self.player_health, "\nYour mana:", self.player_mana)
            else:
                print(f"You have casted heal. You have recovered 40 health \n \nYour health:", self.player_health, "\nYour mana:", self.player_mana)
        else:
            print("You are are full health already")
        
    def monster_attack(self):
        import random
        x = random.randint(1,10)
        if x > 1 and self.player_health > 0:
            self.player_health-=10
            if self.player_health <=0:
                print("The MONSTER has hit you for 10 damage and killed you! \nGAME OVER!")
            else:
                print("The MONSTER has hit you for 10 damage.")
        elif x ==1 and self.player_health >0:
            self.monster_critical()
            if self.player_health <=0:
                print("The MONSTER has hit you for 10 damage and killed you! \nGAME OVER!")
            else:
                print("The MONSTER has hit you with a critical! Dealing 20 damage.")

            
    
    def escape():
        self.fight = False
        pass
    
    def fight_or_run(self):
        import time
        from IPython.display import clear_output
        while True: 
            x = int(input("You have encountered a monster. Will you fight or run? \n1.Fight \n2.Run \n"))
            if x == 1:
                self.fight = True
                print("You have chosen to fight!")
                break
            elif x == 2:
                self.fight = False
                print("You have chosen to run!")
                break
            else:
                print("Your entry is invalid")
                time.sleep(2)
                clear_output()
                
    
    def selection(self):
        import time
        from IPython.display import clear_output
        while self.fight == True:
            print("Your health:", self.player_health, "\tMonster health:", self.monster_health, "\nYour mana:", self.player_mana)
            time.sleep(1)
            x = int(input("What would you like to do? \n1.Attack \t2.Heal \n3.Use item \t4.Escape \n"))
            if x == 1:
                self.attack()
                if self.monster_health > 0:
                    self.monster_attack()
                else:
                    print("The MONSTER is DEAD!")
                    break
                time.sleep(3)
                clear_output()
#                print("Your health:", self.player_health, "\tMonster health:", self.monster_health, "\nYour mana:", self.player_mana)
            elif x == 2:
                self.heal()
                print("\n")
                self.monster_attack()
                time.sleep(4)
                clear_output()
#                print("Your health:", self.player_health, "\tMonster health:", self.monster_health, "\nYour mana:", self.player_mana)
            elif x == 3:
                clear_output()
                self.item_selection()
            elif x == 4:
                self.escape()
            else:
                print("Your entry is invalid!")
                
    def item_selection(self):
        import time
        from IPython.display import clear_output
        print("Your health:", self.player_health, "\tMonster health:", self.monster_health, "\nYour mana:", self.player_mana)
        x = int(input("What item would you like to use? \n1.Health Potion(+50 HP) \t2.Mana Potion(+50 MP) \n3.Stuffed Unicorn \t4.Back \n"))
        if x == 1:
            if self.player_health < 100 or self.player_health > 50:
                self.hp_potion()
                z = abs(100 - self.player_health)
                self.player_health-=z
                y = abs(50-z)
                print("\n")
                print(f"You have recovered {y} hp by using a HP Potion!")
            elif self.player_health <= 50:
                self.hp_potion()
                print("You have recovered 50 hp by using a HP Potion!")
            else:
                print("You are already at full health")
            time.sleep(3)
            clear_output()  
        elif x == 2:
            self.mp_potion()
            if self.player_mana > 100:
                z = abs(100 - self.player_mana)
                self.player_mana-=z
                print("\n")
                print(f"You have recovered {z} mp by using a MP Potion!")
            else:
                print("You have recovered 50 mp by using a HP Potion!")
            time.sleep(3)
            clear_output()          
        elif x == 3:
            self.stuffed_unicorn()
        elif x == 4:
                pass
        else:
            print("Your entry is invalid")
    
    def player_critical(self):
        self.monster_health-=40
    
    def monster_critical(self):
        self.player_health-=20
    
    def critical_heal(self):
        self.player_health+=40
    
    def hp_potion(self):
        self.player_health+=50
        
    def mp_potion(self):
        self.player_mana+=50

    def stuffed_unicorn(self):
        self.fighting = False
    #######################################################
    
    class Route():
    
    
    def __init__(self):
        pass

    def left_or_right(self):
        print("_____________________________________________")
        print("               |          |                  ")
        print("               | <- or -> |                  ")
        print("    left       |          |       right      ")
        print("              /            \                 ")
        print("             /              \                ")
        print("            /                \               ")
        print("           /                  \              ")
        print("-----------                    --------------")
        
    def dead_end(self):
        print("_____________________________________________")
        print("               |          |                  ")
        print("               | DEAD END |                  ")
        print("               |   NERD   |                  ")
        print("              /            \                 ")
        print("             /   GO BACK    \                ")
        print("            /                \               ")
        print("           /                  \              ")
        print("===========                    ==============")
        
    def go_straight(self):
        print("_______________               _______________")
        print("               |             |               ")
        print("               |             |               ")
        print("               |             |               ")
        print("               |             |               ")
        print("               |             |               ")
        print("               |             |               ")
        print("               |             |               ")
        print("===============               ===============")
##################################################
real_fight = MonsterFight()

import time
from IPython.display import clear_output
import random

real_fight.fight_or_run()
time.sleep(2)
clear_output()
while real_fight.fight == True:
    real_fight.selection()

    
