from tkinter import *
from tkinter import ttk

import messagebox
from sqlalchemy import Column,Integer,String,create_engine,Float

from sqlalchemy.orm import sessionmaker,declarative_base
engine = create_engine('sqlite:///florist.db', echo=True)

base = declarative_base()
sessions=sessionmaker(bind=engine)
session = sessions()


class flower(base):
    __tablename__ = 'flowers'
    id=Column(Integer,primary_key=True)

    race=Column(String)
    color=Column(String)
    size=Column(String)
    price=Column(Integer)
    def __init__(self,race='',color='',size='',price=0):
        self.race=race
        self.color=color
        self.size=size
        self.price=price
base.metadata.create_all(engine)
class application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createWidgets()
        self.Load()
    def createWidgets(self):
        self.input()
        self.label()
        self.ButtonForm()
        self.Table()
    def input(self):
        # txt
        self.txtRace = Entry(self.master, justify='center')
        self.txtRace.place(x=100, y=100)
        self.txtColor = Entry(self.master, justify='center')
        self.txtColor.place(x=100, y=140)
        self.comboSize = ttk.Combobox(self.master)
        self.comboSize["values"] = ('Small', 'Medium', 'Large')
        self.comboSize.current(1)
        self.comboSize.place(x=100, y=180)
        self.txtPrice = Entry(self.master, justify='center')
        self.txtPrice.place(x=100, y=220)

    def label(self):
        self.lblRace=Label(self.master, text="Race")
        self.lblRace.place(x=50, y=100)
        self.lblColor= Label(self.master, text="Color")
        self.lblColor.place(x=50, y=140)
        self.lblSize = Label(self.master, text="Size")
        self.lblSize.place(x=50, y=180)
        self.lblPrice= Label(self.master, text="Price")
        self.lblPrice.place(x=50, y=220)
    def ButtonForm(self):
        self.btnRegister = Button(self.master, text="Register")
        self.btnRegister.bind("<Button-1>", self.onClickRegister)
        self.btnRegister.place(x=100, y=300)

    def Table(self):
        columns=('c1','c2','c3','c4')
        self.table=ttk.Treeview(self.master, columns=columns, show='headings')
        headers=['Race','Color','Size','Price']
        for i in range(4):
            self.table.column(columns[i], width=100)
            self.table.heading(columns[i], text=headers[i])
        """
        self.table.column(columns[0], width=100)
        self.table.column(columns[1], width=100)
        self.table.column(columns[2], width=100)
        self.table.column(columns[3], width=100)
        
        self.table.heading(columns[0],text="race")
        self.table.heading(columns[1],text="color")
        self.table.heading(columns[2],text="size")
        self.table.heading(columns[3],text="price")
         """
        self.table.place(x=300,y=100)
    def onClickRegister(self,e):
        flower1=flower(race=self.txtRace.get(),color=self.txtColor.get(),size=self.comboSize.get(),price=int(self.txtPrice.get()))
        self.register(flower1)
        self.Load()
    def register(self,flower1):
        session.add(flower1)
        session.commit()
    def Inset(self,flower1):
        self.table.insert('','end',values=[flower1.race,flower1.color,flower1.size,flower1.price])

    def Load(self):
        alldata=session.query(flower).all()
        self.cleanTable()
        for data in alldata:
            self.Inset(data)

    def cleanTable(self):
        for item in self.table.get_children():
            self.table.delete(item)
if __name__=="__main__":
    win=Tk()
    win.geometry("800x600")
    app=application(master=win)

    win.mainloop()