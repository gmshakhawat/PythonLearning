import datetime
today=datetime.date.today()
date="{today.day}-{today.month}-{today.year}".format(today=today)
name=["shakhawat","hossain","misty"]
amount=[112.6532,122.33,122.1]

msg= """hello {name} sir!

thank you for the application on {date} .
We are so happ to see your application 

Team
BlisndMarshall
"""

def cmsg (name,amount):
    nmsg=[]
    if len(name)==len(amount):
        i=0
        for nam in name:
            namount="%.2f" %(amount[i])
            nmsg=msg.format(
                    nam=name[i],
                    amount=namount  
                )
            i+=1
            print(nmsg)


cmsg(name,amount)            