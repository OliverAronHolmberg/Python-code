class Main:
    def __init__(self):
        self.run = True
        self.contractions = ["Hej", "nej"]
        self.replacement = ["Hejdå", "Aldrig"]
    
    def ReplaceCon(self, text):
        print("Original text:", text)
        
      
        for contraction, replacement in zip(self.contractions, self.replacement):
           
            text = text.replace(contraction, replacement)
        
        print("Replaced text:", text)
        return text


main = Main()

while main.run:
    mening = input("Skriv din mening (skriv Stop för att avsluta): ").capitalize()

    if mening == "Stop":
        print("Avslutar")
        break
    else:
        
        replaced_text = main.ReplaceCon(mening)
        print("Resultat:", replaced_text)