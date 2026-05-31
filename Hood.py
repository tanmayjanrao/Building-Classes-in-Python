class Hood():

    def __init__(self,name):
        self.name=name
        self.intro_yn()
        

    def intro_yn(self):
        print(f"Welcome to the Hood {self.name}!!\nyeah lets see if your ahh can survive in this B\n")        

        input("Press Enter to Start...")

        self.story()
    
    def story(self):
        user=input("""your ungrateful ahh gets to see another morning , ya stepped out to get some milk (really you only wanted to see if your dads there, anyways  There comes 2 YN's , gun on cashier what will you do in this situation?
        1. shut up and stay quit
        2. be a hero    
        3. Run away


            """)
        if user=="1":
            print("You get to see another morning!! ")
        elif user=="2":
            print(f"BOOOOMMMMM ..... rest in peace to {self.name} you got hit by a bazooka...... Kaboom, kablaow, kaboom ")
        elif user=="3":
            print("Good job lets turn your life around..")
        else:
            print("Bro can't even follow instructions")


person=Hood("TJ")
