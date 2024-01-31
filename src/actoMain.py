import sys
sys.dont_write_bytecode = True

import tkinter as tk
from data.actoData import actoData

data = actoData()

data.createTables()
data.deleteAction(1)

class TkinterApp:
    def __init__(self):
        self.placeholder = None


#! TODO: (HAHA GET IT!)
#!    - Utilize a radio button to toggle between completed and uncompleted. 