from datetime import datetime
import time
import winsound
import getpass

username = getpass.getuser()


def Today():
    import datetime
    now = datetime.datetime.now()
    today = now.date()
    miejsce = 'C:/Users/'+username+'/Desktop/Raport.txt'
    plik = open(miejsce, 'a')
    plik.write(" "+str(today))
    plik.write("\n")
    plik.close()


def TakeTime():
    now = datetime.now()
    now=str(now.hour) +":"+ str(now.minute)
    return  now

def WhatDid():
    think = input("What did you do in last 30 min? Be honest :)")
    return  think

def Raport(think, now):
    miejsce = 'C:/Users/' + username + '/Desktop/Raport.txt'
    plik = open(miejsce, 'a')
    plik.write( '\t' +str(think))
    plik.write(" || "+now)
    plik.write("\n")
    plik.close()


Today()


while(True):
    winsound.PlaySound('pik.mp3', winsound.SND_FILENAME)
    Raport(TakeTime(), WhatDid())
    time.sleep(1800)
