class Gepard:
    def __init__(self):
        self.pocet_zivotu = 9

    def je_zivy(self):
        return self.pocet_zivotu > 0

    def uber_zivot(self):
        if not self.je_zivy():
            print("Nemuzes zabit uz mrtve zvire!")
        else:
            self.pocet_zivotu -= 1

    def snez(self, jidlo):
        if not self.je_zivy():
            print("Je zbytecne krmit mrtve zvire!")
        elif jidlo == "ryba" and self.pocet_zivotu < 9:
            self.pocet_zivotu += 1
            print("Gepard spapal rybu a obnovil se mu jeden zivot.")
        else:
            print("Gepard se krmi.")
    
    def napapej_se(self):
        if not self.je_zivy():
            print("Je zbytecne krmit mrtve zvire!")
        elif self.pocet_zivotu == 9:
            print("Gepard se přejedl.")
        else:
            while self.pocet_zivotu < 9:
                self.snez("ryba")
                print(f"Současný počet životů {self.pocet_zivotu}")