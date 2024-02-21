import tkinter as tk
from tkinter import ttk

class BroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bro's Super Cool Tabs")

        # Create a ttk Notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, padx=10, fill='both', expand=True)

        # Create frames for each tab
        self.tab1_frame = ttk.Frame(self.notebook)
        self.tab2_frame = ttk.Frame(self.notebook)
        self.tab3_frame = ttk.Frame(self.notebook)

        # Add tabs to the Notebook
        self.notebook.add(self.tab1_frame, text="Tab 1")
        self.notebook.add(self.tab2_frame, text="Tab 2")
        self.notebook.add(self.tab3_frame, text="Tab 3")

        # Populate Tab 1 with your existing code
        self.populate_tab1()
        self.populate_tab2()
        self.populate_tab3()

    def populate_tab1(self):
        self.dataPanel = ttk.Frame(self.tab1_frame)
        self.butPanel = ttk.Frame(self.tab1_frame)
        self.settingPanel = ttk.Frame(self.butPanel)

        self.lblActions = ttk.Label(self.butPanel, text='There are {} uncompleted Actions'.format(None))
        self.lblActions.grid(row=0, column=0)
        self.butUpdate = ttk.Button(self.butPanel, text='Edit Action', command=None)
        self.butUpdate.grid(row=1, column=0)
        self.butUpdate = ttk.Button(self.butPanel, text='Show completed Actions', command=self.buildCompletedUI)
        self.butUpdate.grid(row=4, column=0)

        self.lblCurrentSelect = ttk.Label(self.butPanel, text="No currently selected Action.")
        self.lblCurrentSelect.grid(row=0, column=4, columnspan=2, padx=25)
        self.butOpen = ttk.Button(self.butPanel, text="Open Action", command=None)
        self.butOpen.grid(row=1, column=2, columnspan=2, padx=25)

        self.butNew = ttk.Button(self.butPanel, text='Create Action', command=None)
        self.butNew.grid(row=4, column=2, columnspan=2)

        self.butCompleteActions = ttk.Button(self.butPanel, text="Mark as uncompleted", command=None)
        self.butCompleteActions.grid(row=4, column=4, columnspan=4)

        self.db_view = ttk.Treeview(self.dataPanel, column=("column1", "column2", "column3", "column4"), show='headings')
        self.db_view.column("#1", width=30)
        self.db_view.heading("#1", text="ID")
        self.db_view.heading("#2", text="Action")
        self.db_view.heading("#3", text="Deadline")
        self.db_view.heading("#4", text="Priority")
        self.db_view["displaycolumns"] = ("column1", "column2", "column3", "column4")
        ysb = ttk.Scrollbar(self.dataPanel, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side=tk.TOP)

        self.dataPanel.pack(side=tk.TOP)
        self.butPanel.pack(side=tk.LEFT)
        self.settingPanel.grid(row=2, column=2)

    def populate_tab2(self):
        label = ttk.Label(self.tab2_frame, text="Welcome to Tab 2!")
        label.pack(padx=10, pady=10)

    def populate_tab3(self):
        label = ttk.Label(self.tab3_frame, text="Tab 3 in the house, yo!")
        label.pack(padx=10, pady=10)

    def buildCompletedUI(self):
        pass  # Add functionality for showing completed actions here

if __name__ == "__main__":
    root = tk.Tk()
    app = BroApp(root)
    root.mainloop()
