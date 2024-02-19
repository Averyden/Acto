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

        self.emptyStar = "☆"
        self.fullStar = "★"
        self.priorityRating = "0"
        
        #* Build the UI on load.
        self.buildStartUI()

    def buildUncompletedUI(self):
        self.Ui = tk.Tk()
        self.dataPanel = tk.Frame(self.Ui)
        self.butPanel = tk.Frame(self.Ui)
        self.settingPanel = tk.Frame(self.butPanel)

        self.lblSelectedAction = tk.Label(self.butPanel, text="No currently selected action to modify.")
        self.lblSelectedAction.grid(row=1, column=2)

        self.db_view = ttk.Treeview(self.data_panel, column=("column1", "column2", "column3", "column4", "column5"), show='headings')
       # self.db_view.bind("<<TreeviewSelect>>", lambda event: self.onOrderSelect(self.db_view.item(self.db_view.selection())['values'][0]))
        self.db_view.column("#1", width=70)
        self.db_view.heading("#1", text="ID")
        self.db_view.heading("#2", text="Action")
        self.db_view.heading("#3", text="Deadline")
        self.db_view.heading("#4", text="Priority")
        self.db_view["displaycolumns"]=("column1", "column4", "column3", "column2")
        ysb = ttk.Scrollbar(self.data_panel, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side = tk.TOP)

        self.settingPanel.grid(row=2, column=0)
        
        self.dataPanel.pack(side = tk.TOP)
        self.butPanel.pack(side = tk.LEFT)
        self.pack()
        self.Ui.mainloop()
      
        

    
    def buildCompletedUI(self):
        self.Ui = tk.Tk()
        self.dataPanel = tk.Frame(self.Ui)
        self.butPanel = tk.Frame(self.Ui)
        self.settingPanel = tk.Frame(self.butPanel)

        self.lblSelectedAction = tk.Label(self.butPanel, text="No currently selected action to modify.")
        self.lblSelectedAction.grid(row=1, column=2)

        self.db_view = ttk.Treeview(self.dataPanel, column=("column1", "column2", "column3", "column4", "column5"), show='headings')
       # self.db_view.bind("<<TreeviewSelect>>", lambda event: self.onOrderSelect(self.db_view.item(self.db_view.selection())['values'][0]))
        self.db_view.column("#1", width=70)
        self.db_view.heading("#1", text="ID")
        self.db_view.heading("#2", text="Action")
        self.db_view.heading("#3", text="Deadline")
        self.db_view.heading("#4", text="Completed")
        self.db_view["displaycolumns"]=("column1", "column2", "column3", "column4")
        ysb = ttk.Scrollbar(self.dataPanel, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side = tk.TOP)

        self.settingPanel.grid(row=2, column=0)
        
        self.dataPanel.pack(side = tk.TOP)
        self.butPanel.pack(side = tk.LEFT)
        self.pack()
        self.Ui.mainloop()
        



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
#root.geometry("800x500") #* temporary window size

app = TkinterApp()
app.master.title("Acto")
app.mainloop()