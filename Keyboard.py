from tkinter import *

### global variables: ###
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

def createButton(row, values, val, capsVal="", shiftVal="", shiftLabel="", label="", changeVal="", width=3, height=4, border=2): # creates, packs and returns a tkinter button object
    if label == "":
        if capsVal!="":
            label = capsVal
        else:
            label = val
    if changeVal == "caps":
        button = Button(row, text=shiftLabel+"\n"+label, width=width, height=height, borderwidth=border, bg=values[1], fg=values[2], activebackground = values[3], activeforeground = values[4], anchor=N, command=lambda: capsChange())
    elif changeVal == "shift":
        button = Button(row, text=shiftLabel+"\n"+label, width=width, height=height, borderwidth=border, bg=values[1], fg=values[2], activebackground = values[3], activeforeground = values[4], anchor=N, command=lambda: shiftChange())
    elif changeVal == "ctrl":
        button = Button(row, text=shiftLabel+"\n"+label, width=width, height=height, borderwidth=border, bg=values[1], fg=values[2], activebackground = values[3], activeforeground = values[4], anchor=N, command=lambda: ctrlChange())
    elif changeVal == "alt":
        button = Button(row, text=shiftLabel+"\n"+label, width=width, height=height, borderwidth=border, bg=values[1], fg=values[2], activebackground = values[3], activeforeground = values[4], anchor=N, command=lambda: altChange())
    elif val == "Unicode":
        button = Button(row, text=shiftLabel+"\n"+label, width=width, height=height, borderwidth=border, bg=values[1], fg=values[2], activebackground = values[3], activeforeground = values[4], anchor=N, command=lambda: send(values[5]))
    else:
        button = Button(row, text=shiftLabel+"\n"+label, width=width, height=height, borderwidth=border, bg=values[1], fg=values[2], activebackground = values[3], activeforeground = values[4], anchor=N, command=lambda: enter(val, capsVal, shiftVal, shiftLabel))
    button.pack(side=LEFT)
    return button

