from tkinter import *
from speech_recog import r, mic, get_problem, get_attempted_solutions

def click():
        global problem_text, attempted_solutions_text, problem, attempted_solutions
        problem = get_problem()
        attempted_solutions = get_attempted_solutions()
        problem_text.config(text="This Customer's Problem is: " + '"' + problem + '"')
        attempted_solutions_text.config(text="This Customer has Attempted: " + '"' + attempted_solutions + '"')

#WINDOW TITLE
window = Tk() #create a window instance (not actually make one)
window.title('Problem Report')

#WINDOW ICON
icon = PhotoImage(file='D:\Coding\Verizon Prototype\call-report-icon-3.png')
window.iconphoto(True, icon)
#WINDOW BACKGROUND COLOUR
window.config(background='white')

button = Button(window,
                text='GO!',
                relief=RAISED,
                bd=10,
                bg='black',
                fg='white',
                activebackground='blue',
                activeforeground='white'
                )
button.config(command=click) #performs command of function
button.config(font=('Arial', 50, 'bold'))
image = PhotoImage(file=r"C:\Users\theda\Desktop\image files\woah-removebg-preview.png")
button.config(image=image)
button.config(compound='top')
button.config(state=ACTIVE)#disables button, can be set to ACTIVE or DISABLED

#PROBLEM TEXT
problem_text = Label(window,
                text='waiting for problem...',
                font=('Arial', 50, 'bold'),
                bg='white'
                )

#ATTEMPTED SOLUTIONS TEXT
attempted_solutions_text = Label(window,
                text='waiting for attempted solutions...',
                font=('Arial', 50, 'bold'),
                bg='white'
                )

#PLACEMENT
problem_text.pack()
attempted_solutions_text.pack()
button.pack()

window.mainloop() #put window on computer screen, listen for events(future)