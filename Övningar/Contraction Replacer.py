


class Main:

    def __init__(self):
        self.run = True
        self.contractions = ["Hej", "nej"]
        self.replacement = ["Hejdå", "Aldrig"] ###
        self.nummer = []


    def Replace(self, mening):
        mening = mening.replace("it is", "it's")
        mening = mening.replace("we are", "we're")
        return mening



        


                
                



       



        





main = Main()

while main.run == True:
    mening = input("Write your sentence(write Stop to end)").capitalize()

    if mening == "Stop":
        print("Quiting")
        quit()

    else:
        mening = main.Replace(mening) 
        print(mening)

        