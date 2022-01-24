from random import *
import os
from gtts import gTTS
def heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")
def Ask_Input(a):
    """
    """
    a=str(input("=>=>=>"))
    return a
def Reader(f: str,l:list):
    """Information from file f to list l
    """
    file=open(f,"r", encoding= "utf-8-sig")
    for i in file:
        l.append(i.strip())
    file.close()
    return l
def Random_Word(l:list):
    """
    """
    Number = randrange(1,10)
    Word=l[Number]
    return Word
def Line_Saving(f:str,line:str):
    file=open(f,"a",encoding="utf-8-sig")
    file.write(line+"\n")
    file.close()
def New_Word(f:str,line:str):
    """
    """
    with open(f,"a",encoding="utf-8-sig") as file:
        file.write(line+"\n")
def Translation(l1:list,l2:list):
    word=input("What word do you want?")
    if word in l1:
        tolk=l2[l1.index(word)]
        print(word+"-"+tolk)
    elif word in l2:
        tolk=l1[l2.index(word)]
        print(word+"-"+tolk)
    else:
        print("Not found")
def Test(l1:list,l2:list,a:str):
    """
    """
    l=[]
    q=0
    Point=0
    while True:
        q+=1
        if q==10:
            break
        c=Random_Word(l1)
        while l1.count(c)==1:
            c=Random_Word(l1)
        l.append(c)
        print(c)
        print("Write translate")
        Answer=Ask_Input(a)
        if l1.index(c)==l2.index(Answer):
            print("Right!")
            Point+=1
        else:
            print("Wrong!")
    P=10/Point*100
    print("Your check is"+P)
    return P