def qwertyBoard(values, currentProfileName): # creates a tkinter window object containing a keyboard interface with a qwerty layout
    print("qwertyBoard: ", values, ", ", currentProfileName)
    height1 = 5
    width1 = 6
    width2 = 3
    height6 = 7
    home = Tk()
    home.title("Keyboard: " + currentProfileName)
    home.geometry("800x480")
    # home.resizable(False, False)
    # home.attributes("-fullscreen", True)
    home["bg"]=values[1]
    row1 = Frame(home, bg=values[1])
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
    MuteKey = createButton(row1, values, "Mute", label="Mute", height=height1, width=width1)
    PlayPauseKey = createButton(row1, values, "PlayPause", label="▶/⏯️", height=height1, width=width1)
    VolDownKey = createButton(row1, values, "VolDown", label="⇩", height=height1, width=width1)
    VolUpKey = createButton(row1, values, "VolUp", label="⇧", height=height1, width=width1)
    
    AccentKey = createButton(row2, values, "`", shiftLabel="¬", width=width2-1)
    OneKey = createButton(row2, values, "1", shiftLabel="!", width=width2)
    TwoKey = createButton(row2, values, "2", shiftLabel="\"", width=width2)
    ThreeKey = createButton(row2, values, "3", shiftLabel="£", width=width2)
    FourKey = createButton(row2, values, "4", shiftLabel="$", width=width2)
    FiveKey = createButton(row2, values, "5", shiftLabel="%", width=width2)
    SixKey = createButton(row2, values, "6", shiftLabel="^", width=width2)
    SevenKey = createButton(row2, values, "7", shiftLabel="&", width=width2)
    EightKey = createButton(row2, values, "8", shiftLabel="*", width=width2)
    NineKey = createButton(row2, values, "9", shiftLabel="(", width=width2)
    TenKey = createButton(row2, values, "0", shiftLabel=")", width=width2)
    MinusKey = createButton(row2, values, "-", shiftLabel="_", width=width2)
    EqualKey = createButton(row2, values, "=", shiftLabel="+", width=width2)
    BackKey = createButton(row2, values, "Back", label="⟵", shiftLabel="", width=20)
        
    TabKey = createButton(row3, values, "Tab", width=8)
    QKey = createButton(row3, values, "q", capsVal="Q")
    WKey = createButton(row3, values, "w", capsVal="W")
    EKey = createButton(row3, values,"e", capsVal="E")
    RKey = createButton(row3, values,"r", capsVal="R")
    TKey = createButton(row3, values,"t", capsVal="T")
    YKey = createButton(row3, values, "y", capsVal="Y")
    UKey = createButton(row3, values, "u", capsVal="U")
    IKey = createButton(row3, values, "i", capsVal="I")
    OKey = createButton(row3, values, "o", capsVal="O")
    PKey = createButton(row3, values, "p", capsVal="P")
    SqBrOKey = createButton(row3, values, "[", shiftLabel="{")
    SqBrCKey = createButton(row3, values, "]", shiftLabel="}")
    HashKey = createButton(row3, values, "#", shiftLabel="~", width=10)
    
    CapsKey = createButton(row4, values, "Caps Lock", width=10, changeVal="caps")
    AKey = createButton(row4, values, "a", capsVal="A")
    SKey = createButton(row4, values, "s", capsVal="S")
    DKey = createButton(row4, values, "d", capsVal="D")
    FKey = createButton(row4, values, "f", capsVal="F")
    GKey = createButton(row4, values, "g", capsVal="G")
    HKey = createButton(row4, values, "h", capsVal="H")
    JKey = createButton(row4, values, "j", capsVal="J")
    KKey = createButton(row4, values, "k", capsVal="K")
    LKey = createButton(row4, values, "l", capsVal="L")
    SemiColonKey = createButton(row4, values, ";", shiftLabel=":")
    ApostropheKey = createButton(row4, values, "'", shiftLabel="@")
    EnterKey = createButton(row4, values, "\n", "↵", width=14)


    ShiftLKey = createButton(row5, values, "Shift", width=8, changeVal="shift")
    BSlashKey = createButton(row5, values, "\\", shiftLabel="|")
    ZKey = createButton(row5, values, "z", capsVal="Z")
    XKey = createButton(row5, values, "x", capsVal="X")
    CKey = createButton(row5, values, "c", capsVal="C")
    VKey = createButton(row5, values, "v", capsVal="V")
    BKey = createButton(row5, values, "b", capsVal="B")
    NKey = createButton(row5, values, "n", capsVal="N")
    MKey = createButton(row5, values, "m", capsVal="M")
    CommaKey = createButton(row5, values, ",", shiftLabel="<")
    StopKey = createButton(row5, values, ".", shiftLabel=">")
    FSlashKey = createButton(row5, values, "/", shiftLabel="?")
    shiftRKey = createButton(row5, values, "Shift", width=20, changeVal="shift")
    
    CtrlLKey = createButton(row6, values, "Ctrl", width = 6, height=height6, changeVal="ctrl")

    WinLKey = createButton(row6, values, "Win", height=height6)
    AltLKey = createButton(row6, values, "Alt", height=height6, changeVal="alt")
    SpaceKey = createButton(row6, values, " ", label="____________", width=41, height=height6)
    UnicodeKey = createButton(row6, values, "Unicode", width=5, height=height6)
    WinRKey = createButton(row6, values, "Win", height=height6)
    MenuKey = createButton(row6, values, "Menu", height=height6)
    CtrlRKey = createButton(row6, values, "Ctrl", width=6, height=height6, changeVal="ctrl")
    



    home.mainloop()

