#Jack Lawrence
#Programming PM
#1/23/2018
import random
myrandomlist =[]
def MylistAppend():
    myList = [76]
    myList.append(92.3)
    myList.append("Hello")
    myList.append(True)
    myList.append(4)
    myList.append(76)
    print(myList)
MylistAppend()
def MylistCon():
    myList = [76]
    myList = myList + [92.3]
    myList = myList + ["Hello"]
    myList = myList + [True]
    myList = myList + [4]
    myList = myList + [76]
    print(myList)
MylistCon()
def Random():
    for x in range(101):
        y = (random.randrange(0,1001))
        myrandomlist.append(y)
    Average(myrandomlist)
def Average(myrandomlist):
    z = 0
    tot=0
    while z<101:
        y=myrandomlist[z]
        z = z+1
        tot+=y
        print(y)
    print (tot/100)
Random()

