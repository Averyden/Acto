import sys
sys.dont_write_bytecode = True

import tkinter as tk
from data.toDOData import toDoData

data = toDoData()

data.createTables()
data.completeAction(1)

class TkinterApp:
    def __init__(self):
        self.placeholder = None


#! TODO: (HAHA GET IT!)
#!    - Utilize a radio button to toggle between completed and uncompleted. 