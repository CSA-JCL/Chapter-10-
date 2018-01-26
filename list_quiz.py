#Jack Lawrence
#Programming PM
#1/11/2018



def print_things():
    names = ['Jack', 'Bob', 'Tim', "Kelvin", "Joe"]
    numbers = [11, 15, 20, 56, 89]
    both = (names + numbers)
    names[3:3] = ["Tom", "Ed"]
    print(names)
    print(numbers)
    print(both)

print_things()