def dvorakBoard(values, currentProfileName): # creates a tkinter window object containing a keyboard interface with a dvorak layout
    print("dvorakBoard: ", values, ", ", currentProfileName)
    height1 = 5
    width1 = 6
    width2 = 3
    height6 = 7
    home = Tk()
    home.title("Keyboard: " + currentProfileName)
    home.geometry("800x480")
    # home.resizable(False, False)
    # home.attributes("-fullscreen", True)
    home["bg"]=values[1]
    row1 = Frame(home, bg=values[1])
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
    MuteKey = createButton(row1, values, "Mute", label="Mute", height=height1, width=width1)
    PlayPauseKey = createButton(row1, values, "PlayPause", label="▶/⏯️", height=height1, width=width1)
    VolDownKey = createButton(row1, values, "VolDown", label="⇩", height=height1, width=width1)
    VolUpKey = createButton(row1, values, "VolUp", label="⇧", height=height1, width=width1)
    
    AccentKey = createButton(row2, values, "`", shiftLabel="¬", width=width2-1)
    OneKey = createButton(row2, values, "1", shiftLabel="!", width=width2)
    TwoKey = createButton(row2, values, "2", shiftLabel="\"", width=width2)
    ThreeKey = createButton(row2, values, "3", shiftLabel="£", width=width2)
    FourKey = createButton(row2, values, "4", shiftLabel="$", width=width2)
    FiveKey = createButton(row2, values, "5", shiftLabel="%", width=width2)
    SixKey = createButton(row2, values, "6", shiftLabel="^", width=width2)
    SevenKey = createButton(row2, values, "7", shiftLabel="&", width=width2)
    EightKey = createButton(row2, values, "8", shiftLabel="*", width=width2)
    NineKey = createButton(row2, values, "9", shiftLabel="(", width=width2)
    TenKey = createButton(row2, values, "0", shiftLabel=")", width=width2)
    MinusKey = createButton(row2, values, "-", shiftLabel="_", width=width2)
    EqualKey = createButton(row2, values, "=", shiftLabel="+", width=width2)
    BackKey = createButton(row2, values, "Back", label="⟵", shiftLabel="", width=20)
        
    TabKey = createButton(row3, values, "Tab", width=8)
    CommaKey = createButton(row3, values, ",", shiftLabel="<")
    StopKey = createButton(row3, values, ".", shiftLabel=">")
    PKey = createButton(row3, values, "p", capsVal="P")
    YKey = createButton(row3, values, "y", capsVal="Y")
    FKey = createButton(row3, values, "f", capsVal="F")
    GKey = createButton(row3, values, "g", capsVal="G")
    CKey = createButton(row3, values, "c", capsVal="C")
    RKey = createButton(row3, values,"r", capsVal="R")
    LKey = createButton(row3, values, "l", capsVal="L")
    SqBrOKey = createButton(row3, values, "[", shiftLabel="{")
    SqBrCKey = createButton(row3, values, "]", shiftLabel="}")
    FSlashKey = createButton(row3, values, "/", shiftLabel="?")
    HashKey = createButton(row3, values, "#", shiftLabel="~", width=10)
    
    CapsKey = createButton(row4, values, "Caps Lock", width=10, changeVal="caps")
    AKey = createButton(row4, values, "a", capsVal="A")
    OKey = createButton(row4, values, "o", capsVal="O")
    EKey = createButton(row4, values,"e", capsVal="E")
    UKey = createButton(row4, values, "u", capsVal="U")
    IKey = createButton(row4, values, "i", capsVal="I")
    DKey = createButton(row4, values, "d", capsVal="D")
    HKey = createButton(row4, values, "h", capsVal="H")
    TKey = createButton(row4, values,"t", capsVal="T")
    NKey = createButton(row4, values, "n", capsVal="N")
    SKey = createButton(row4, values, "s", capsVal="S")
    ApostropheKey = createButton(row4, values, "'", shiftLabel="@")
    EnterKey = createButton(row4, values, "\n", "↵", width=14)


    ShiftLKey = createButton(row5, values, "Shift", width=8, changeVal="shift")
    BSlashKey = createButton(row5, values, "\\", shiftLabel="|")
    SemiColonKey = createButton(row5, values, ";", shiftLabel=":")
    QKey = createButton(row5, values, "q", capsVal="Q")
    JKey = createButton(row5, values, "j", capsVal="J")
    KKey = createButton(row5, values, "k", capsVal="K")
    XKey = createButton(row5, values, "x", capsVal="X")
    BKey = createButton(row5, values, "b", capsVal="B")
    MKey = createButton(row5, values, "m", capsVal="M")
    WKey = createButton(row5, values, "w", capsVal="W")
    VKey = createButton(row5, values, "v", capsVal="V")
    ZKey = createButton(row5, values, "z", capsVal="Z")
    shiftRKey = createButton(row5, values, "Shift", width=20, changeVal="shift")










    
    CtrlLKey = createButton(row6, values, "Ctrl", width = 6, height=height6, changeVal="ctrl")

    WinLKey = createButton(row6, values, "Win", height=height6)
    AltLKey = createButton(row6, values, "Alt", height=height6, changeVal="alt")
    SpaceKey = createButton(row6, values, " ", label="____________", width=41, height=height6)
    UnicodeKey = createButton(row6, values, "Unicode", width=5, height=height6)
    WinRKey = createButton(row6, values, "Win", height=height6)
    MenuKey = createButton(row6, values, "Menu", height=height6)
    CtrlRKey = createButton(row6, values, "Ctrl", width=6, height=height6, changeVal="ctrl")
    



    home.mainloop()

