# Making classes for each lesson
def welcome():
    user_input = input("Welcome Pupil to the Music Studio! Please enter your name: ")
    Username = user_input
    lesson_input = input(
        "Hello " + Username + "! Please choose a lesson from the following list: \n "
                              "Beginner\n Intermediate\n Advanced\n Novice\n NOTICE:\n "
                              "!! At the end of each lesson, there will be a quiz to see what you learned. \n "
                              "Try and get as many questions correct as possible!!"
                              "")



def beginner(lesson_input):
    beginner_quest = True
    beginner1 = True
    # start beginner lesson
    if lesson_input.lower() == "beginner":
        beginner1 = False
        while beginner1 is False:
            print(
                "Beginner 1:\n Ok let's begin!\n Let's start with the layout of a piano. If you were to look up an image,\n you'd notice that there are a mixture of black and white keys. The black keys are known as sharps or flats, and the\n white keys are known as naturals. Sharps can be notated using the [♯] symbol,\n Flats can be notated using the [♭] symbol, and naturals can be notated using the [♮] symbol.")
            # takes in user input to proceed
            Continue_input = input("Ready to move on?")
            # should print beginner 2 if input is "yes" and should print beginner 1 again if input is "no"
            if Continue_input.lower() == "yes":
                print("Ok, let's move on!")
                beginner1 = True
            else:
                print("Take as much time as you need.")
                beginner1 = True
            # print beginner 2
            if Continue_input.lower() == "yes":
                print("Beginner 2:\n Now that we have some fundamentals,"
                      "lets take a brief look at a concept\n called Enharmonics.\n"
                      "Enharmonics are essentially the idea that notes on a piano"
                      "can have diferent\n names. For example, another name for [C] could be B♯ or D𝄫"
                      "(double flat). Double flats look advanced but they aren't. So, for the sake of conntinuity,"
                      "we'll save them for later.")
            # if input is yes, should print review portion. If no, should print beginner 2 again.
            Continue_input = input("Ready to move on?")
            if Continue_input.lower() == "yes":
                print("Ok lets go!!\n \nSince this is the beginning and you should be new, let's do some review!\n \n"
                      "As we've covered, there are three types of notes on a piano: Sharps[♯],\n Flats[♭], and Naturals[♮]."
                      "The usage of them changes depending on the context in the key signature. If you are playing in a sharp"
                      "key, then you wou ld most likely use sharps for accidentals. Naturals can be used in both because it lets"
                      "the player know that the note is technically 'outside' of the key. Now knowing how to use sharps,\n flats,"
                      "and naturals, you should know how to identify notes on a piano. Lets say that you play an E♭. Another way "
                      "to identify that note is D♯. For naturals, if D♯ is in the key of the piece that is\n being analyzed, and"
                      "a D natural accidental shows up, it should look like this: [D♮]")
            else:
                print("No worries. You got all the time in the world.")
                beginner1 = True
            # review portion
            if Continue_input.lower() == "yes":
                # prompt user to start the quiz.
                Continue_input = input("Are you ready for the quiz?")
                # if yes, go on to beginner_quest. If no, keep user there and reprint "Ready to move on?"
                if Continue_input.lower() == "yes":
                    print("Okay! Good luck!")
                    beginner1 = True
                else:
                    print("Take as much time needed to review!")
                    beginner1 = True
        while beginner_quest is True:
            print("Okay lets get started!")
            # question 1
            quest1 = input("What is another name for [C♯]? \n A. D flat\n B. C natural\n C. B double flat")
            if quest1.lower() == "a":
                print("Good job!")
            elif quest1.lower() == "b" or "c":
                print("Sorry. Thats not the correct answer was A")
            # incase user enters jibberish
            else:
                print("Please enter a valid option")
            # question 2
            quest2 = input("What is another name for [A♯]?\n A. G flat\n B. B flat\n C. F sharp")
            if quest2.lower() == "b":
                print("Awesomesauce!")
            elif quest2.lower() == "a" or "c":
                print("Aw man! The correct answer was B")
            # incase user enters jibberish
            else:
                print("Please enter a valid option")
            # question 3
            quest3 = input("What is another name for [F♭]?\n A. F sharp\n B. E flat\n C. E natural")
            if quest3.lower() == "c":
                print("Amazing!")
            elif quest3.lower() == "a" or "b":
                print("C'mon dude. The right answer was C :(")
            # incase user enters jibberish
            else:
                print("Please enter a letter!")
                beginner_quest = True

            # prompt user to return back to lesson choices.
            home_page = input("Press H to return home!")
            if home_page.lower() == "h":
                return welcome()


def intermediate(lesson_input):
    inter_quest = True
    inter1 = True
    # start intermediate lesson
    if lesson_input.lower() == "intermediate":
        inter1 = False


#def novice():

#def advanced():