beginner1 = True
user_input = input("Welcome Pupil to the Music Studio! Please enter your name: ")
Username = user_input
lesson_input = input("Hello " + Username + "! Please choose a lesson from the following list: \n Beginner\n Intermediate\n Advanced\n Novice\n NOTICE:\n !! At the end of each lesson, there will be a quiz to see what you learned. \n Try and get as many questions correct as possible!!")
if lesson_input.lower() == "beginner":
    while beginner1:
        print(
            "Beginner 1:\n Ok let's begin!\n Let's start with the layout of a piano. If you were to look up an image,\n you'd notice that there are a mixture of black and white keys. The black keys are known as sharps or flats, and the\n white keys are known as naturals. Sharps can be notated using the [♯] symbol,\n Flats can be notated using the [♭] symbol, and naturals can be notated using the [♮] symbol.")
        Continue_input = input("Ready to move on?")
        if Continue_input.lower() == "yes":
            print("Ok, let's move on!")
            beginner1 = False
        else:
            print("Take as much time as you need.")
