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



    







    #CtrlKey = Button(home, text = "Ctrl",width=3,height=1,borderwidth=1, command=lambda: send("Ctrl"))
    #CtrlKey.grid(row=0, column=1)
    #BackKey = Button(home, text = "<--",width=3,height=1,borderwidth=1, command=lambda: send("Back"))
    #BackKey.grid(row=1, column=0)
    #Key = createButton(home, , , "")
    
    #VolDownKey = createButton(home, 13, 1, "VolDown", "⇩")
    #VolUpKey = createButton(home, 12, 1, "VolUp", "⇧")
    
    #OneKey = createButton(home, 2, 2, "1")
    #TwoKey = createButton(home, 3, 2, "2")
    #ThreeKey = createButton(home, 4, 2, "3")
    #FourKey = createButton(home, 5, 2, "4")
    #FiveKey = createButton(home, 6, 2, "5")
    #SixKey = createButton(home, 7, 2, "6")
    #SevenKey = createButton(home, 8, 2, "7")
    #EightKey = createButton(home, 9, 2, "8")
    #NineKey = createButton(home, 10, 2, "9")
    #TenKey = createButton(home, 11, 2, "0")
    





    
    
    
    
    
    EnterKey = createButton(row3,"\n", "↵")
    SqBr2Key = createButton(row3, "]")
    SqBr1Key = createButton(row3, "[")
    PKey = createButton(row3, "P")
    OKey = createButton(row3, "O")
    IKey = createButton(row3,"I")
    UKey = createButton(row3, "U")
    YKey = createButton(row3, "Y")
    TKey = createButton(row3, "T")
    RKey = createButton(row3, "R")
    EKey = createButton(row3, "E")
    WKey = createButton(row3, "W")
    QKey = createButton(row3, "Q")
    TabKey = createButton(row3, "Tab")
    
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
    

    #CtrlKey = createButton(home, 1, 6, "Ctrl")
    #WinLKey = createButton(home, 2, 6, "Win")
    #AltLKey = createButton(home, 3, 6, "Alt")
    #SpaceKey = createButton(home, 4, 6, " ", columnSpan=5, width=30)

    #SpaceKey = Button(home, text=" ", width=30, height=3,borderwidth=1, command=lambda val=" ": send(val))
    #SpaceKey.grid(column = 4, row=6, columnspan=5)

    home.mainloop()
    

    


bg = "#000e26"
fg= "#4286f4"




keyboard()




