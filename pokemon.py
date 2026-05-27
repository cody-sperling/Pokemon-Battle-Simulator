import random
import sys
import os


#advantage chart

advantage_chart = [[1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1,1,0.5,1],[1,0.5,0.5,1,2,2,1,1,1,1,1,2,0.5,1,0.5,1,2,1],[1,2,0.5,1,0.5,1,1,1,2,1,1,1,2,1,0.5,1,1,1],[1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5,1,1,1],[1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5,1,0.5],[1,0.5,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2,1,0.5],[2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1,2,2,0.5],[1,1,1,1,2,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,0,2],[1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1,1,2],[1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1,1,1,1,0.5,1],[1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1,0,0.5,1],[1,0.5,1,1,2,1,0.5,0.5,1,0.5,2,1,1,0.5,1,2,0.5,0.5],[1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1,1,0.5,1],[0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,0.5,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0.5,0],[1,1,1,1,1,1,0.5,1,1,1,2,1,1,2,1,0.5,1,0.5],[1,0.5,0.5,0.5,1,2,1,1,1,1,1,1,2,1,1,1,0.5,2],[1,0.5,1,1,1,1,2,0.5,1,1,1,1,1,1,2,2,0.5,1]]



#reading file
poke_list = []

file = open("pokemon.txt","r")
for n in range(1025):
    Pokemon = file.readline()
    name,element = [str(i) for i in Pokemon.split()]
    poke_list.append((name,element))

class Pokemon:
    def __init__(self,num_of_poke_selected):
        self.name = poke_list[num_of_poke_selected][0]
        self.level = random.randint(0,100)
        self.in_tourny = True
        self.element = poke_list[num_of_poke_selected][1]
        if self.element == "Normal":
            self.element_num = 0
        elif self.element == "Fire":
            self.element_num = 1
        elif self.element == "Water":
            self.element_num = 2
        elif self.element == "Electric":
            self.element_num = 3
        elif self.element == "Grass":
            self.element_num = 4
        elif self.element == "Ice":
            self.element_num = 5
        elif self.element == "Fighting":
            self.element_num = 6
        elif self.element == "Poison":
            self.element_num = 7
        elif self.element == "Ground":
            self.element_num = 8
        elif self.element == "Flying":
            self.element_num = 9
        elif self.element == "Psychic":
            self.element_num = 10
        elif self.element == "Bug":
            self.element_num = 11
        elif self.element == "Rock":
            self.element_num = 12
        elif self.element == "Ghost":
            self.element_num = 13
        elif self.element == "Dragon":
            self.element_num = 14
        elif self.element == "Dark":
            self.element_num = 15
        elif self.element == "Steel":
            self.element_num = 16
        elif self.element == "Fairy":
            self.element_num = 17
        else:
            print("Houston we have a problem")



    def set_lost(self):
        self.in_tourny = False
    def get_status(self):
        return self.in_tourny
    def play_a_round(self,other_player_obj):
        #Currently, both player lose
        #Change this function so that only one player loses
        #based on some "skill" value that both players have.





        if advantage_chart[self.element_num][other_player_obj.element_num] == 0:
            self.set_lost()


        elif advantage_chart[self.element_num][other_player_obj.element_num] == 1:

            x = random.randint(0,self.level)
            y = random.randint(0,other_player_obj.level)

            if x >= y:
                other_player_obj.set_lost()

            else:

                self.set_lost()



        elif advantage_chart[self.element_num][other_player_obj.element_num] == 0.5:
            x = random.randint(1,100)
            if x <= 55:
                self.set_lost()
            else:
                other_player_obj.set_lost()



        elif advantage_chart[self.element_num][other_player_obj.element_num] == 2:
            other_player_obj.set_lost()






        return self.in_tourny,other_player_obj.in_tourny


    def report(self,i):
        s = "Not Out"
        if self.in_tourny:
            s = "Not Out"
        else:
            s = "\033[0;31mOut\033[0;37m"
        print(f"{i} : Level {self.level} : {self.name} : {self.element} : {s}")













num = random.randint(4,8)
element_list = []
player_list = []
for i in range(num):
    r_num = random.randint(0,1024)
    p = Pokemon(r_num)
    player_list.append(p)




def report(player_list):
    print("----Tournament of Pokemon----")
    for i in range(len(player_list)):
        player_list[i].report(i)
    print("-------------------")






os.system("cls")



#main loop
count = 0

while True:

    report(player_list)

    one = int(input("Choose first player:"))
    two = int(input("Choose second player:"))
    os.system("cls")

    holder = player_list[one]
    holder2 = player_list[two]

    if one == two:
        print("You may not choose the same Pokemon twice")
        continue
    if holder.in_tourny and holder2.in_tourny:
        holder.play_a_round(holder2)
    else:
        print("Can't choose a Pokemon that already lost") 
        continue
    for i in player_list:
        if i.in_tourny:
            count+=1

    if count == 1:
        report(player_list)
        for i in player_list:
            if i.in_tourny:
                winner = i.name
                print(f"The winner is {winner}")
        sys.exit()
    count = 0








'''
import names
import random
import sys
class Person:
    def __init__(self):
        self.name = names.get_first_name()
        self.skill = random.randint(0,100)
        self.money = 5000
        self.in_tourny = True
    def set_lost(self):
        self.in_tourny = False
    def get_status(self):
        return self.in_tourny
    def play_a_round(self,other_player_obj):
        #Currently, both player lose
        #Change this function so that only one player loses
        #based on some "skill" value that both players have.


        x = random.randint(0,self.skill)
        y = random.randint(0,other_player_obj.skill)

        if x >= y:
            other_player_obj.set_lost()

            self.money += other_player_obj.money
            other_player_obj.money = 0

        else:

            other_player_obj.money += self.money
            self.money=0
            self.set_lost()
        return self.in_tourny,other_player_obj.in_tourny


#This function will loop through the player list and print
#a leaderboard with all necessary information.

    def report(self,i):
        s = "Not Out"
        if self.in_tourny:
            s = "Not Out"
        else:
            s = "\033[0;31mOut\033[0;37m"
        print(f"{i} : {self.name} : {self.money} : {s}")



def report(player_list):
    print("----Leaderboard----")
    for i in range(len(player_list)):
        player_list[i].report(i)
    print("-------------------")


num = random.randint(4,8)
player_list = []

for i in range(num):
    i = Person()
    player_list.append(i)

#You must write code that will append "num" number of
#player objects to player_list.
#done maybe?

count = 0

while 1 == 1:
    report(player_list)
#If only one player remains, print the winner and end program.
    one = int(input("Choose first player:"))
    two = int(input("Choose second player:"))
    holder = player_list[one]
    holder2 = player_list[two]

    if one == two:
        print("You may not choose the same person")
        continue
    if holder.in_tourny and holder2.in_tourny:
        holder.play_a_round(holder2)
    else:
        print("choose to people that are in the tournament") 
        continue
    for i in player_list:
        if i.in_tourny:
            count+=1

    if count == 1:
        report(player_list)
        for i in player_list:
            if i.in_tourny:
                winner = i.name
                print(f"The winner is {winner}")
        sys.exit()
    count = 0
#User should not be able to choose a player that has lost.
#User Should not be able have a player play against themselves.
#Have a function call to "play_a_round" where the two chosen
#players play a game.


'''
