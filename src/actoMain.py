import sys
sys.dont_write_bytecode = True #* Don't write pycache.

import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
from data.actoData import actoData


#? Maybe set window to a constant size?

class TkinterApp(ttk.Frame):
    def __init__(self,root):
        #* For priority
        self.emptyStar = "☆"
        self.fullStar = "★"
        self.priorityRating = "0"

       
        self.root = root
        self.root.title("Acto")
        self.data = actoData()
        
        self.data.createTables() #* In case there are no tables.

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.uncompletedTabFrame = ttk.Frame(self.notebook)
        self.completedTabFrame = ttk.Frame(self.notebook)
        self.createActionTabFrame = ttk.Frame(self.notebook)


        self.notebook.add(self.uncompletedTabFrame, text="Uncompleted Actions")
        self.notebook.add(self.completedTabFrame, text="Completed Actions")
        self.notebook.add(self.createActionTabFrame, text="Create Action")

        self.buildCompletedUI()
        self.buildUncompletedUI()
        self.buildCreationUI()

        self.updateLabels()


    def onActionSelect(self, event):
        curItem = self.db_view.item(self.db_view.focus())['values']
        if len(curItem) > 0:
            self.lblCurrentSelect.config(text = 'Currently selected action: {}'.format(curItem[0]))
      
    def updateLabels(self): #TODO: Figure out how I could check the state variable for it, and then if it 
        l = self.data.getUncompletedActionList()

        self.lblActions.config(text = 'There are {} uncompleted Actions'.format(len(l)))
        self.db_view.delete(*self.db_view.get_children())
        for a in l:
            self.db_view.insert("", tk.END, values=(a.actionID, a.content, "", self.getPriority(a.priority)))

    def getPriority(self, number):
        return "★" * number + "☆" * (5 - number)

    def buildUncompletedUI(self):
        self.dataPanel = ttk.Frame(self.uncompletedTabFrame)
        self.butPanel = ttk.Frame(self.uncompletedTabFrame)
        self.settingPanel = ttk.Frame(self.butPanel)
        self.lblActions = ttk.Label(self.butPanel, text = 'There are no uncompleted Actions')
        self.lblActions.grid(row = 0, column = 0)
        self.butDelete = ttk.Button(self.butPanel, text = 'Delete Action', command=self.data.deleteAction)
        self.butDelete.grid(row = 4, column = 0)
       
        self.lblCurrentSelect = ttk.Label(self.butPanel, text="No currently selected Action.")
        self.lblCurrentSelect.grid(row=0, column=4, columnspan=2, padx=25)
        self.butOpen = ttk.Button(self.butPanel, text="Open Action", command=None)
        self.butOpen.grid(row = 1, column = 2, columnspan=2, padx=25)
        

        self.butNew = ttk.Button(self.butPanel, text = 'Create Action', command = self.buildCreationUI)
        self.butNew.grid(row=4, column=2, columnspan = 2)

        
        self.butCompleteActions = ttk.Button(self.butPanel, text = "Mark as completed", command=None)
        self.butCompleteActions.grid(row=4, column=4,columnspan=4)
         
   

        self.db_view = ttk.Treeview(self.dataPanel, column=("column1", "column2", "column3", "column4"), show='headings')
        self.db_view.bind("<ButtonRelease-1>", self.onActionSelect)
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
        #* Variables for the action
        self.actionContentEntry = ttk.Entry(self.createActionTabFrame)
        self.actionContentEntry.grid(row=1, column=0, columnspan=2)

        # self.lblDeadlineHeader = ttk.Label(self.createActionTabFrame, text="Set deadline (yyyy-mm-dd)")
        # self.lblDeadlineHeader.grid(row=2, column=0)

        self.lblPriorityHeader = ttk.Label(self.createActionTabFrame, text="Set priority.")
        self.lblPriorityHeader.grid(row=2, column=1, columnspan=3, padx=125)

        # self.deadlineEntry = ttk.Entry(self.createActionTabFrame)
        # self.deadlineEntry.grid(row=3, column=1)

        # self.butSetDeadline = ttk.Button(self.createActionTabFrame, text="Set Deadline", command=self.setDeadline)
        # self.butSetDeadline.grid(row=4, column=0)

        self.slPriority = ttk.LabeledScale(self.createActionTabFrame, from_ = 0, to = 5)
        #self.scPris.config(showvalue=1)
        self.slPriority.grid(row = 3, column = 2)

        # Button to create action
        self.createActionButton = ttk.Button(self.createActionTabFrame, text="Create Action", command=self.createAction)
        self.createActionButton.grid(row=5, column=0, columnspan=7)

    # def setDeadline(self):
    #     # Set self.deadline to the date entered in the entry
    #     deadline_str = self.deadlineEntry.get()
    #     try:
    #         self.deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
    #     except ValueError:
    #         print("Invalid date format. Please enter date in yyyy-mm-dd format.")

    def createAction(self):
        # Get content from entry
        self.content = self.actionContentEntry.get()
        self.priority = int(self.slPriority.scale.get())
        # Call data's createAction method
        self.data.createAction(content=self.content, priority=self.priority) #*Deadlines are put on hold for an indefinete time.
        self.updateLabels()


    def buildCompletedUI(self):

        self.dataPanel = ttk.Frame(self.completedTabFrame)
        self.butPanel = ttk.Frame(self.completedTabFrame)
        self.settingPanel = ttk.Frame(self.butPanel)
        self.lblActions = ttk.Label(self.butPanel, text = 'There are {} completed Actions'.format(None))
        self.lblActions.grid(row = 0, column = 0)

        self.lblCurrentSelect = ttk.Label(self.butPanel, text="No currently selected Action.")
        self.lblCurrentSelect.grid(row=0, column=2, columnspan=2, padx=25)
        self.butOpen = ttk.Button(self.butPanel, text="Open Action", command=None)
        self.butOpen.grid(row = 1, column = 2, columnspan=2)

        
        self.butUncompleteAction = ttk.Button(self.butPanel, text = "Mark as uncompleted", command=None)
        self.butUncompleteAction.grid(row=4, column=4,columnspan=4, padx=25)
         
   

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