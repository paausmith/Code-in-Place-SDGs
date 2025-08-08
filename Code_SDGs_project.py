"""
This program allows the user to get to know the Sustainable Development Goals (SDG) and
how they can contribute to them with achievable actions. The user will have a lovely guide, a dog named Chonchis
who will move to the correspondent SDG which the user selects to learn about.
"""

# Importar las bibliotecas
import tkinter
from PIL import ImageTk, Image
import time
import random

# Constantes
CANVAS_SIZE = 810

def main():
    # 1.1 Create canvas
    canvas = make_canvas(CANVAS_SIZE, CANVAS_SIZE, "Sustainable Development Goals")
    # 1.2 Select default background image
    image = Image.open("Recursos digitales/SDG Wheel_Transparent_WEB.png")
    backgroundImage = ImageTk.PhotoImage(image)
    background = canvas.create_image(40, 40, image=backgroundImage, anchor="nw")
    # 2.1 Introduction: ask the user their name and give a brief intro, then delete and place chonchis
    name = input("Enter your name: ")
    welcome_1 = canvas.create_text(90, 250, font="Corbel 20",
                                   text="Hello " + name + " you are going to learn how to contribute to the",
                                   anchor="nw")
    welcome_2 = canvas.create_text(220, 400, font="Corbel 20", text=" Sustainable Development Goals!", anchor="nw")
    next = input("Type enter to continue ")
    canvas.delete(welcome_1)
    canvas.delete(welcome_2)
    sdg_intro(canvas)
    chonchis = ImageTk.PhotoImage(Image.open("Recursos digitales/Chonchiwi copia.png"))
    chonchiwi = canvas.create_image(350, 350, anchor="nw", image=chonchis)
    # 3.1 Present once all the keys for the SDGS.
    print("This is Chonchis, he will guide you to the SDG action. There are 17 SDGs but we are going to learn about 5 of them.")
    print("SGD2: ZERO HUNGER\nSDG4: QUALITY EDUCATION\nSDG6: CLEAN WATER AND SANITATION\nSDG12: RESPONSIBLE CONSUMPTION AND PRODUCTION\nSDG17: PARTNERSHIPS FOR THE GOALS")
    print("")
    # 3.2 Go to learn about SDG action
    sdg_wheel(canvas, chonchiwi)
    image = Image.open("Recursos digitales/SDG Poster.png")
    # 4.1 Ask if they want to play a game or exit
    print("")
    ask_game = input('Ready for a game? type "yes" to continue or "no" to exit: ')
    print("")
    if ask_game == "yes":
        # 4.2 Go to game function
        sdg_game(canvas, background, chonchiwi)
    else:
        # 4.3 Leave and thank you function
        sdg_bye(canvas, background, chonchiwi)

def sdg_bye(canvas, background, chonchiwi):
    # Delete the previous background
    canvas.delete(background)
    canvas.delete(chonchiwi)
    # Change background image
    backgroundNew = ImageTk.PhotoImage(Image.open("Recursos digitales/SDG Logo.png"))
    canvas.create_image(5, 200, image=backgroundNew, anchor="nw")
    # Show Chonchiwi
    chonchis = ImageTk.PhotoImage(Image.open("Recursos digitales/Chonchiwi copia.png"))
    chonchiwi_e = canvas.create_image(600, 30, anchor="nw", image=chonchis)
    # Create thank you text
    canvas.create_text(150, 80, font="Oswald 30", text="THANK YOU! BYE", anchor="w")
    canvas.mainloop()

