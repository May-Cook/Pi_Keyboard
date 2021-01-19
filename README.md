# Pi_keyboard
I started this project as part of my A-level computer science course. The purpose of this project was to create a virtual keyboard that would run on a raspberry pi zero
the project was unrealistically ambitious *(as is typical of early projects)* and was only ever partially completed
I have slightly cleaned up the project and am releasing  it... I don't really know why

anyway this is it
the keyboard currently just prints the corresponding character to the terminal when a key is pressed.

the project was written in python and uses `tkinter` to create the UI

the project was meant to allow the user to create and store profiles, and this functionality is implemented... badly
the profiles are stored in text files, named `Profile1.txt`, `Profile2.txt` and so on. each profile contains:
* the keyboard layout 
 * qwerty, colemak or dvorak
* the background colour, as a hexcode
* the foreground colour, as a hexcode
* the active background colour, as a hexcode
* the active foreground colour, as a hexcode
* the character that will be output when the `unicode` character is pressed
the currently selected profile, followed by a list of all profiles, including the currently selected one are all stored in `Profiles.txt`

the project was initially intended to run on the touchscreen of a specif raspberry pi, the UI is therefore designed for a window of a specific size, when the project was initially created, the keyboard ran in fullscreen but when running the program on a different machine it best to run it as a window. I have therefore changed the interface to run in a window of the correct size, if you really want to run it in fullscreen, you can change the global variable `fullScreen` to true **I do not recommend this**
