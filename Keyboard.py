from tkinter import *

def send(val):
    print(val)

def createButton(window, column, row, val):
    button = Button(window, text=val, width=6, height=3,borderwidth=1, command=lambda val=val: send(val))
    button.grid(row=row, column = column)
    return button
def keyboard():
    home = Tk()
    home.title("keyboard")
    home.geometry("800x480")
    #CtrlKey = Button(home, text = "Ctrl",width=3,height=1,borderwidth=1, command=lambda: send("Ctrl"))
    #CtrlKey.grid(row=0, column=1)
    #BackKey = Button(home, text = "<--",width=3,height=1,borderwidth=1, command=lambda: send("Back"))
    #BackKey.grid(row=1, column=0)
    #Key = createButton(home, , , "")
    
    VDownKey = createButton(home, 13, 1, "⇩")
    VUpKey = createButton(home, 12, 1, "⇧")
    
    
    QKey = createButton(home, 2, 3, "Q")
    WKey = createButton(home, 3, 3, "W")
    EKey = createButton(home, 4, 3, "E")
    RKey = createButton(home, 5, 3, "R")
    TKey = createButton(home, 6, 3, "T")
    YKey = createButton(home, 7, 3, "Y")
    UKey = createButton(home, 8, 3, "U")
    IKey = createButton(home, 9, 3, "I")
    OKey = createButton(home, 10, 3, "O")
    PKey = createButton(home, 11, 3, "P")
    SqBr1Key = createButton(home, 12, 3, "[")
    SqBr2Key = createButton(home, 13, 3, "]")
    EnterKey = createButton(home, 14, 3, "↵")
    
    AKey = createButton(home, 2, 4, "A")
    SKey = createButton(home, 3, 4, "S")
    DKey = createButton(home, 4, 4, "D")
    FKey = createButton(home, 5, 4, "F")
    GKey = createButton(home, 6, 4, "G")
    HKey = createButton(home, 7, 4, "H")
    JKey = createButton(home, 8, 4, "J")
    KKey = createButton(home, 9, 4, "K")
    LKey = createButton(home, 10, 4, "L")
    
    ZKey = createButton(home, 2, 5, "Z")
    XKey = createButton(home, 3, 5, "X")
    CKey = createButton(home, 4, 5, "C")
    VKey = createButton(home, 5, 5, "V")
    BKey = createButton(home, 6, 5, "B")
    NKey = createButton(home, 7, 5, "N")
    MKey = createButton(home, 8, 5, "M")
    
    CtrlKey = createButton(home, 1, 6, "Ctrl")
    WinLKey = createButton(home, 2, 6, "Win")
    AltLKey = createButton(home, 3, 6, "Alt")
    SpaceKey = Button(home, text=" ", width=30, height=3,borderwidth=1, command=lambda val=" ": send(val))
    SpaceKey.grid(column = 4, row=6, columnspan=5)

    home.mainloop()
    

    


    




keyboard()