def sdg_game(canvas, background, chonchiwi):
    # Delete the previous background
    canvas.delete(background)
    canvas.delete(chonchiwi)
    # Show all the 5 SDG icons
    sdg2i = ImageTk.PhotoImage(Image.open("Recursos digitales/SDG2i.png"))
    sdg2 = canvas.create_image(100, 20, anchor="nw", image=sdg2i)
    sdg4i = ImageTk.PhotoImage(Image.open("Recursos digitales/SDG4i.png"))
    sdg4 = canvas.create_image(450, 20, anchor="nw", image=sdg4i)
    sdg6i = ImageTk.PhotoImage(Image.open("Recursos digitales/SDG6I.png"))
    sdg6 = canvas.create_image(275, 275, anchor="nw", image=sdg6i)
    sdg12i = ImageTk.PhotoImage(Image.open("Recursos digitales/SDG12i.png"))
    sdg12 = canvas.create_image(100, 530, anchor="nw", image=sdg12i)
    sdg17i = ImageTk.PhotoImage(Image.open("Recursos digitales/SDG17i.png"))
    sdg17 = canvas.create_image(450, 530, anchor="nw", image=sdg17i)
    # Create a loop for the icons to bounce and game text
    for i in range(5):
        canvas.move(sdg2, 4, -4)
        canvas.move(sdg4, -4, 4)
        canvas.move(sdg6, 8, 0)
        canvas.move(sdg12, -4, 4)
        canvas.move(sdg17, 4, -4)
        canvas.update()
        time.sleep(1 / 5)
        canvas.move(sdg2, -4, 4)
        canvas.move(sdg4, 4, -4)
        canvas.move(sdg6, -8, 0)
        canvas.move(sdg12, 4, -4)
        canvas.move(sdg17, -4, 4)
        canvas.update()
        time.sleep(1 / 5)
    game = canvas.create_text(530, 400, font="Oswald 35", text="GAME!", anchor="w")
    # Create sdg and variable and a list of them
    sdg2_name = "zero hunger"
    sdg4_name = "quality education"
    sdg6_name = "clean water and sanitation"
    sdg12_name = "responsible consumption and production"
    sdg17_name = "partnerships for the goals"
    sdg_list = [sdg2_name, sdg4_name, sdg6_name, sdg12_name, sdg17_name]
    #Instructions
    print('This small game will show you messy words that corresponds to the name of one of the SDG, you will have to rearrange the letters and guess the SDG!\n')
    # Show the user a random value and they have to guess the key
    correct = 0
    while correct < 3:
        # Generate the random value
        rand = random.randint(0, 4)
        sdg_rand = sdg_list[rand]
        sdg_rev = ''
        for ch in sdg_rand:
            sdg_rev = ch + sdg_rev
        # Ask the user to solve
        answer_given = input('You have to guess: ' + sdg_rev + '\nReady? Type your answer in lowercases: ')
        # Check if the answer if correct of not
        if sdg_rand == answer_given:
            # Count the correct answers
            correct += 1
            print("Correct!")
        else:
            print("Incorrect")
            correct = 0
    # Tell the user the game its over
    print("Great! You've got 3 points!")
    # Delete the background and images
    canvas.delete(game)
    canvas.delete(sdg2)
    canvas.delete(sdg4)
    canvas.delete(sdg6)
    canvas.delete(sdg12)
    canvas.delete(sdg17)
    # Once finished return to bye
    sdg_bye(canvas, background, chonchiwi)

def sdg_wheel(canvas, chonchiwi):
    while True:
        # Ask the user to enter the key of an SDG
        sdg = int(input('Type the number of the SDG you want to know how to contribute, "0" to end the learning: '))
        # Evaluate if the SDG info is available. If not, ask again.
        if (sdg == 2) or (sdg == 4) or (sdg == 6) or (sdg == 12) or (sdg == 17):
            sdg_find(canvas, sdg, chonchiwi)
        elif sdg == 0:
            break
        else:
            sdg = int(input("Invalid number. Type the number of the SDG you want to know how to contribute: "))
            sdg_find(canvas, sdg, chonchiwi)

def sdg_find(canvas, sdg, chonchiwi):
    if sdg == 2:
        sdg_2(canvas, chonchiwi)
    if sdg == 4:
        sdg_4(canvas, chonchiwi)
    if sdg == 6:
        sdg_6(canvas, chonchiwi)
    if sdg == 12:
        sdg_12(canvas, chonchiwi)
    if sdg == 17:
        sdg_17(canvas, chonchiwi)

def sdg_2(canvas, chonchiwi):
    # Creates text with the name of the SDG
    sdg_title = canvas.create_text(270, 35, font="Oswald 30", text="ZERO HUNGER", fill="#DDA63A", anchor="w")
    # Chonchiwi will move certain pixels each 1/10 seconds
    for i in range(10):
        canvas.move(chonchiwi, 14, -18)
        canvas.update()
        time.sleep(1 / 10)
    sdg_action1 = canvas.create_text(40, 350, font="Roboto 18", justify="center",
                                     text="1. Have a diet with less environmental impact: eat more legumes,\neat healthier, buy local and sesonal foods.",
                                     anchor="w")
    sdg_action2 = canvas.create_text(40, 420, font="Roboto 18",
                                     text="2. Volunteer at the food bank of your city, wait until it is safe (COVID19).",
                                     anchor="w")
    wait = input("Enter to continue")
    # Chonchiwi will return to center
    for i in range(10):
        canvas.move(chonchiwi, -14, 18)
        canvas.update()
        time.sleep(1 / 10)
    canvas.delete(sdg_title)
    canvas.delete(sdg_action1)
    canvas.delete(sdg_action2)

def sdg_4(canvas, chonchiwi):
    sdg_title = canvas.create_text(270, 35, font="Oswald 25", text="QUALITY EDUCATION", fill="#C5192D", anchor="w")
    for i in range(10):
        canvas.move(chonchiwi, 24, -6)
        canvas.update()
        time.sleep(1 / 10)
    sdg_cheers = canvas.create_text(100, 120, font="Roboto 20", justify="center",
                                    text="Code In Place is a great example of contributing\nto SDG4!", anchor="w")
    sdg_action1 = canvas.create_text(40, 260, font="Roboto 18", justify="center",
                                     text="1. Share your knowledge and create a learning network with\nyour community.",
                                     anchor="w")
    sdg_action2 = canvas.create_text(40, 350, font="Roboto 18", justify="center",
                                     text="2. Donate what you don’t use: books, notebooks,\npencils, pens, even a computer!",
                                     anchor="w")
    wait = input("Enter to continue")
    for i in range(10):
        canvas.move(chonchiwi, -24, 6)
        canvas.update()
        time.sleep(1 / 10)
    canvas.delete(sdg_title)
    canvas.delete(sdg_cheers)
    canvas.delete(sdg_action1)
    canvas.delete(sdg_action2)


