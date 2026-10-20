import random
#from itertools import count


class Player:
    def __init__(self,name):
         self.name=name

class Comp(Player):
    def __init__(self,name):
        super().__init__(name)
    def display(self):
        print(f"{self.name} VS ⚔️ computer")

class Game:
    def __init__(self,player,comp):
        self.player=player
        self.comp=comp
        self.count_num=0
    def how(self):
        numbers=[]
        num1=0
        num2=0
        num3=0
        countn=input("How many number do you want input")
        if(countn=='1'):
            num1=int( input("Enter the number 1"))
            numbers.append(num1)
            print(num1)
            if(numbers[0] != self.count_num+1 ):
               print("please again input numbers")
               return self.how()
        elif(countn=='2'):
            num1 =int( input("Enter the number 1"))
            num2 =int( input("Enter the number 2"))
            numbers.append(num1)
            numbers.append(num2)
            print(num1)
            print(num2)
            if(numbers[0] != self.count_num + 1 or numbers[1] != self.count_num + 2 ):
                print("please again input numbers")
                return self.how()
        elif(countn=='3'):
            num1 = int (input("Enter the number 1"))
            num2 =int( input("Enter the number 2"))
            num3 = int(input("Enter the number 3"))
            numbers.append(num1)
            numbers.append(num2)
            numbers.append(num3)
            print(num1)
            print(num2)
            print(num3)
            if(numbers[0] != self.count_num+1 or numbers[1] != self.count_num+2 or numbers[2] != self.count_num+3):
                print("please again input numbers")
                return self.how()

        else:
            print("Sorry : can’t input this")
            return self.how()
        self.count_num = numbers[-1]
        if (self.count_num == 21):
            print("End Game")
            print("You lose")




    def computer_turn(self):
         count= random.randint(1,3)
        #للارقام العشواءية محصورة بين القيمتين اللي انت كاتبهم
         for i in range(count):
            self.count_num+=1
            print(self.count_num)
            if (self.count_num == 21):
               print("End Game")
               print("You Win🤩")
               return


    def star(self):
            while self.count_num <21:
                self.how()
                self.computer_turn()












name= input ("Enter your name")
p1= Player(name)
c1=Comp(name)
c1.display()
game1=Game(p1,c1)

game1.star()


