import sqlite3

class Action():
    def __init__(self, content, priority, state):
        self.content = content
        self.priority = priority
        # self.deadline
        self.state = state
        

    def setId(self, id):
        self.actionID = id



class actoData():
    def __init__(self):
        self.db = sqlite3.connect("src/data/storage/data.db")

    

    def getCompletedActionList(self):
        c = self.db.cursor()
        c.execute('SELECT id, content, priority, state from Actions WHERE state = 2')
        Alist = []
        for a in c:
            action = Action(a[1],a[2], a[3])
            action.setId(a[0])
            Alist.append(action)
        return Alist

    def getUncompletedActionList(self):
        c = self.db.cursor()
        c.execute('SELECT id, content, priority, state from Actions WHERE state = 1')
        Alist = []
        for a in c:
            action = Action(a[1],a[2], a[3])
            action.setId(a[0])
            Alist.append(action)
        return Alist

    def completeAction(self, actionID):
        c = self.db.cursor()
        print(f"Checking validity for the action with the id: {actionID}...")

        c.execute('''SELECT state, content FROM Actions WHERE id = ?''', [actionID]) #TODO: Remove the content parameter from the equation once whatever the fuck is not making it work is gone from the equation

        actionState = c.fetchone()
        if actionState == None:
            print(f"Invalid request: Action {actionID} does not exist... 5x54e9")
            return
        
        print(f"{actionState[1]}")

        if actionState[0] == 0: #* Failsafe incase the state has not been initialized on the action
            for i in range(25):
                print("CRITICAL ERROR: 5x86e4 INVALID STATE. \n ACTION MUST BE DELETED.")
                #! Force user to manually remove the action, instead of making the user confused as to why their action randomly disappeared.
        elif actionState[0] == 1: #* If the state is set to "in progress"
            c.execute('''UPDATE Actions SET state = 2 WHERE id = ?''', [actionID])
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
            self.db.commit()


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
                state INTEGER,
                completeDate DATE
            );
            ''')
        except:
            print("Table 'Actions' already exists... Passing...")

        self.db.commit()