def sdg_6(canvas, chonchiwi):
    sdg_title = canvas.create_text(120, 35, font="Oswald 25", text="CLEAN WATER AND SANITATION", fill="#26BDE2",
                                   anchor="w")
    for i in range(10):
        canvas.move(chonchiwi, 22, 11)
        canvas.update()
        time.sleep(1 / 10)
    sdg_action1 = canvas.create_text(40, 280, font="Roboto 18", justify="center",
                                     text="1. Don't throw oil in the sink, 1L could pollute up to 1000L\nof potable water.",
                                     anchor="w")
    sdg_action2 = canvas.create_text(40, 360, font="Roboto 18", justify="center",
                                     text="2. If you smoke don't litter butts, they could pollute up to\n50L of water.",
                                     anchor="w")
    wait = input("Enter to continue")
    for i in range(10):
        canvas.move(chonchiwi, -22, -11)
        canvas.update()
        time.sleep(1 / 10)
    canvas.delete(sdg_title)
    canvas.delete(sdg_action1)
    canvas.delete(sdg_action2)


def sdg_12(canvas, chonchiwi):
    sdg_title = canvas.create_text(10, 35, font="Oswald 25", text="RESPONSIBLE CONSUMPTION AND PRODUCTION",
                                   fill="#BF8B2E", anchor="w")
    for i in range(10):
        canvas.move(chonchiwi, -20, 12)
        canvas.update()
        time.sleep(1 / 10)
    sdg_action1 = canvas.create_text(40, 260, font="Roboto 18", justify="center",
                                     text="1. Donate clothes to someone in need or exchange and renew your\ncloset responsibly!",
                                     anchor="w")
    sdg_action2 = canvas.create_text(40, 380, font="Roboto 18", justify="center",
                                     text='2. Give "ugly" fruits and vegetables a chance, they are often as\nnutritious as those that meet aesthetic standards\nand often end up in the trash.',
                                     anchor="w")
    wait = input("Enter to continue")
    for i in range(10):
        canvas.move(chonchiwi, 20, -12)
        canvas.update()
        time.sleep(1 / 10)
    canvas.delete(sdg_title)
    canvas.delete(sdg_action1)
    canvas.delete(sdg_action2)


def sdg_17(canvas, chonchiwi):
    sdg_title = canvas.create_text(170, 35, font="Oswald 25", text="PARTNERSHIPS FOR THE GOALS", fill="#19486A",
                                   anchor="w")
    for i in range(10):
        canvas.move(chonchiwi, -2, -20)
        canvas.update()
        time.sleep(1 / 10)
    sdg_action1 = canvas.create_text(40, 350, font="Roboto 18",
                                     text="1. Collaborate (virtually or wait until it is safe) with an NGO that\npromotes the SDGs.",
                                     anchor="w")
    sdg_action2 = canvas.create_text(40, 460, font="Roboto 18",
                                     text="2. Organize meetings with your friends where they discuss\nmore actions they can do while having their favorite drink.",
                                     anchor="w")
    wait = input("Enter to continue")
    for i in range(10):
        canvas.move(chonchiwi, 2, 20)
        canvas.update()
        time.sleep(1 / 10)
    canvas.delete(sdg_title)
    canvas.delete(sdg_action1)
    canvas.delete(sdg_action2)


def sdg_intro(canvas):
    # Create text with all the SDGs.
    sdg_all = canvas.create_text(120, 420, font="Corbel 22",
                                 text="SDG1: No poverty\nSG2: Zero Hunger\nSDG3: Good Health and Wellbeing\nSDG4: Quality Education\nSDG5: Gender Equality\n"
                                      "SDG6: Clean Water and Sanitation\nSDG7: Affordable and clean energy\nSDG8: Decent Work and Economic Growth\n"
                                      "SDG9: Industry Innovation and Infrastructure\nSDG10: Reduced Inequalities\nSDG11: Sustainable Cities and Communities\n"
                                      "SDG12: Responsible Consumption and Production\nSDG13: Climate Action\nSDG14: Life Below Water\nSDG15: Life on Land\n"
                                      "SDG16: Peace, Justice and Strong Institutions\nSDG17: Partnerships for the Goals",
                                 anchor="w")
    start = input("Type enter to continue\n")
    # Delete the SDGs
    canvas.delete(sdg_all)


def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()
