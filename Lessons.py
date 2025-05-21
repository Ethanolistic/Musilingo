import main as m
# Making classes for each lesson
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
            continue_input = input("Ready to move on?")
            # should print beginner 2 if input is "yes" and should print beginner 1 again if input is "no"
            if continue_input.lower() == "yes":
                print("Ok, let's move on!")
                beginner1 = True
            else:
                print("Take as much time as you need.")
                beginner1 = True
            # print beginner 2
            if continue_input.lower() == "yes":
                print("Beginner 2:\n Now that we have some fundamentals,"
                      "lets take a brief look at a concept\n called Enharmonics.\n"
                      "Enharmonics are essentially the idea that notes on a piano"
                      "can have diferent\n names. For example, another name for [C] could be B♯ or D𝄫"
                      "(double flat). Double flats look advanced but they aren't. So, for the sake of conntinuity,"
                      "we'll save them for later.")
            # if input is yes, should print review portion. If no, should print beginner 2 again.
            continue_input = input("Ready to move on?")
            if continue_input.lower() == "yes":
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
            if continue_input.lower() == "yes":
                # prompt user to start the quiz.
                continue_input = input("Are you ready for the quiz?")
                # if yes, go on to beginner_quest. If no, keep user there and reprint "Ready to move on?"
                if continue_input.lower() == "yes":
                    print("Okay! Good luck!")
                    beginner1 = True
                else:
                    print("Take as much time needed to review!")
                    beginner1 = True
        beginner_quest = False
        while beginner_quest is False:
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
            return m.homepage()
            # prompt user to return back to lesson choices.


def intermediate(lesson_input):
    inter_quest = True
    inter1 = True
    # start intermediate lesson
    if lesson_input.lower() == "intermediate":
        inter1 = False
        while inter1 is False:
            print("Welcome to the Intermediate Course! Here we'll go through the three topics of:"
                  "\n The Grand Staff\n Key Signatures\n and Time Signatures\n \n \n Intermediate 1:\n "
                  "The Grand Staff is where ALL the notes are placed on. It presents itself as a combination bettween The treble clef and the bass clef. "
                  "On these clefs are Lines and Spaces. Keep in mind that the lines and spaces are different for each clef. "
                  "For Treble clef from bottom to top, the lines are [E], [G], [B], [D], [F]. The Spaces are [F], [A], [C], [E]. "
                  "To remember the Lines, here's a simple phrase:\n [E]very [G]ood [B]oy [D]oes [F]ine. For the spaces, Just remember FACE.\n "
                  "The bass clef is not that different. The lines are [G], [B], [D], [F], [A]. The spaces are [A], [C], [E], [G]. "
                  "To remember the bass cleff lines, use this:\n [G]ood [B]oys [D]o [F]ine [A]lways. For the spaces:\n [A]ll [C]ows [E]at [G]rass.\n "
                  "Now that we've gone through the Grand Staff, let's move on to Key Signatures. ")
            continue_input = input("Ready to move on?")
            if continue_input.lower() == "yes":
                print("Alright lets go!!")
            else:
                print("That's alright. It's a new topic so take your time!")
            if continue_input.lower() == "yes":
                print("Intermediate 2:\n Remember Sharps and Flats? Well, composers use these to show how many sharps or flats there are in a key.\n "
                      "They do this by putting the sharps or flats right next to the clef sign. For example, the key of C major has no sharps or flats in the key signature.\n"
                      "This is because all of the notes in the scale are white keys. If we were to go to a fifth above C,\n"
                      "to the key of G major, there would be one sharp: [F♯]. This trend continues throughout all keys in music.\n"
                      "When you go a fifth up, a sharp is added, and when you go a fourth up, a flat is added to the key signature.")
            continue_input = input("Ready to go?")
            if continue_input.lower() == "yes":
                print("Okay cool!")
            else:
                print("No problem.")
            if continue_input.lower() == "yes":
                print("On to time signatures!\n Time signatures are what lets the performer know the timing in which to play"
                      "each note. On sheet music, the time signature is shown right next to the key signature. It's almost like"
                      "all the important information is right at the beginning of the piece!\n The Time signature of a song is usually"
                      "represented as a fraction such as: 4/4, 3/4, 2/4, 3/2.\n Other times, musicians use words like 'Common Time',"
                      "'Cut time', or 'ballad' to represent these time signatures.\n "
                      "Here are the feels associated with the time signatures:\n Ballad: 3/4\n Common Time: 4/4\n Cut Time: 2/4")
            continue_input = input("Ready to move on?")
            if continue_input.lower() == "yes":
                print("Alright! Get ready for a test!")
            else:
                print("Okay. Just be mindful that there's a test next!")
           # if continue_input.lower() == "yes":


#def novice():

#def advanced():
