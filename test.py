import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=599
        height=498
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_615=tk.Listbox(root)
        GListBox_615["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_615["font"] = ft
        GListBox_615["fg"] = "#ffffff"
        GListBox_615["justify"] = "center"
        GListBox_615.place(x=30,y=130,width=251,height=283)

        GListBox_531=tk.Listbox(root)
        GListBox_531["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_531["font"] = ft
        GListBox_531["fg"] = "#ffffff"
        GListBox_531["justify"] = "center"
        GListBox_531.place(x=310,y=130,width=251,height=279)

        GButton_12=tk.Button(root)
        GButton_12["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_12["font"] = ft
        GButton_12["fg"] = "#000000"
        GButton_12["justify"] = "center"
        GButton_12["text"] = "Obfuscate"
        GButton_12.place(x=490,y=40,width=94,height=32)
        GButton_12["command"] = self.GButton_12_command

        GLineEdit_507=tk.Entry(root)
        GLineEdit_507["bg"] = "#000000"
        GLineEdit_507["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_507["font"] = ft
        GLineEdit_507["fg"] = "#ffffff"
        GLineEdit_507["justify"] = "center"
        GLineEdit_507["text"] = "Entry"
        GLineEdit_507.place(x=120,y=40,width=314,height=30)

        GLabel_979=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_979["font"] = ft
        GLabel_979["fg"] = "#ffffff"
        GLabel_979["justify"] = "center"
        GLabel_979["text"] = "APK Obfuscator"
        GLabel_979.place(x=0,y=0,width=105,height=30)

        GLabel_861=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_861["font"] = ft
        GLabel_861["fg"] = "#ffffff"
        GLabel_861["justify"] = "center"
        GLabel_861["text"] = "Original"
        GLabel_861.place(x=110,y=420,width=70,height=25)

        GLabel_173=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_173["font"] = ft
        GLabel_173["fg"] = "#ffffff"
        GLabel_173["justify"] = "center"
        GLabel_173["text"] = "Obfuscated"
        GLabel_173.place(x=400,y=420,width=70,height=25)

        GLabel_440=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_440["font"] = ft
        GLabel_440["fg"] = "#ffffff"
        GLabel_440["justify"] = "center"
        GLabel_440["text"] = "APK Directory Path"
        GLabel_440.place(x=0,y=40,width=120,height=30)

        GButton_142=tk.Button(root)
        GButton_142["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_142["font"] = ft
        GButton_142["fg"] = "#000000"
        GButton_142["justify"] = "center"
        GButton_142["text"] = "Button"
        GButton_142.place(x=440,y=40,width=42,height=30)
        GButton_142["command"] = self.GButton_142_command

    def GButton_12_command(self):
        print("command")


    def GButton_142_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
