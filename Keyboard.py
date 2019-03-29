from tkinter import *
#import pyautogui

# global variables:
bg = "#000e26"
fg = "#4286f4"
caps = False
shift = False
text = ""

def send(val):
#    global text
#    
#    if val == "Back":
#        text = text[0:len(text)-1]
#    elif val == "\n":
#        text = ""
#    else:
#        text += val
#    print(text)

    print(val)
    




def createButton(row, val, capsVal="caps", shiftVal="", other="", label="", width=6, height=3):
    if label == "":
        label = val
    if shiftVal == "":
        shiftVal = capsVal
    button = Button(row, text=other+"\n"+label, width=width, height=height, borderwidth=1,bg=bg, fg=fg, anchor=N, command=lambda val=val: send(val))
    button.pack(side=LEFT)
    #button.grid(row=row, column=column, columnspan=columnSpan, sticky=W,)
    return button




def mainBoard():
    home = Tk()
    home.title("keyboard")
    home.geometry("800x480")
    home.resizable(False, False)
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

    macroFrame = Frame(row1)
    macroFrame.pack(fill=NONE, padx=199, pady=5, side=LEFT)
    MuteKey = createButton(row1, "Mute", label="Mute")
    PlayPauseKey = createButton(row1, "PlayPause", label="▶/⏯️")
    VolDownKey = createButton(row1, "VolDown", label="⇩")
    VolUpKey = createButton(row1, "VolUp", label="⇧")
    
    AccentKey = createButton(row2, "`", other="¬")
    OneKey = createButton(row2, "1", other="!")
    TwoKey = createButton(row2, "2", other="\"")
    ThreeKey = createButton(row2, "3", other="£")
    FourKey = createButton(row2, "4", other="$")
    FiveKey = createButton(row2, "5", other="%")
    SixKey = createButton(row2, "6", other="^")
    SevenKey = createButton(row2, "7", other="&")
    EightKey = createButton(row2, "8", other="*")
    NineKey = createButton(row2, "9", other="(")
    TenKey = createButton(row2, "0", other=")")
    MinusKey = createButton(row2, "-", other="_")
    EqualKey = createButton(row2, "=", other="+")
    BackKey = createButton(row2, "Back", label="⟵", other="", width=13)
        
    TabKey = createButton(row3, "Tab", width=9)
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
    SqBrOKey = createButton(row3, "[", other="{")
    SqBrCKey = createButton(row3, "]", other="}")
    EnterKey = createButton(row3,"\n", "↵", width=12)
    
    CapsKey = createButton(row4, "Caps Lock", width=12)
    AKey = createButton(row4, "A")
    SKey = createButton(row4, "S")
    DKey = createButton(row4, "D")
    FKey = createButton(row4, "F")
    GKey = createButton(row4, "G")
    HKey = createButton(row4, "H")
    JKey = createButton(row4, "J")
    KKey = createButton(row4, "K")
    LKey = createButton(row4, "L")
    SemiColonKey = createButton(row4, ";", other=":")
    ApostropheKey = createButton(row4, "'", other="@")
    HashKey = createButton(row4, "#", other="~")

    ShiftLKey = createButton(row5, "Shift", width=9)
    BSlashKey = createButton(row5, "\\", other="|")
    ZKey = createButton(row5, "Z")
    XKey = createButton(row5, "X")
    CKey = createButton(row5, "C")
    VKey = createButton(row5, "V")
    BKey = createButton(row5, "B")
    NKey = createButton(row5, "N")
    MKey = createButton(row5, "M")
    CommaKey = createButton(row5, ",", other="<")
    StopKey = createButton(row5, ".", other=">")
    FSlashKey = createButton(row5, "/", other="?")
    shiftRKey = createButton(row5, "Shift", width=18)
    
    CtrlLKey = createButton(row6, "Ctrl", width = 11)

    WinLKey = createButton(row6, "Win")
    AltLKey = createButton(row6, "Alt")
    SpaceKey = createButton(row6, " ", width=43)
    UnicodeKey = createButton(row6, "Unicode", width=9)
    WinRKey = createButton(row6, "Win")
    MenuKey = createButton(row6, "Menu")
    CtrlRKey = createButton(row6, "Ctrl", width=11)

    home.mainloop()



mainBoard()
