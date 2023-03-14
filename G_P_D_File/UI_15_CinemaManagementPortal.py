from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Cinema Management Portal")

class Show:
    def __init__(self, master):
        self.tree1 = ttk.Treeview(selectmode="browse")
        self.tree1.grid(row=0,column=1)
        self.tree1["columns"] = ("1", "2", "3")
        self.tree1['show'] = 'headings'
        self.tree1.column("1", width = 120, anchor ='c')
        self.tree1.column("2", width = 120, anchor ='c')
        self.tree1.column("3", width = 120, anchor ='c')
        self.tree1.heading("1", text ="Cinema ID")
        self.tree1.heading("2", text ="Cinema Name")
        self.tree1.heading("3", text ="Total Bookings")
        scrollbar = ttk.Scrollbar(self.tab1, orient=VERTICAL, command=self.tree1.yview)
        self.tree1.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=2, sticky='ns')