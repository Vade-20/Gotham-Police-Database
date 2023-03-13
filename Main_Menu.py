from tkinter import *
import Back_end as v
import mysql.connector as mysql


def main(root, password):
    mycom = mysql.connect(host='localhost', user='root', password=password, database='dc_comics')
    cur = mycom.cursor()
    root.geometry('370x330')
    root.title("Records on gotham criminals")
    root.config(bg='Black')
    cur.execute('select * from gotham_villain')
    forgot = cur.fetchall()
    name = cur.column_names
    name = [i.capitalize() for i in name]
    if 'Serial_number' not in name:
        cur.execute('alter table gotham_villain add serial_number int auto_increment unique first')
        mycom.commit()
    a = v.Villain(root,password)

    def add_record(): #For adding a new criminal
        root.geometry('881x375')
        f12 = Frame(root, width=200, height=200)
        f12.grid(row=0, column=0)
        l11.grid_remove()
        b11.grid_remove()
        b22.grid_remove()
        b55.grid_remove()
        b77.grid_remove()
        b = v.Villain(f12,password)
        b.registration(root)

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
            root.geometry(f'{780+len(biggest)*15}x{100+40 * len(data)}')
        else:
            root.geometry(f'765x120')
        f1 = Frame(root, width=200, height=200)
        f1.grid(row=0, column=0)
        l11.grid_remove()
        b11.grid_remove()
        b22.grid_remove()
        b55.grid_remove()
        b77.grid_remove()
        b = v.Villain(f1,password)
        b.show_records(root)

    def back_to_main_menu(): #back_to_main_menu
        global f1
        f1.destroy()
        root.geometry('370x330')

    def alter_record(): #alter a record 
        global f1
        f1.destroy()
        l11.grid_remove()
        b11.grid_remove()
        b22.grid_remove()
        b55.grid_remove()
        b77.grid_remove()
        f12 = Frame(root)
        f12.grid(row=0, column=0, columnspan=5, rowspan=5)
        root.geometry('700x420')
        b = v.Villain(f12,password)
        b.updated(root)

    def remove_record(): #delete the record
        global f1
        f1.destroy()
        l11.grid_remove()
        b11.grid_remove()
        b22.grid_remove()
        b55.grid_remove()
        b77.grid_remove()
        f12 = Frame(root)
        f12.grid(row=0, column=0, columnspan=5, rowspan=5)
        root.geometry('700x200')
        b = v.Villain(f12,password)
        b.deleted(root)

    def update_record(): #open a new screen with alter,delete and back button
        global f1
        root.geometry('500x370')
        f1 = Frame(root)
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
    l11 = Label(root, text="Gotham Police", fg='red', bg='black', font=('Times', '35'), highlightbackground='grey',
                highlightthickness=2,
                relief='solid')
    l11.grid(row=0, column=0, columnspan=3, sticky=W + E)
    b11 = Button(root, text='Add a new criminal', command=add_record, fg='red', bg='black', font=('Times', '25'), width=20,
                 relief='solid', justify=CENTER, borderwidth=2,
                 highlightbackground='grey', highlightthickness=2)
    b11.grid(row=1, column=1, sticky=W + E)
    b22 = Button(root, text='Show Gotham criminals', command=display_record, fg='red', bg='black', font=('Times', '25'),
                 width=20,
                 relief='solid', justify=CENTER, borderwidth=2,
                 highlightbackground='grey', highlightthickness=2)
    b22.grid(row=2, column=1, sticky=W + E)

    b55 = Button(root, text='Update Records', command=update_record, fg='red', bg='black', font=('Times', '25'), width=20,
                 relief='solid', justify=CENTER, borderwidth=2,
                 highlightbackground='grey', highlightthickness=2)
    b55.grid(row=3, column=1, sticky=W + E)
    b77 = Button(root, text='Exit', command=lambda: root.quit(), fg='red', bg='black', font=('Times', '25'), width=20,
                 relief='solid', justify=CENTER, borderwidth=2,
                 highlightbackground='grey', highlightthickness=2)
    b77.grid(row=5, column=1, sticky=W + E)
