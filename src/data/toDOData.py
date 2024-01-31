import sqlite3

class toDoData():
    def __init__(self):
        self.db = sqlite3.connect("src/data/storage/data.db")

    
    def completeAction(self, toDoID):
        c = self.db.cursor()
        print(f"Checking validity for the action with the id: {toDoID}...")

        c.execute('''SELECT state, content FROM Actions WHERE id = ?''', [toDoID]) #TODO: Remove the content parameter from the equation once whatever the fuck is not making it work is gone from the equation

        actionState = c.fetchone()
        if actionState == None:
            print(f"Invalid request: Action {toDoID} does not exist... 5x54e9")
            return
        
        print(f"{actionState[1]}")

        if actionState[0] == 0: #* Failsafe incase the state has not been initialized on the action
            for i in range(25):
                print("CRITICAL ERROR: 5x86e4 INVALID STATE. \n ACTION MUST BE DELETED.")
                #! Force user to manually remove the action, instead of making the user confused as to why their action randomly disappeared.
        elif actionState[0] == 1: #* If the state is set to "in progress"
            c = self.db.cursor()
            c.execute('''UPDATE Actions SET state = 2 WHERE id = ?''', [toDoID])
            self.db.commit()

    def deleteAction(self, actionID):
        c = self.db.cursor()
        print(f"Checking validity for the requested action...")
        
        c.execute('''SELECT id FROM Actions WHERE id = ?''', [actionID])
        
        action = c.fetchone()

        if action[0] == None:
            print(f"Invalid request: Action {actionID} does not exist... 5x57e9")
            return
        else:
            c.execute('''DELETE FROM Actions WHERE id = ?''', [actionID])
            print(f"Successfully deleted action {actionID}")


    def createAction(self, content="", deadline="", priority=0):
        print("Creating new todo...")
        c = self.db.cursor()
        c.execute('''INSERT INTO Actions (content, deadline, priority, state) VALUES (?,?,?,?)''', [content, deadline, priority, 1])
        self.db.commit()

        print("Created new todo.")

    def createTables(self):
        c = self.db.cursor()

        try: 
            c.execute('''
            CREATE TABLE Actions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT,
                deadline DATE,
                priority INTEGER,
                state INTEGER
            );
            ''')
        except:
            print("Table 'Actions' already exists... Passing...")

        self.db.commit()

