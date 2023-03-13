from tkinter import *
import Back_end as v
import mysql.connector as mysql


def back(self, ab, password):

    mycom = mysql.connect(host='localhost', user='root', password=password, database='dc_comics')
    cur = mycom.cursor()
    cur.execute('select * from gotham_villain')
    name = cur.column_names
    forgot = cur.fetchall()
    name = [i.capitalize() for i in name]
    if 'Serial_number' not in name:
        cur.execute('alter table gotham_villain add serial_number int auto_increment unique first')
        mycom.commit()
    self.destroy()


    def upp():
        global f1
        f1.destroy()
        l11.grid_remove()
        b11.grid_remove()
        b22.grid_remove()
        b55.grid_remove() 
        b77.grid_remove()
        f12 = Frame(ab)
        f12.grid(row=0, column=0, columnspan=5, rowspan=5)
        ab.geometry('700x420')
        b = v.Villain(f12, password)
        b.updated(ab)

    ab.title("Records on gotham criminals")
    ab.config(bg='Black')
    ab.geometry('370x330')
    a = v.Villain(ab, password)

    def backed():
        global f1
        f1.destroy()
        ab.geometry('370x330')

    def perma():
        global f1
        f1.destroy()
        l11.grid_remove()
        b11.grid_remove()
        b22.grid_remove()
        b55.grid_remove()
        b77.grid_remove()
        f12 = Frame(ab)
        f12.grid(row=0, column=0, columnspan=5, rowspan=5)
        ab.geometry('700x200')
        b = v.Villain(f12, password)
        b.deleted(ab)

    def delete():
        global f1
        ab.geometry('500x370')
        f1 = Frame(ab)
        f1.grid(row=0, column=0, columnspan=4, rowspan=5)
        l13 = Label(f1, text="Update Records", fg='red', bg='black', font=('Times', '45'),
                            highlightbackground='grey',
                            highlightthickness=2,
                            relief='solid')
        l13.grid(row=0, column=0, columnspan=3, sticky=W + E)
        b33 = Button(f1, text='Remove records', command=perma, fg='red', bg='black',
                             font=('Times', '35'),
                             width=20,
                             relief='solid', justify=CENTER, borderwidth=2,
                             highlightbackground='grey', highlightthickness=2)
        b33.grid(row=1, column=1, sticky=W + E)
        b44 = Button(f1, text='Alter records', command=upp, fg='red', bg='black',
                             font=('Times', '35'),
                             width=20,
                             relief='solid', justify=CENTER, borderwidth=2,
                             highlightbackground='grey', highlightthickness=2)
        b44.grid(row=2, column=1, sticky=W + E)
        b66 = Button(f1, text='Back ', command=backed, fg='red', bg='black', font=('Times', '35'),
                             width=20,
                             relief='solid', justify=CENTER, borderwidth=2,
                             highlightbackground='grey', highlightthickness=2)
        b66.grid(row=3, column=1, sticky=W + E)

    def add():
        ab.geometry('881x375')
        f12 = Frame(ab, width=200, height=200)
        f12.grid(row=0, column=0)
        l11.grid_remove()
        b11.grid_remove()
        b22.grid_remove()
        b55.grid_remove()
        b77.grid_remove()
        b = v.Villain(f12, password)
        b.registration(ab)

    def display():
        import mysql.connector as mysl
        mycom = mysl.connect(host='localhost', user='root', password=password, database='dc_comics')
        cur = mycom.cursor()
        cur.execute('select * from gotham_villain ')
        data = cur.fetchall()
        biggest = ''
        for i in data:
            for j in i:
                if len(str(j))>len(str(biggest)):
                    biggest = j
        if len(data) != 0:
            ab.geometry(f'{785+len(str(biggest))*15}x{100+40 * len(data)}')
        else:
            ab.geometry(f'765x120')
        f1 = Frame(ab, width=200, height=200)
        f1.grid(row=0, column=0)
        l11.grid_remove()
        b11.grid_remove()
        b22.grid_remove()
        b55.grid_remove()
        b77.grid_remove()
        b = v.Villain(f1, password)
        b.show_records(ab)

    l11 = Label(ab, text="Gotham Police", fg='red', bg='black', font=('Times', '35'),
                        highlightbackground='grey',
                        highlightthickness=2,
                        relief='solid')
    l11.grid(row=0, column=0, columnspan=3, sticky=W + E)
    b11 = Button(ab, text='Add a new criminal', command=add, fg='red', bg='black', font=('Times', '25'),
                         width=20,
                         relief='solid', justify=CENTER, borderwidth=2,
                         highlightbackground='grey', highlightthickness=2)
    b11.grid(row=1, column=1, sticky=W + E)
    b22 = Button(ab, text='Show Gotham criminals', command=display, fg='red', bg='black',
                         font=('Times', '25'),
                         width=20,
                         relief='solid', justify=CENTER, borderwidth=2,
                         highlightbackground='grey', highlightthickness=2)
    b22.grid(row=2, column=1, sticky=W + E)
    b55 = Button(ab, text='Update Records', command=delete, fg='red', bg='black', font=('Times', '25'),
                         width=20,
                         relief='solid', justify=CENTER, borderwidth=2,
                         highlightbackground='grey', highlightthickness=2)
    b55.grid(row=3, column=1, sticky=W + E)
    b77 = Button(ab, text='Exit', command=lambda: ab.quit(), fg='red', bg='black', font=('Times', '25'),
                         width=20,
                         relief='solid', justify=CENTER, borderwidth=2,
                         highlightbackground='grey', highlightthickness=2)
    b77.grid(row=5, column=1, sticky=W + E)
