import Tkinter # External modules
import random

    
class App(Tkinter.Tk): # Main Class
    
    def __init__(self,parent): # init fuction, required
        Tkinter.Tk.__init__(self,parent) # Constructor
        self.parent = parent # Keeps track of parent
        self.initialize() # Calls initialize function

    def initialize(self): #This fuction builds the GUI
        self.a = Tkinter.IntVar()
        self.grid()
        self.label = Tkinter.Label(self, text = "Welcome to the Space Fleet Battle Simulator.").grid(row=1, column=0)
        
        # Labels in front of entry boxes
        self.label_attdmg = Tkinter.Label(self, text = "Attacking Fleet's Damage:", bg='red', fg='white').grid(row=2, column=0, sticky='W')
        self.label_attdef = Tkinter.Label(self, text = "Attacking Fleet's Defense:", bg='red', fg='white').grid(row=3, column=0, sticky='W')
        self.label_attsup = Tkinter.Label(self, text = "Attacking Fleet's Support:", bg='red', fg='white').grid(row=4, column=0, sticky='W')
        self.label_atttac = Tkinter.Label(self, text = "Attacking Fleet's Tactics:", bg='red', fg='white').grid(row=5, column=0, sticky='W')
        self.label_defdmg = Tkinter.Label(self, text = "Defending Fleet's Damage:", bg='blue', fg='white').grid(row=6, column=0, sticky='W')
        self.label_defdef = Tkinter.Label(self, text = "Defending Fleet's Defense:", bg='blue', fg='white').grid(row=7, column=0, sticky='W')
        self.label_defsup = Tkinter.Label(self, text = "Defending Fleet's Support:", bg='blue', fg='white').grid(row=8, column=0, sticky='W')
        self.label_deftac = Tkinter.Label(self, text = "Defending Fleet's Tactics:", bg='blue', fg='white').grid(row=9, column=0, sticky='W')
        
        # Labels in from of output values
        self.label_title1 = Tkinter.Label(self, text= 'Attack Output:').grid(row=11, column=0, sticky='W')
        self.label_title2 = Tkinter.Label(self, text= 'Defender Output:').grid(row=12, column=0, sticky='W') 
        self.label_title3 = Tkinter.Label(self, text= 'Attacker\'s Remining Defense:').grid(row=13, column=0, sticky='W')
        self.label_title4 = Tkinter.Label(self, text= 'Defender\'s Remaining Defense:').grid(row=14, column=0, sticky='W')        
        
        # Variable placeholders for all input
        self.a = Tkinter.IntVar() 
        self.b = Tkinter.IntVar()
        self.c = Tkinter.IntVar()
        self.d = Tkinter.IntVar()
        self.e = Tkinter.IntVar()
        self.f = Tkinter.IntVar()
        self.g = Tkinter.IntVar()
        self.h = Tkinter.IntVar()
        
        # Variable placeholders for all output
        self.attack_output    = Tkinter.IntVar()
        self.defense_output   = Tkinter.IntVar()
        self.att_def_remain   = Tkinter.IntVar()
        self.defe_defe_remain = Tkinter.IntVar()        
        
        self.entry_attdmg = Tkinter.Entry(self, textvariable=self.a) # Attacking Fleets Damage Input
        self.entry_attdmg.grid(row=2, column=1)
        
        self.entry_attdef = Tkinter.Entry(self, textvariable=self.b) # Attacking Fleets Defense Input
        self.entry_attdef.grid(row=3, column=1)
        
        self.entry_attsup = Tkinter.Entry(self, textvariable=self.c) # Attacking Fleets Support Systems Input
        self.entry_attsup.grid(row=4, column=1)
        
        self.entry_atttac = Tkinter.Entry(self, textvariable=self.d) # Attacking Fleets Tactical Bonus Input
        self.entry_atttac.grid(row=5, column=1)
        
        self.entry_defdmg = Tkinter.Entry(self, textvariable=self.e) # Defending Fleets Damage Input
        self.entry_defdmg.grid(row=6, column=1)
        
        self.entry_defdef = Tkinter.Entry(self, textvariable=self.f) # Defending Fleets Defense Input
        self.entry_defdef.grid(row=7, column=1)
        
        self.entry_defsup = Tkinter.Entry(self, textvariable=self.g) # Defending Fleets Support Systems Input
        self.entry_defsup.grid(row=8, column=1)
        
        self.entry_deftac = Tkinter.Entry(self, textvariable=self.h) # Defending Fleets Tactical Bonus Input
        self.entry_deftac.grid(row=9, column=1)        
        
        # Button to call battle function
        self.button_battle = Tkinter.Button(self, text = 'Click to Calculate Battle', command=self.battle)
        self.button_battle.grid(row=10, column=0, sticky='E')
        
        # Labels for the outputs
        self.attack_output_label    = Tkinter.Label(self, textvariable=self.attack_output).grid(row=11, column=1, sticky='W')
        self.defense_output_label   = Tkinter.Label(self, textvariable=self.defense_output).grid(row=12, column=1, sticky='W')   
        self.att_def_remain_label   = Tkinter.Label(self, textvariable=self.att_def_remain).grid(row=13, column=1, sticky='W')
        self.defe_defe_remain_label = Tkinter.Label(self, textvariable=self.defe_defe_remain).grid(row=14, column=1, sticky='W')        
    
    def battle(self): # Custom battle equation for simulation
        att_dmg_rand = random.randrange(1, 3, 1)
        att_sup_rand = random.randrange(1, 4, 1)
        att_tac_rand = random.randrange(1, 6, 1)
        
        def_dmg_rand = random.randrange(1, 3, 1)
        def_sup_rand = random.randrange(1, 4, 1)
        def_tac_rand = random.randrange(1, 6, 1)        
        
        self.attack_output.set((att_dmg_rand * self.a.get()) + (att_sup_rand * self.c.get()) + (att_tac_rand * self.d.get()))
        self.defense_output.set((def_dmg_rand * self.e.get()) + (def_sup_rand * self.g.get()) + (def_tac_rand * self.h.get()))
        self.att_def_remain.set(self.b.get() - self.defense_output.get())  
        self.defe_defe_remain.set(self.f.get() - self.attack_output.get())
        
        
        self.b.set(self.b.get() - self.defense_output.get())
        self.f.set(self.f.get() - self.attack_output.get())

if __name__ == "__main__": # Sets title and geometry for GUI and loops
    app = App(None)
    app.title('Space Fleet Battle Simulator v1.0')
    app.geometry('375x300')
    app.mainloop()           