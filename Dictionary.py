from module1 import *
a=" "
eng=[]
rus=[]
eng = Reader("eng.txt",eng)
rus = Reader("rus.txt",rus)
print("Welcome to Dictionary!")
while True:
    print("=~     Main Menu    ~=")
    print("=~     !Actions!    ~=")
    print("=~   Instructions   ~=")
    print("=~     Hear Word    ~=")
    print("=~    Translation   ~=")
    print("=~     Add Words    ~=")
    print("=~Check your English~=")
    print("=~Check your Russian~=")
    Answer=Ask_Input(a)
    if Answer.lower()=="instructions":
        True
    elif Answer.lower()=="translation":
        Translation(eng,rus)
    elif Answer.lower()=="hear word":
        print("In what language do you want to hear the word?")
        lang=Ask_Input(a)
        print("Word")
        word=Ask_Input(a)
        heli(lang,word)
    elif Answer.lower()=="add":
        print("Write english word")
        Word1=Ask_Input(a)
        New_Word("eng.txt",Word1,eng)
        print("Write russian translation")
        Word2=Ask_Input(a)
        New_Word("rus.txt",Word2,rus)
    elif Answer.lower()=="check english":
        True
    elif Answer.lower()=="check russian":
        True
