import Lessons as l
from Lessons import beginner as b

def homepage():
    if __name__ == "__main__":
        user_input = input('Welcome pupil to the Music Studio! Please enter your name: ')
        lesson_input = input("Hello " + user_input + "! Please choose a lesson from the following list: \n Beginner\n Intermediate\n Advanced\n Novice\n NOTICE:\n !! At the end of each lesson, there will be a quiz to see what you learned. \n Try and get as many questions correct as possible!!")
        if lesson_input.lower() == "beginner":
            l.beginner(lesson_input)
        elif lesson_input.lower() == "intermediate":
            l.intermediate(lesson_input)
        elif lesson_input.lower() == "novice":
            l.novice(lesson_input)

