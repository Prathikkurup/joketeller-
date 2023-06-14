import tkinter


def getNewJoke(): print("Gets the joke from internet")

def loadJoke(): print("Display and do some other stuff")

def newJokeBtnClicked(): print("Requests a new joke")

#GUI
window = tkinter.Tk();
window.title("Joke Teller");

heading = tkinter.Label(window, text="Joke Teller", font=("Stencil", 28));
heading.pack();

display = tkinter.Text(window);
display.pack();

button = tkinter.Button(window, text="New Joke", font=("Stencil", 15));
button.pack();

window.mainloop()

