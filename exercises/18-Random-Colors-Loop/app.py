import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():

    #your loop here
    for i in range(10):
        num_Ale = random.randint(0,4)
        print(get_color(num_Ale))




print(get_allStudentColors())