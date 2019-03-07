from tkinter import *
#import pyautogui

def send(val):
    print(val)

def createButton(row, val, label="", width=6, height=3):
    if label == "":
        label = val
    button = Button(row, text=label, width=width, height=height,borderwidth=1,bg=bg, fg=fg, anchor=N, command=lambda val=val: send(val))
    button.pack(side=LEFT)
    #button.grid(row=row, column=column, columnspan=columnSpan, sticky=W,)
    return button
def keyboard():
    home = Tk()
    home.title("keyboard")
    home.geometry("800x480")
    home["bg"]="#000000"
    row1 = Frame(home)
    row1.pack(side=TOP, anchor=W)
    row2 = Frame(home)
    row2.pack(side=TOP, anchor=W)
    row3 = Frame(home)
    row3.pack(side=TOP, anchor=W)
    row4 = Frame(home)
    row4.pack(side=TOP, anchor=W)
    row5 = Frame(home)
    row5.pack(side=TOP, anchor=W)
    row6 = Frame(home)
    row6.pack(side=TOP, anchor=W)

    #button1 = Button(row1, text="test")
    #button2 = Button(row1, text="test")
    #button3 = Button(row1, text="test")
    #button4 = Button(row2, text="test")
    #button5 = Button(row2, text="test")
    #button6 = Button(row2, text="test")

    #button1.pack(side=LEFT)
    #button2.pack(side=LEFT)
    #button3.pack(side=LEFT)
    #button4.pack(side=LEFT)
    #button5.pack(side=LEFT)
    #button6.pack(side=LEFT)

    #Key = createButton(row, "")
    
    VolDownKey = createButton(row1, "VolDown", label="⇩")
    VolUpKey = createButton(row1, "VolUp", label="⇧")
    
    OneKey = createButton(row2, "1")
    TwoKey = createButton(row2, "2")
    ThreeKey = createButton(row2, "3")
    FourKey = createButton(row2, "4")
    FiveKey = createButton(row2, "5")
    SixKey = createButton(row2, "6")
    SevenKey = createButton(row2, "7")
    EightKey = createButton(row2, "8")
    NineKey = createButton(row2, "9")
    TenKey = createButton(row2, "0") 

    
    TabKey = createButton(row3, "Tab")
    QKey = createButton(row3, "Q")
    WKey = createButton(row3, "W")
    EKey = createButton(row3, "E")
    RKey = createButton(row3, "R")
    TKey = createButton(row3, "T")
    YKey = createButton(row3, "Y")
    UKey = createButton(row3, "U")
    IKey = createButton(row3, "I")
    OKey = createButton(row3, "O")
    PKey = createButton(row3, "P")
    SqBr1Key = createButton(row3, "[")
    SqBr2Key = createButton(row3, "]")
    EnterKey = createButton(row3,"\n", "↵")
    
    CtrlKey = createButton(row4, "Ctrl", width=9)
    AKey = createButton(row4, "A")
    SKey = createButton(row4, "S")
    DKey = createButton(row4, "D")
    FKey = createButton(row4, "F")
    GKey = createButton(row4, "G")
    HKey = createButton(row4, "H")
    JKey = createButton(row4, "J")
    KKey = createButton(row4, "K")
    LKey = createButton(row4, "L")

    ShiftKey = createButton(row5, "Shift")
    ZKey = createButton(row5, "Z")
    XKey = createButton(row5, "X")
    CKey = createButton(row5, "C")
    VKey = createButton(row5, "V")
    BKey = createButton(row5, "B")
    NKey = createButton(row5, "N")
    MKey = createButton(row5, "M")
    

    CtrlKey = createButton(row6, "Ctrl")
    WinLKey = createButton(row6, "Win")
    AltLKey = createButton(row6, "Alt")
    SpaceKey = createButton(row6, " ", width=30)

    home.mainloop()
    

    


bg = "#000e26"
fg= "#4286f4"




keyboard()




