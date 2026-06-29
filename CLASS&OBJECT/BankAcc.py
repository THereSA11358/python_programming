class BankAcc:
    def __init__(self,bal,name):
        self.name=name
        self.__bal=bal
    #getters
    def get_bal(self):
        return self.__bal
acc=BankAcc(1000,"hahha")
print(acc.get_bal())
