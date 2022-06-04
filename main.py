import uuid


class User():
    def __init__(self,name):
        self.name=name
        self.card=Card()

    def info(self):
        print(f'User name:{self.name}')
        return (self.card.info())

    def logg(self):
        return (self.card.loggering())

class Card:
    default_ballance=0
    default_uuid=uuid.uuid4()
    default_log=[]
    def __init__(self,uuid=default_uuid,ballance=default_ballance,log=default_log):
        self.uuid=uuid
        self.ballance=float(ballance)
        self.log=log

    def loggering(self):
        if self.log==[]:
            print("You hawen't any activity")
        else:
            print(f'Your log of operations:')
            for i in self.log:
                print(i)

    def info(self):
        #Метод виводу інформації по карті
        print(f'You hawe: {self.ballance} usd money')
        print(f'Your card number:{self.uuid}')
        print(f'You have:{len(self.log)} transaction')


    def earn_money(self,value):
        #метод ініціалізаціі певної стартової сумі коштив на карту
        if value>0:
            self.ballance+=value
            self.log.append(f'You resive {value} usd in your acount,total ballance is: {self.ballance}')
        else:
            print('Error: you cant earn this shit!')


    def transaction(self,value,recipient):
        #метод проведення транзакції з карти на отримувача
        if value<=self.ballance:
            self.ballance-=value
            recipient.card.earn_money(value)
            self.log.append(f'You hawe transacted {value} usd,from your acount, to the {recipient} acout, total ballance'
                            f' is: {self.ballance} usd. ')
        else:
            print(f'You have not enought money')
            

fedor=User('Fedor_Ovchinkin')
nikon=User('Nikodim_Rozetkin')
fedor.info()
nikon.info()
nikon.logg()
fedor.card.earn_money(100)
fedor.card.transaction(20,nikon)
fedor.logg()

