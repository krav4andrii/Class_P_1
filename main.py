import uuid


class User():
    default_log='None'
    def __init__(self,name,log=default_log):
        self.name=name
        self.log=str(log)
        self.card=Card()
    def info(self):
        print(f'User name:{self.name}')
        return (self.card.info())

class Card:
    default_ballance=0
    default_uuid=uuid.uuid4()
    def __init__(self,uuid=default_uuid,ballance=default_ballance):
        self.uuid=uuid
        self.ballance=float(ballance)

    def info(self):
        #Метод виводу інформації по карті
        print(f'You hawe: {self.ballance} usd money')
        print(f'Your card number:{self.uuid}')

    def earn_money(self,value):
        #метод ініціалізаціі певної стартової сумі коштив на карту
        if value>0:
            self.ballance+=value
        else:
            print('Error: you cant earn this shit!')


    def transaction(self,value,recipient):
        #метод проведення транзакції з карти на отримувача
        if value<=self.ballance:
            self.ballance-=value
            recipient.card.earn_money(value)

            print(f'You hawe transacted {value} usd,from your card, to the {recipient} card, total ballance is: {self.ballance} ')
        else:
            print(f'You hawe not inought money')
            

fedor=User('Fedor_Ovchinkin')
nikon=User('Nikodim_Rozetkin')
fedor.info()
nikon.info()
fedor.card.earn_money(100)
fedor.card.transaction(20,nikon)
fedor.info()
nikon.info()