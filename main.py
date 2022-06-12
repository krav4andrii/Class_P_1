import uuid


class User():
    def __init__(self,name):
        self.name=name
        self.card=Card()

    def info(self):
        #function print vfin information about user and his card acount
        print(f'User name:{self.name}')
        self.card.info()


    def log(self,H):
        #function connecting loggering function of the card with class User
        self.card.loggering(H)

class Card:
    default_ballance=0

    def __init__(self,ballance=default_ballance,log=None):
        self.ballance=float(ballance)
        self.log=log or []


    def loggering(self,H):
        # log function, veriable "H" means have much operations shoud function print, if 'H' = -1 - all log are printing.
        lenght=len(self.log)
        if lenght==0:
            print("You haven't any activity")
        else:
            print(f'Your log of operations:')
            if H==-1:
                for i in range(lenght-1,-1,-1):
                    print(self.log[i])
            else:
                for i in range(lenght-1,-1,-1):
                    if i==lenght-1-H:
                        break
                    else:
                        print(self.log[i])


    def info(self):
        # Print user's card general information

        print(f'You have: {self.ballance} usd money')
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

fedor.card.earn_money(200,bank)
fedor.card.earn_money(300,bank)
fedor.card.transaction(400,nikon,bank)
fedor.card.earn_money(500,bank)
fedor.card.transaction(180,nikon,fedor)
fedor.info()
nikon.info()
fedor.log(23)
nikon.log(-1)