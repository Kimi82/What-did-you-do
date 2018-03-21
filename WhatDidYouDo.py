from datetime import datetime
import time
import winsound





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
    winsound.PlaySound('pik.mp3', winsound.SND_FILENAME)
    Raport(TakeTime(), WhatDid())
    time.sleep(5)

