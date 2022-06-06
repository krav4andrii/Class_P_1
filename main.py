import uuid


class User():
    def __init__(self,name):
        self.name=name
        self.card=Card()

    def info(self):
        print(f'User name:{self.name}')
        return (self.card.info())

    def logg(self):
        return(self.card.loggering())

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
        print(f'You hawe: {self.ballance} usd money')
        print(f'Your card number:{uuid.uuid4()}')
        print(f'You have:{len(self.log)} transaction')


    def earn_money(self,value,trans):
        #проблема з записом в лог - записи дублює в лог обох коростувачів, або ж один лог вийшов на двох
        if value>0:
            self.ballance+=value
            self.log.append(
                f'You resive {value} usd in your acount, from {trans.name} acoun total ballance is: {self.ballance}')
        else:
            print('Error: you cant earn this shit!')


    def transaction(self,value,recipient,trans):
        # Transaction function with loggering in both logs (self and recipient)
        if value<=self.ballance:
            self.ballance-=value
            recipient.card.earn_money(value,trans)
            self.log.append(f'You have transacted {value} usd,from your acount, to the {recipient.name} acount, total ballance'
                            f' is: {self.ballance} usd. ')
        else:
            print(f"You dont have enought money")
            

fedor=User('Fedor_Ovchinkin')
nikon=User('Nikodim_Rozetkin')
bank=User('Bank')

fedor.card.earn_money(100,bank)
nikon.card.earn_money(200,bank)
nikon.card.transaction(12,fedor,nikon)
nikon.info()
nikon.logg()