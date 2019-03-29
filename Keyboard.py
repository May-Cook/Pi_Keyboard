from tkinter import *
#import pyautogui

### global variables: ###
bg = "#000e26"
fg = "#4286f4"
uniList = ["☺", "≠️", "∬", "ↄ"]
uniPos = 0
caps = False
shift = False
ctrl = False
alt = False
# text = ""
#########################

def send(val):
#    global text
#    if val == "Back":
#        text = text[0:len(text)-1]
#    elif val == "\n":
#        text = ""
#    else:
#        text += val
#    print(text)

    print(val)

def enter(val, capsVal, shiftVal, other):
    global shift, caps
    if shift:
        if shiftVal!="":
            send(shiftVal)
        elif other!="":
            send(other)
        elif capsVal != "":
            send(capsVal)
        else:
            send(val)
    elif caps:
        if capsVal != "":
            send(capsVal)
        else:
            send(val)
    else:
        send(val)
def shiftChange():
    global shift
    if shift:
        shift=False
        send("ShiftOff")
    else:
        shift=True
        send("ShiftOn")
def capsChange():
    global caps
    if caps:
        caps=False
        send("CapsOff")
    else:
        caps=True
        send("CapsOn")
def ctrlChange():
    global ctrl
    if ctrl:
        ctrl=False
        send("CtrlOff")
    else:
        ctrl=True
        send("CtrlOn")
def altChange():
    global alt
    if alt:
        alt=False
        send("AltOff")
    else:
        alt=True
        send("AltOn")
def uniChange(uniVal):
    global uniList, uniPos
    if uniPos < len(uniList)-1:
        uniPos += 1
    else:
        uniPos = 0
    send(uniList[uniPos])


def createButton(row, val, capsVal="", shiftVal="", other="", label="", changeVal="", uniVal="", width=6, height=3):
    if label == "":
        if capsVal!="":
            label = capsVal
        else:
            label = val
    if changeVal == "caps":
        button = Button(row, text=other+"\n"+label, width=width, height=height, borderwidth=1,bg=bg, fg=fg, anchor=N, command=lambda: capsChange())
    elif changeVal == "shift":
        button = Button(row, text=other+"\n"+label, width=width, height=height, borderwidth=1,bg=bg, fg=fg, anchor=N, command=lambda: shiftChange())
    elif changeVal == "ctrl":
        button = Button(row, text=other+"\n"+label, width=width, height=height, borderwidth=1,bg=bg, fg=fg, anchor=N, command=lambda: ctrlChange())
    elif changeVal == "alt":
        button = Button(row, text=other+"\n"+label, width=width, height=height, borderwidth=1,bg=bg, fg=fg, anchor=N, command=lambda: altChange())
    elif uniVal != "":
        button = Button(row, text=other+"\n"+label, width=width, height=height, borderwidth=1,bg=bg, fg=fg, anchor=N, command=lambda: uniChange(uniVal))
    else:
        button = Button(row, text=other+"\n"+label, width=width, height=height, borderwidth=1,bg=bg, fg=fg, anchor=N, command=lambda: enter(val, capsVal, shiftVal, other))
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
    # indicatorFrame = Frame(row1)
    # indicatorFrame.pack(fill=NONE, padx=100, pady=5, side=LEFT)
    
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
    QKey = createButton(row3, "q", capsVal="Q")
    WKey = createButton(row3, "w", capsVal="W")
    EKey = createButton(row3, "e", capsVal="E")
    RKey = createButton(row3, "r", capsVal="R")
    TKey = createButton(row3, "t", capsVal="T")
    YKey = createButton(row3, "y", capsVal="Y")
    UKey = createButton(row3, "u", capsVal="U")
    IKey = createButton(row3, "i", capsVal="I")
    OKey = createButton(row3, "o", capsVal="O")
    PKey = createButton(row3, "p", capsVal="P")
    SqBrOKey = createButton(row3, "[", other="{")
    SqBrCKey = createButton(row3, "]", other="}")
    EnterKey = createButton(row3,"\n", "↵", width=12)
    
    CapsKey = createButton(row4, "Caps Lock", width=12, changeVal="caps")
    AKey = createButton(row4, "a", capsVal="A")
    SKey = createButton(row4, "s", capsVal="S")
    DKey = createButton(row4, "d", capsVal="D")
    FKey = createButton(row4, "f", capsVal="F")
    GKey = createButton(row4, "g", capsVal="G")
    HKey = createButton(row4, "h", capsVal="H")
    JKey = createButton(row4, "j", capsVal="J")
    KKey = createButton(row4, "k", capsVal="K")
    LKey = createButton(row4, "l", capsVal="L")
    SemiColonKey = createButton(row4, ";", other=":")
    ApostropheKey = createButton(row4, "'", other="@")
    HashKey = createButton(row4, "#", other="~")

    ShiftLKey = createButton(row5, "Shift", width=9, changeVal="shift")
    BSlashKey = createButton(row5, "\\", other="|")
    ZKey = createButton(row5, "z", capsVal="Z")
    XKey = createButton(row5, "x", capsVal="X")
    CKey = createButton(row5, "c", capsVal="C")
    VKey = createButton(row5, "v", capsVal="V")
    BKey = createButton(row5, "b", capsVal="B")
    NKey = createButton(row5, "n", capsVal="N")
    MKey = createButton(row5, "m", capsVal="M")
    CommaKey = createButton(row5, ",", other="<")
    StopKey = createButton(row5, ".", other=">")
    FSlashKey = createButton(row5, "/", other="?")
    shiftRKey = createButton(row5, "Shift", width=18, changeVal="shift")
    
    CtrlLKey = createButton(row6, "Ctrl", width = 11, changeVal="ctrl")

    WinLKey = createButton(row6, "Win")
    AltLKey = createButton(row6, "Alt", changeVal="alt")
    SpaceKey = createButton(row6, " ", width=43)
    UnicodeKey = createButton(row6, "Unicode", width=9, uniVal=0)
    WinRKey = createButton(row6, "Win")
    MenuKey = createButton(row6, "Menu")
    CtrlRKey = createButton(row6, "Ctrl", width=11, changeVal="ctrl")
    



    home.mainloop()
    # while True:
    #     if caps:
    #         CapsKey.config(relief=RAISED)
    #     else:
    #         CapsKey.config(relief=FLAT)



mainBoard()
