class grandfather():
    def skill(self):

        print("reading")
class father(grandfather):
    def fatherskill(self):
        print("making money")
class Son(father):
    def sonskill(self):
        print("sleeping")

#instance of son
son=Son()
son.fatherskill()


   