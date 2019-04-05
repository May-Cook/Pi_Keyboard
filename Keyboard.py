from tkinter import *

### global variables: ###
bg = "#4286f4"
fg = "#000e26"
uniList = ["☺", "≠️", "∬", "ↄ"]
uniPos = 0
caps = False
shift = False
ctrl = False
alt = False
#########################

def send(val): # sends the value to the other device
    print(val)

def enter(val, capsVal, shiftVal, shiftLabel): # calculates which value to pass into send()
    global shift, caps
    if shift:
        if shiftVal!="":
            send(shiftVal)
        elif shiftLabel!="":
            send(shiftLabel)
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

def shiftChange(): # changes the value of shift and passes the corresponding value into send()
    global shift
    if shift:
        shift=False
        send("ShiftOff")
    else:
        shift=True
        send("ShiftOn")

def capsChange(): # changes the value of caps and passes the corresponding value into send()
    global caps
    if caps:
        caps=False
        send("CapsOff")
    else:
        caps=True
        send("CapsOn")

def ctrlChange(): # changes the value of ctrl and passes the corresponding value into send()
    global ctrl
    if ctrl:
        ctrl=False
        send("CtrlOff")
    else:
        ctrl=True
        send("CtrlOn")

def altChange(): # changes the value of alt and passes the corresponding value into send()
    global alt
    if alt:
        alt=False
        send("AltOff")
    else:
        alt=True
        send("AltOn")

def uniChange(uniVal): # changes the value of uniPos and passes the character at corresponding itex of uniList into send()
    global uniList, uniPos
    if uniPos < len(uniList)-1:
        uniPos += 1
    else:
        uniPos = 0
    send(uniList[uniPos])

def createButton(row, val, capsVal="", shiftVal="", shiftLabel="", label="", changeVal="", uniVal="", width=3, height=4, border=2): # creates, packs and returns a tkinter button object
    if label == "":
        if capsVal!="":
            label = capsVal
        else:
            label = val
    if changeVal == "caps":
        button = Button(row, text=shiftLabel+"\n"+label, width=width, height=height, borderwidth=border,bg=bg, fg=fg, anchor=N, command=lambda: capsChange())
    elif changeVal == "shift":
        button = Button(row, text=shiftLabel+"\n"+label, width=width, height=height, borderwidth=border,bg=bg, fg=fg, anchor=N, command=lambda: shiftChange())
    elif changeVal == "ctrl":
        button = Button(row, text=shiftLabel+"\n"+label, width=width, height=height, borderwidth=border,bg=bg, fg=fg, anchor=N, command=lambda: ctrlChange())
    elif changeVal == "alt":
        button = Button(row, text=shiftLabel+"\n"+label, width=width, height=height, borderwidth=border,bg=bg, fg=fg, anchor=N, command=lambda: altChange())
    elif uniVal != "":
        button = Button(row, text=shiftLabel+"\n"+label, width=width, height=height, borderwidth=border,bg=bg, fg=fg, anchor=N, command=lambda: uniChange(uniVal))
    else:
        button = Button(row, text=shiftLabel+"\n"+label, width=width, height=height, borderwidth=border,bg=bg, fg=fg, anchor=N, command=lambda: enter(val, capsVal, shiftVal, shiftLabel))
    button.pack(side=LEFT)
    return button

