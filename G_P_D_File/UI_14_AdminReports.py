from tkinter import *
from tkinter import ttk
import _14_AdminReports
import dbConnection

root = Tk()
root.title("Admin Report")

def AdminReports(c, master):
    #creating frames
    
    tabControl = ttk.Notebook(master)
    tab1 = Frame(tabControl)
    tab2 = Frame(tabControl)
    tab3 = Frame(tabControl)
    tab4 = Frame(tabControl)

    tabControl.add(tab1, text ='Bookings per Cinema')
    tabControl.add(tab2, text ='Revenue per Cinema')
    tabControl.add(tab3, text ='Top Revenue Movie')
    tabControl.add(tab4, text ='Staff Bookings')
    tabControl.pack(expand = 1, fill ="both")

    #tab1
    tree1 = ttk.Treeview(tab1,selectmode="browse")
    tree1.grid(row=0,column=1)
    tree1["columns"] = ("1", "2", "3")
    tree1['show'] = 'headings'
    tree1.column("1", width = 120, anchor ='c')
    tree1.column("2", width = 120, anchor ='c')
    tree1.column("3", width = 120, anchor ='c')
    tree1.heading("1", text ="Cinema ID")
    tree1.heading("2", text ="Cinema Name")
    tree1.heading("3", text ="Total Bookings")
    scrollbar = ttk.Scrollbar(tab1, orient=VERTICAL, command=tree1.yview)
    tree1.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=2, sticky='ns')
    
    #tab2
    tree2 = ttk.Treeview(tab2,selectmode="browse")
    tree2.grid(row=0,column=1)
    tree2["columns"] = ("1", "2", "3")
    tree2['show'] = 'headings'
    tree2.column("1", width = 120, anchor ='c')
    tree2.column("2", width = 120, anchor ='c')
    tree2.column("3", width = 120, anchor ='c')
    tree2.heading("1", text ="Cinema ID")
    tree2.heading("2", text ="Cinema Name")
    tree2.heading("3", text ="Total Revenue")
    scrollbar = ttk.Scrollbar(tab2, orient=VERTICAL, command=tree1.yview)
    tree2.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=2, sticky='ns')
    
    #tab3
    tree3 = ttk.Treeview(tab3,selectmode="browse")
    tree3.grid(row=0,column=1)
    tree3["columns"] = ("1", "2", "3")
    tree3['show'] = 'headings'
    tree3.column("1", width = 75, anchor ='c')
    tree3.column("2", width = 165, anchor ='w')
    tree3.column("3", width = 120, anchor ='c')
    tree3.heading("1", text ="Movie ID")
    tree3.heading("2", text ="Movie Name")
    tree3.heading("3", text ="Movie Revenue")
    scrollbar = ttk.Scrollbar(tab3, orient=VERTICAL, command=tree1.yview)
    tree3.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=2, sticky='ns')

    #tab4
    tree4 = ttk.Treeview(tab4,selectmode="browse")
    tree4.grid(row=0,column=1)
    tree4["columns"] = ("1", "2", "3")
    tree4['show'] = 'headings'
    tree4.column("1", width = 120, anchor ='c')
    tree4.column("2", width = 120, anchor ='c')
    tree4.column("3", width = 120, anchor ='c')
    tree4.heading("1", text ="User ID")
    tree4.heading("2", text ="User Name")
    tree4.heading("3", text ="Total Bookings")
    scrollbar = ttk.Scrollbar(tab4, orient=VERTICAL, command=tree1.yview)
    tree4.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=2, sticky='ns')

    #calling functions from _14_AdminReports.py
    BPC = _14_AdminReports.bookings_per_cinema(c)
    RPC = _14_AdminReports.revenue_per_cinema(c)
    TRM = _14_AdminReports.top_revenue_movie(c)
    SB = _14_AdminReports.staff_bookings(c)
    
    #add data to the treeview
    for bookings in BPC:
        tree1.insert('', END, values=bookings)
    for revenues in RPC:
        tree2.insert('', END, values=revenues)
    for movie_revenue in TRM:
        tree3.insert('', END, values=movie_revenue)
    for staff_bookings in SB:
        tree4.insert('', END, values=staff_bookings)

root.mainloop()