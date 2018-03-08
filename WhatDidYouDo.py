from datetime import datetime
import time

def TakeTime():
    now = datetime.now()
    return  now

def WhatDid():

    think = input("What did you do in last 30 min? Be honest :)")

    return  think





def Raport(think, now):

    #lista = [think, now]

    #print (lista)
    global think
    global now
    print (think)
    print (now)

TakeTime()
WhatDid()
Raport()
