from tkinter import *
import Back_end as v
import mysql.connector as mysql


def main(self,password,original_screen=None):
    mycom = mysql.connect(host='localhost', user='root', password=password, database='dc_comics')
    cur = mycom.cursor()
    self.geometry('370x330')
    self.title("Records on gotham criminals")
    self.config(bg='Black')
    cur.execute('select * from gotham_villain')
    forgot = cur.fetchall()
    name = cur.column_names
    name = [i.capitalize() for i in name]
    if 'Serial_number' not in name:
        cur.execute('alter table gotham_villain add Serial_number int auto_increment unique first')
        mycom.commit()
    a = v.Villain(self,password)
    if original_screen is not None:
        original_screen.destroy()

    def add_record(): #For adding a new criminal
        self.geometry('920x375')
        f12 = Frame(self, width=200, height=200)
        f12.grid(row=0, column=0)
        l11.grid_remove()
        b11.grid_remove()
        b22.grid_remove()
        b55.grid_remove()
        b77.grid_remove()
        b = v.Villain(f12,password)
        b.registration(self)

    def display_record(): #For displaying all the criminal
        mycom = mysql.connect(host='localhost', user='root', password=password, database='dc_comics')
        cur = mycom.cursor()
        cur.execute('select * from gotham_villain')
        data = cur.fetchall()
        biggest = ''
        for i in data:
            for j in i:
                if len(str(j)) > len(str(biggest)):
                    biggest = str(j)
        if len(data) != 0:
            self.geometry(f'{780+len(biggest)*15}x{100+40 * len(data)}')
        else:
            self.geometry(f'765x120')
        f1 = Frame(self, width=200, height=200)
        f1.grid(row=0, column=0)
        l11.grid_remove()
        b11.grid_remove()
        b22.grid_remove()
        b55.grid_remove()
        b77.grid_remove()
        b = v.Villain(f1,password)
        b.show_records(self)

    def back_to_main_menu(): #back_to_main_menu
        global f1
        f1.destroy()
        self.geometry('370x330')

    def alter_record(): #alter a record 
        global f1
        f1.destroy()
        l11.grid_remove()
        b11.grid_remove()
        b22.grid_remove()
        b55.grid_remove()
        b77.grid_remove()
        f12 = Frame(self)
        f12.grid(row=0, column=0, columnspan=5, rowspan=5)
        self.geometry('700x420')
        b = v.Villain(f12,password)
        b.updated(self)

    def remove_record(): #delete the record
        global f1
        f1.destroy()
        l11.grid_remove()
        b11.grid_remove()
        b22.grid_remove()
        b55.grid_remove()
        b77.grid_remove()
        f12 = Frame(self)
        f12.grid(row=0, column=0, columnspan=5, rowspan=5)
        self.geometry('700x200')
        b = v.Villain(f12,password)
        b.deleted(self)

    def update_record(): #open a new screen with alter,delete and back button
        global f1
        self.geometry('500x370')
        f1 = Frame(self)
        f1.grid(row=0, column=0, columnspan=4, rowspan=5)
        l13 = Label(f1, text="Update Records", fg='red', bg='black', font=('Times', '45'), highlightbackground='grey',
                    highlightthickness=2,
                    relief='solid')
        l13.grid(row=0, column=0, columnspan=3, sticky=W + E)
        b33 = Button(f1, text='Remove records', command=remove_record, fg='red', bg='black', font=('Times', '35'), width=20,
                     relief='solid', justify=CENTER, borderwidth=2,
                     highlightbackground='grey', highlightthickness=2)
        b33.grid(row=1, column=1, sticky=W + E)
        b44 = Button(f1, text='Alter records', command=alter_record, fg='red', bg='black', font=('Times', '35'), width=20,
                     relief='solid', justify=CENTER, borderwidth=2,
                     highlightbackground='grey', highlightthickness=2)
        b44.grid(row=2, column=1, sticky=W + E)
        b66 = Button(f1, text='Back ', command=back_to_main_menu, fg='red', bg='black', font=('Times', '35'), width=20,
                     relief='solid', justify=CENTER, borderwidth=2,
                     highlightbackground='grey', highlightthickness=2)
        b66.grid(row=3, column=1, sticky=W + E)


    #Main Menu
    l11 = Label(self, text="Gotham Police", fg='red', bg='black', font=('Times', '35'), highlightbackground='grey',
                highlightthickness=2,
                relief='solid')
    l11.grid(row=0, column=0, columnspan=3, sticky=W + E)
    b11 = Button(self, text='Add a new criminal', command=add_record, fg='red', bg='black', font=('Times', '25'), width=20,
                 relief='solid', justify=CENTER, borderwidth=2,
                 highlightbackground='grey', highlightthickness=2)
    b11.grid(row=1, column=1, sticky=W + E)
    b22 = Button(self, text='Show Gotham criminals', command=display_record, fg='red', bg='black', font=('Times', '25'),
                 width=20,
                 relief='solid', justify=CENTER, borderwidth=2,
                 highlightbackground='grey', highlightthickness=2)
    b22.grid(row=2, column=1, sticky=W + E)

    b55 = Button(self, text='Update Records', command=update_record, fg='red', bg='black', font=('Times', '25'), width=20,
                 relief='solid', justify=CENTER, borderwidth=2,
                 highlightbackground='grey', highlightthickness=2)
    b55.grid(row=3, column=1, sticky=W + E)
    b77 = Button(self, text='Exit', command=lambda: self.quit(), fg='red', bg='black', font=('Times', '25'), width=20,
                 relief='solid', justify=CENTER, borderwidth=2,
                 highlightbackground='grey', highlightthickness=2)
    b77.grid(row=5, column=1, sticky=W + E)
