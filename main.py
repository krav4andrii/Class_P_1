import uuid


class User():
    def __init__(self,name):
        self.name=name
        self.card=Card()

    def info(self):
        #function print vfin information about user and his card acount
        print(f'User name:{self.name}')
        self.card.info()


    def log(self):
        #function connecting loggering function of the card with class User
        self.card.loggering()

class Card:
    default_ballance=0
    default_log=[]

    def __init__(self,ballance=default_ballance,log=default_log):
        self.ballance=float(ballance)
        self.log=log


    def loggering(self):
        # log function, main problem: logging at one log for two users at same time
        if self.log==[]:
            print("You haven't any activity")
        else:
            print(f'Your log of operations:')
            for i in self.log:
                print(i)

    def info(self):
        # Print user's card general information
        # problem with uuid - it is different for that some person
        print(f'You hawe: {self.ballance} usd money')
        print(f'Your card number:{uuid.uuid4()}')
        print(f'You have:{len(self.log)} transaction')


    def earn_money(self,value,trans):
        # Earn money function
        if value>0:
            self.ballance+=value
            self.log.append(
                f'You resive {value} usd in your acount, from {trans.name} acoun total ballance is: {self.ballance}')
        else:
            self.log.append('Error: you try to do something irrational')
            print('Error: you cant earn this amount of money!')



    def transaction(self,value,recipient,trans):
        # Transaction function with loggering in both logs (self and recipient)
        if value<=self.ballance:
            self.ballance-=value
            recipient.card.earn_money(value,trans)
            self.log.append(f'You have transacted {value} usd,from your acount, to the {recipient.name} acount, total ballance'
                            f' is: {self.ballance} usd. ')
        else:
            print(f"You dont have enought money")
            self.log.append(f'Error: You dont have enought money for transacting {value} money to the {recipient.name}')
            

fedor=User('Fedor_Ovchinkin')
nikon=User('Nikodim_Rozetkin')
bank=User('Bank')

fedor.info()
fedor.card.earn_money(100,bank)
nikon.card.transaction(40,fedor,nikon)
fedor.info()
nikon.log()