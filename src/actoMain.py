import sys
sys.dont_write_bytecode = True

import tkinter as tk
import tkinter.ttk as ttk
from data.actoData import actoData

data = actoData()

data.createTables()
#data.deleteAction(1)

#? Maybe set window to a constant size?

class TkinterApp(ttk.Frame):
    def __init__(self,master=None):
        ttk.Frame.__init__(self, master)
        self.placeholder = None
        
        #* Build the UI on load.
        self.buildStartUI()

    def buildUncompletedUI(self):
        pass #* For uncompleted actions

    
    def buildCompletedUI(self):
        self.dataPanel = tk.Frame(self)
        self.butPanel = tk.Frame(self)
        self.settingPanel = tk.Frame(self.butPanel)

        self.lblSelectedAction = tk.Label(self.butPanel, text="No currently selected action to modify.")
        self.lblSelectedAction.grid(row=1, column=2)

        self.settingPanel.grid(row=2, column=0)
        
        self.dataPanel.pack(side = tk.TOP)
        self.butPanel.pack(side = tk.LEFT)
        self.pack()



    def buildStartUI(self):
        self.funny = tk.Frame(self)


        self.labelMainText = tk.Label(self.funny, text="Select which menu to view.")
        self.labelMainText.grid(row=0, columnspan=2)

        self.btnCompleted = tk.Button(self.funny, text="Completed Actions", command=self.buildCompletedUI)
        self.btnCompleted.grid(row=1, column=0)

        self.btnUnCompleted = tk.Button(self.funny, text="Uncompleted Actions", command=self.buildUncompletedUI)
        self.btnUnCompleted.grid(row=1, column=1)

        self.funny.pack(side=tk.TOP)
        self.pack()






#TODO: (HAHA GET IT!)
#!    - Utilize a radio button to toggle between completed and uncompleted. 

root = tk.Tk()
root.geometry("800x500") #* temporary window size

app = TkinterApp()
app.master.title("Acto")
app.mainloop()