from tkinter import *
#import pyautogui

def send(val):
    print(val)

def createButton(window, column, row, val, label="", columnSpan = 1, width=6, height=3):
    if label == "":
        label = val
    button = Button(window, text=label, width=width, height=height,borderwidth=1,bg=bg, fg=fg, anchor=N, command=lambda val=val: send(val))
    button.grid(row=row, column=column, columnspan=columnSpan, sticky=W,)
    return button
def keyboard():
    home = Tk()
    home.title("keyboard")
    home.geometry("800x480")
    home["bg"]="#000000"
    #CtrlKey = Button(home, text = "Ctrl",width=3,height=1,borderwidth=1, command=lambda: send("Ctrl"))
    #CtrlKey.grid(row=0, column=1)
    #BackKey = Button(home, text = "<--",width=3,height=1,borderwidth=1, command=lambda: send("Back"))
    #BackKey.grid(row=1, column=0)
    #Key = createButton(home, , , "")
    
    VolDownKey = createButton(home, 13, 1, "VolDown", "⇩")
    VolUpKey = createButton(home, 12, 1, "VolUp", "⇧")
    
    OneKey = createButton(home, 2, 2, "1")
    TwoKey = createButton(home, 3, 2, "2")
    ThreeKey = createButton(home, 4, 2, "3")
    FourKey = createButton(home, 5, 2, "4")
    FiveKey = createButton(home, 6, 2, "5")
    SixKey = createButton(home, 7, 2, "6")
    SevenKey = createButton(home, 8, 2, "7")
    EightKey = createButton(home, 9, 2, "8")
    NineKey = createButton(home, 10, 2, "9")
    TenKey = createButton(home, 11, 2, "0")
    
    TabKey = createButton(home, 1, 3, "Tab")
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
    EnterKey = createButton(home, 14, 3,"\n", "↵")
    
    CtrlKey = createButton(home, 1, 4, "Ctrl", width=7)
    AKey = createButton(home, 2, 4, "A")
    SKey = createButton(home, 3, 4, "S")
    DKey = createButton(home, 4, 4, "D")
    FKey = createButton(home, 5, 4, "F")
    GKey = createButton(home, 6, 4, "G")
    HKey = createButton(home, 7, 4, "H")
    JKey = createButton(home, 8, 4, "J")
    KKey = createButton(home, 9, 4, "K")
    LKey = createButton(home, 10, 4, "L")

    ShiftKey = createButton(home, 1, 5, "Shift")
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
    SpaceKey = createButton(home, 4, 6, " ", columnSpan=5, width=30)

    #SpaceKey = Button(home, text=" ", width=30, height=3,borderwidth=1, command=lambda val=" ": send(val))
    #SpaceKey.grid(column = 4, row=6, columnspan=5)

    home.mainloop()
    

    


bg = "#000e26"
fg= "#4286f4"




keyboard()




