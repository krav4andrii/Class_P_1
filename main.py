import uuid


class User():
    def __init__(self,name):
        self.name=name
        self.card=Card()

    def info(self):
        #function print information about user and his card acount
        print(f'User name:{self.name}')
        self.card.info()


    def log(self,N):
        #function connecting loggering function of the card with class User
        self.card.loggering(N)

class Card:
    # class Card is the argument of the class User
    default_ballance=0

    def __init__(self,ballance=default_ballance,log=None):
        self.ballance=float(ballance)
        self.log=log or []


    def loggering(self,N):
        # log function, veriable "N" means have much last operations should print, if 'N' = -1 - all log are printing.
         # operations printing in reverse chronology
        lenght=len(self.log)
        if lenght==0:
            print("You haven't any activity")
        else:
            print(f'Your log of operations:')
            if N==-1:
                for i in range(lenght-1,-1,-1):
                    print(self.log[i])
            else:
                for i in range(lenght-1,-1,-1):
                    if i==lenght-1-N:
                        break
                    else:
                        print(self.log[i])


    def info(self):
        # Print user's card general information
        print(f'You have: {self.ballance} usd money'
              f'\nYour card number:{uuid.uuid4()}'
              f'\nYou have:{len(self.log)} transaction')



    def transaction(self,value,recipient,trans):
        # Transaction function with loggering in both logs (self and recipient)
        if value<0:
            self.log.append(f"Error: You can't transacted {value} usd,from your acount!")
        else:
            if value<=self.ballance:

                self.ballance-=value
                recipient.card.ballance+=value

                self.log.append(f'You have transacted {value} usd,from your acount, to the {recipient.name} acount,'
                                f' total ballance is: {self.ballance} usd. ')
                recipient.card.log.append(f'You resive {value} usd in your acount, from {trans.name} acount total ballance '
                                        f'is: {recipient.card.ballance} usd.')
            else:
                self.log.append(f'Error: You dont have enought money for transacting {value} usd to the {recipient.name}')
            

fedor=User('Fedor_Ovchinkin')
nikon=User('Nikodim_Rozetkin')
fedor.card.ballance=1000

fedor.info()
nikon.info()
fedor.card.transaction(100.52,nikon,fedor)
fedor.card.transaction(-200,nikon,fedor)
fedor.card.transaction(300,nikon,fedor)
nikon.card.transaction(500,fedor,nikon)
fedor.info()
nikon.info()
fedor.log(-1)
nikon.log(-1)