def mainBoard(): # creates a tkinter window object containing the keyboard interface
    global bg
    height1 = 5
    width1 = 6
    width2 = 3
    height6 = 7
    home = Tk()
    home.title("keyboard")
    home.geometry("800x480")
    home.resizable(False, False)
    home.attributes("-fullscreen", True)
    home["bg"]=bg
    row1 = Frame(home, bg=bg)
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
    macroFrame.pack(fill=NONE, padx=244, pady=5, side=LEFT)
    MuteKey = createButton(row1, "Mute", label="Mute", height=height1, width=width1)
    PlayPauseKey = createButton(row1, "PlayPause", label="▶/⏯️", height=height1, width=width1)
    VolDownKey = createButton(row1, "VolDown", label="⇩", height=height1, width=width1)
    VolUpKey = createButton(row1, "VolUp", label="⇧", height=height1, width=width1)
    
    AccentKey = createButton(row2, "`", shiftLabel="¬", width=width2-1)
    OneKey = createButton(row2, "1", shiftLabel="!", width=width2)
    TwoKey = createButton(row2, "2", shiftLabel="\"", width=width2)
    ThreeKey = createButton(row2, "3", shiftLabel="£", width=width2)
    FourKey = createButton(row2, "4", shiftLabel="$", width=width2)
    FiveKey = createButton(row2, "5", shiftLabel="%", width=width2)
    SixKey = createButton(row2, "6", shiftLabel="^", width=width2)
    SevenKey = createButton(row2, "7", shiftLabel="&", width=width2)
    EightKey = createButton(row2, "8", shiftLabel="*", width=width2)
    NineKey = createButton(row2, "9", shiftLabel="(", width=width2)
    TenKey = createButton(row2, "0", shiftLabel=")", width=width2)
    MinusKey = createButton(row2, "-", shiftLabel="_", width=width2)
    EqualKey = createButton(row2, "=", shiftLabel="+", width=width2)
    BackKey = createButton(row2, "Back", label="⟵", shiftLabel="", width=20)
        
    TabKey = createButton(row3, "Tab", width=8)
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
    SqBrOKey = createButton(row3, "[", shiftLabel="{")
    SqBrCKey = createButton(row3, "]", shiftLabel="}")
    HashKey = createButton(row3, "#", shiftLabel="~", width=10)
    
    CapsKey = createButton(row4, "Caps Lock", width=10, changeVal="caps")
    AKey = createButton(row4, "a", capsVal="A")
    SKey = createButton(row4, "s", capsVal="S")
    DKey = createButton(row4, "d", capsVal="D")
    FKey = createButton(row4, "f", capsVal="F")
    GKey = createButton(row4, "g", capsVal="G")
    HKey = createButton(row4, "h", capsVal="H")
    JKey = createButton(row4, "j", capsVal="J")
    KKey = createButton(row4, "k", capsVal="K")
    LKey = createButton(row4, "l", capsVal="L")
    SemiColonKey = createButton(row4, ";", shiftLabel=":")
    ApostropheKey = createButton(row4, "'", shiftLabel="@")
    EnterKey = createButton(row4,"\n", "↵", width=14)


    ShiftLKey = createButton(row5, "Shift", width=8, changeVal="shift")
    BSlashKey = createButton(row5, "\\", shiftLabel="|")
    ZKey = createButton(row5, "z", capsVal="Z")
    XKey = createButton(row5, "x", capsVal="X")
    CKey = createButton(row5, "c", capsVal="C")
    VKey = createButton(row5, "v", capsVal="V")
    BKey = createButton(row5, "b", capsVal="B")
    NKey = createButton(row5, "n", capsVal="N")
    MKey = createButton(row5, "m", capsVal="M")
    CommaKey = createButton(row5, ",", shiftLabel="<")
    StopKey = createButton(row5, ".", shiftLabel=">")
    FSlashKey = createButton(row5, "/", shiftLabel="?")
    shiftRKey = createButton(row5, "Shift", width=20, changeVal="shift")
    
    CtrlLKey = createButton(row6, "Ctrl", width = 6, height=height6, changeVal="ctrl")

    WinLKey = createButton(row6, "Win", height=height6)
    AltLKey = createButton(row6, "Alt", height=height6, changeVal="alt")
    SpaceKey = createButton(row6, " ", label="____________", width=41, height=height6)
    UnicodeKey = createButton(row6, "Unicode", width=5, height=height6, uniVal=0)
    WinRKey = createButton(row6, "Win", height=height6)
    MenuKey = createButton(row6, "Menu", height=height6)
    CtrlRKey = createButton(row6, "Ctrl", width=6, height=height6, changeVal="ctrl")
    



    home.mainloop()

mainBoard()



