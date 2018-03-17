from datetime import datetime
import time
def Today():
    import datetime
    now = datetime.datetime.now()
    today = now.date()
    pli = open('Raport.txt', 'a')
    pli.write(" "+str(today))
    pli.write("\n")
    pli.close()


def TakeTime():
    now = datetime.now()
    if len(str(now.minute))==0:
        now.minute="0"+now.minute
    now=str(now.hour) +":"+ str(now.minute)
    return  now

def WhatDid():
    think = input("What did you do in last 30 min? Be honest :)")
    return  think

def Raport(think, now):
    pli = open('Raport.txt', 'a')
    pli.write( '\t' +str(think))
    pli.write(" || "+now)
    pli.write("\n")
    pli.close()


Today()

while(True):
    time.sleep(2)
    Raport(TakeTime(), WhatDid())



