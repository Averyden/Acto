import sys
sys.dont_write_bytecode = True #* Don't write pycache.

import tkinter as tk
import tkinter.ttk as ttk
from data.actoData import actoData


#? Maybe set window to a constant size?

class TkinterApp(ttk.Frame):
    def __init__(self,root):
        self.root = root
        self.root.title("Acto")
        self.data = actoData()

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.uncompletedTabFrame = ttk.Frame(self.notebook)
        self.completedTabFrame = ttk.Frame(self.notebook)

        self.notebook.add(self.uncompletedTabFrame, text="Uncompleted Actions")
        self.notebook.add(self.completedTabFrame, text="Completed Actions")

        self.buildCompletedUI()
        self.buildUncompletedUI()

        #* For priority
        self.emptyStar = "☆"
        self.fullStar = "★"
        self.priorityRating = "0"

    def updateLabels(self): #* Automatically run every time code is started so that things are added to the ma bobs
        pass 

    def buildUncompletedUI(self):
        self.dataPanel = ttk.Frame(self.uncompletedTabFrame)
        self.butPanel = ttk.Frame(self.uncompletedTabFrame)
        self.settingPanel = ttk.Frame(self.butPanel)
        self.lblActions = ttk.Label(self.butPanel, text = 'There are {} uncompleted Actions'.format(None))
        self.lblActions.grid(row = 0, column = 0)
        self.butUpdate = ttk.Button(self.butPanel, text = 'Edit Action', command=None)
        self.butUpdate.grid(row = 4, column = 0)
       
        self.lblCurrentSelect = ttk.Label(self.butPanel, text="No currently selected Action.")
        self.lblCurrentSelect.grid(row=0, column=4, columnspan=2, padx=25)
        self.butOpen = ttk.Button(self.butPanel, text="Open Action", command=None)
        self.butOpen.grid(row = 1, column = 2, columnspan=2, padx=25)
        

        self.butNew = ttk.Button(self.butPanel, text = 'Create Action', command = None)
        self.butNew.grid(row=4, column=2, columnspan = 2)

        
        self.butCompleteActions = ttk.Button(self.butPanel, text = "Mark as uncompleted", command=None)
        self.butCompleteActions.grid(row=4, column=4,columnspan=4)
         
   

        self.db_view = ttk.Treeview(self.dataPanel, column=("column1", "column2", "column3", "column4"), show='headings')
        #self.db_view.bind("<ButtonRelease-1>", self.on_guitar_selected)
        self.db_view.column("#1", width=30)
        self.db_view.heading("#1", text="ID")
        self.db_view.heading("#2", text="Action")
        self.db_view.heading("#3", text="Deadline")
        self.db_view.heading("#4", text="Priority")
        self.db_view["displaycolumns"]=("column1", "column2", "column3", "column4")
        ysb = ttk.Scrollbar(self.dataPanel, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side = tk.TOP)

        self.dataPanel.pack(side = tk.TOP)
        self.butPanel.pack(side = tk.LEFT)
        self.settingPanel.grid(row=2, column=2)
      
        
    def buildCreationUI(self):


        self.but_list = []
        
        for i in range(5):
            self.starButton = ttk.Button(self.settingPanel, text=self.emptyStar, command=lambda idx=i: self.setStarRating(idx), width=0.2)
            self.starButton.grid(row=0, column=i)
            self.but_list.append(self.starButton)


    
    def buildCompletedUI(self):

        self.dataPanel = ttk.Frame(self.completedTabFrame)
        self.butPanel = ttk.Frame(self.completedTabFrame)
        self.settingPanel = ttk.Frame(self.butPanel)
        self.lblActions = ttk.Label(self.butPanel, text = 'There are {} completed Actions'.format(None))
        self.lblActions.grid(row = 0, column = 0)

        self.lblCurrentSelect = ttk.Label(self.butPanel, text="No currently selected Action.")
        self.lblCurrentSelect.grid(row=0, column=2, columnspan=2)
        self.butOpen = ttk.Button(self.butPanel, text="Open Action", command=None)
        self.butOpen.grid(row = 1, column = 2, columnspan=2)

        
        self.butUncompleteAction = ttk.Button(self.butPanel, text = "Mark as uncompleted", command=None)
        self.butUncompleteAction.grid(row=4, column=4,columnspan=4)
         
   

        self.db_view = ttk.Treeview(self.dataPanel, column=("column1", "column2", "column3", "column4"), show='headings')
        #self.db_view.bind("<ButtonRelease-1>", self.on_guitar_selected)
        self.db_view.column("#1", width=30)
        self.db_view.heading("#1", text="ID")
        self.db_view.heading("#2", text="Action")
        self.db_view.heading("#3", text="Deadline")
        self.db_view.heading("#4", text="Completed")
        self.db_view["displaycolumns"]=("column1", "column2", "column3", "column4")
        ysb = ttk.Scrollbar(self.dataPanel, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side = tk.TOP)

        self.dataPanel.pack(side = tk.TOP)
        self.butPanel.pack(side = tk.LEFT)
        self.settingPanel.grid(row=2, column=2)






root = tk.Tk()
#root.geometry("800x500") #* temporary window size
app = TkinterApp(root)
root.mainloop()