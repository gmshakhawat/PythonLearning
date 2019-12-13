import datetime
today=datetime.date.today()
date="{today.day}-{today.month}-{today.year}".format(today=today)
print(date)


class umsg():
    msg=[]
    detail=[]
    dmsg="""hello {name},
    we get your CV on {date} ,We are really to happy to see you .
    to complete your application for this job please pay {amount} tk. 
    within 72 hours 
    
    thanks 
    Team BlindMarshall
    """

    def add_user(self,name,amount):

        data ={"name":name,"amount":amount
        }


        data['date']=date
        self.detail.append(data)
    def get_detail(self):
        print(self.detail)
    def get_msg(self):
        if len(self.detail)>0:
            for data in self.detail:
                name=data['name']
                date=data['date']
                amount=data['amount']
                txt=self.dmsg
                print(txt.format(name=name,date=date,amount=amount))



ob=umsg()
ob.add_user('shakhawat',558.05)
ob.add_user('shakhawat1',558.05)
ob.add_user('shakhawat2',558.05)
ob.add_user('shakhawat3',558.05)
# ob.get_detail()
ob.get_msg()
