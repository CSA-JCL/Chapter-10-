#Jack Lawrence
#Programming PM
#1/22/2018

def list2():
    personal_info = ['Jack Lawrence', 'December', '17', '2001', 'Round Rock TX']
    place = personal_info[4]
    month = personal_info[1]
    x=0
    while x<5:
        print (personal_info[x])
        x = x+1
    print("I was born in",place)
    print("The month was",month)
    personal_info[1:1] = ["Kelvin", "Lorna"]
    x=0
    while x<7:
        print (personal_info[x])
        x = x+1                    
list2()
