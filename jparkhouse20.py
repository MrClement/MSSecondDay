def do_something():
    question = raw_input("We are playing mind the city. press enter. ")
    t = 0
    while t < 1:
        question = raw_input("guess the continent")
        if question == "antarctica":

            print ("What the hell are you thinking?")
        elif question == "south america":
            question = raw_input("Yes. guess the contry")
            t = 1
        else:
            print ("no. try again")

    while t < 2:
        question = raw_input("guess the country")
        if question == ("suriname"):

            question = raw_input("yes guess the city")
            t = 2
        else:
            print ("no. try again")
    while t < 3:
        question = raw_input("guess the city")
        if question == ("paramaribo"):
            ("wow. I am guessing you either looked this up on the internent or tortured me until I told you.")
            t = 3
        else:
            print ("no.")
    print ("you won")
do_something()