def colemakBoard(values, currentProfileName): # creates a tkinter window object containing a keyboard interface with a qwerty layout
    print("qwertyBoard: ", values, ", ", currentProfileName)
    height1 = 5
    width1 = 6
    width2 = 3
    height6 = 7
    home = Tk()
    home.title("Keyboard: " + currentProfileName)
    home.geometry("800x480")
    # home.resizable(False, False)
    # home.attributes("-fullscreen", True)
    home["bg"]=values[1]
    row1 = Frame(home, bg=values[1])
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
    MuteKey = createButton(row1, values, "Mute", label="Mute", height=height1, width=width1)
    PlayPauseKey = createButton(row1, values, "PlayPause", label="▶/⏯️", height=height1, width=width1)
    VolDownKey = createButton(row1, values, "VolDown", label="⇩", height=height1, width=width1)
    VolUpKey = createButton(row1, values, "VolUp", label="⇧", height=height1, width=width1)
    
    AccentKey = createButton(row2, values, "`", shiftLabel="¬", width=width2-1)
    OneKey = createButton(row2, values, "1", shiftLabel="!", width=width2)
    TwoKey = createButton(row2, values, "2", shiftLabel="\"", width=width2)
    ThreeKey = createButton(row2, values, "3", shiftLabel="£", width=width2)
    FourKey = createButton(row2, values, "4", shiftLabel="$", width=width2)
    FiveKey = createButton(row2, values, "5", shiftLabel="%", width=width2)
    SixKey = createButton(row2, values, "6", shiftLabel="^", width=width2)
    SevenKey = createButton(row2, values, "7", shiftLabel="&", width=width2)
    EightKey = createButton(row2, values, "8", shiftLabel="*", width=width2)
    NineKey = createButton(row2, values, "9", shiftLabel="(", width=width2)
    TenKey = createButton(row2, values, "0", shiftLabel=")", width=width2)
    MinusKey = createButton(row2, values, "-", shiftLabel="_", width=width2)
    EqualKey = createButton(row2, values, "=", shiftLabel="+", width=width2)
    BackKey = createButton(row2, values, "Back", label="⟵", shiftLabel="", width=20)
        
    TabKey = createButton(row3, values, "Tab", width=8)
    QKey = createButton(row3, values, "q", capsVal="Q")
    WKey = createButton(row3, values, "w", capsVal="W")
    FKey = createButton(row3, values, "f", capsVal="F")
    PKey = createButton(row3, values, "p", capsVal="P")
    GKey = createButton(row3, values, "g", capsVal="G")
    JKey = createButton(row3, values, "j", capsVal="J")
    LKey = createButton(row3, values, "l", capsVal="L")
    UKey = createButton(row3, values, "u", capsVal="U")
    YKey = createButton(row3, values, "y", capsVal="Y")
    SemiColonKey = createButton(row3, values, ";", shiftLabel=":")
    SqBrOKey = createButton(row3, values, "[", shiftLabel="{")
    SqBrCKey = createButton(row3, values, "]", shiftLabel="}")
    HashKey = createButton(row3, values, "#", shiftLabel="~", width=10)


    BigBackKey = createButton(row4, values, "Back", label="⟵", shiftLabel="", width=10)
    AKey = createButton(row4, values, "a", capsVal="A")
    RKey = createButton(row4, values,"r", capsVal="R")
    SKey = createButton(row4, values, "s", capsVal="S")
    TKey = createButton(row4, values,"t", capsVal="T")
    DKey = createButton(row4, values, "d", capsVal="D")
    HKey = createButton(row4, values, "h", capsVal="H")
    NKey = createButton(row4, values, "n", capsVal="N")
    EKey = createButton(row4, values,"e", capsVal="E")
    IKey = createButton(row4, values, "i", capsVal="I")
    OKey = createButton(row4, values, "o", capsVal="O")
    ApostropheKey = createButton(row4, values, "'", shiftLabel="@")
    EnterKey = createButton(row4, values, "\n", "↵", width=14)

    ShiftLKey = createButton(row5, values, "Shift", width=8, changeVal="shift")
    BSlashKey = createButton(row5, values, "\\", shiftLabel="|")
    ZKey = createButton(row5, values, "z", capsVal="Z")
    XKey = createButton(row5, values, "x", capsVal="X")
    CKey = createButton(row5, values, "c", capsVal="C")
    VKey = createButton(row5, values, "v", capsVal="V")
    BKey = createButton(row5, values, "b", capsVal="B")
    KKey = createButton(row5, values, "k", capsVal="K")
    MKey = createButton(row5, values, "m", capsVal="M")
    CommaKey = createButton(row5, values, ",", shiftLabel="<")
    StopKey = createButton(row5, values, ".", shiftLabel=">")
    FSlashKey = createButton(row5, values, "/", shiftLabel="?")
    shiftRKey = createButton(row5, values, "Shift", width=20, changeVal="shift")
    


    CtrlLKey = createButton(row6, values, "Ctrl", width = 6, height=height6, changeVal="ctrl")
    WinLKey = createButton(row6, values, "Win", height=height6)
    AltLKey = createButton(row6, values, "Alt", height=height6, changeVal="alt")
    SpaceKey = createButton(row6, values, " ", label="____________", width=41, height=height6)
    UnicodeKey = createButton(row6, values, "Unicode", width=5, height=height6)
    WinRKey = createButton(row6, values, "Win", height=height6)
    MenuKey = createButton(row6, values, "Menu", height=height6)
    CtrlRKey = createButton(row6, values, "Ctrl", width=6, height=height6, changeVal="ctrl")
    



    home.mainloop()


Profiles = open("Saves/Profiles.txt", "r")
currentProfileName = Profiles.readline()
currentProfileName = currentProfileName.replace("\n", "")
currentProfile = open("Saves/"+ currentProfileName +".txt", "rb")
values = currentProfile.readlines()

for i in range (0, len(values)):
    newVal = values[i]
    newVal = newVal.decode("utf-8")
    newVal = newVal.replace("\n", "")
    newVal = newVal.replace("\r","")
    values[i] = newVal

if "dvorak" in values[0]:
    dvorakBoard(values, currentProfileName)
elif "colemak" in values[0]:
    colemakBoard(values, currentProfileName)
else:
    qwertyBoard(values, currentProfileName)
