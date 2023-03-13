from tkinter import *
import Main_Menu
import mysql.connector as mysql

root = Tk()
root.title("Records on gotham criminals")
root.config(bg='black')
root.geometry('830x173')


def check(): #check whether if the user have a database name dc_comics with tabel name gotham_villain.It also check whether the password entered is correct or not
    global password
    password = e1.get()
    try:
        mycom = mysql.connect(host='localhost', user='root', password=password)
        cur = mycom.cursor()
        if mycom.is_connected():
            cur.execute('show databases')
            data = cur.fetchall()
            data = [i[0] for i in data]
            if 'dc_comics' not in data:
                cur.execute('create database dc_comics')
                mycom.commit()
            cur.execute('use dc_comics')
            mycom.commit()
            cur.execute('show tables')
            data = cur.fetchall()
            data = [i[0] for i in data]
            if 'gotham_villain' not in data:
                cur.execute('''create table gotham_villain(Serial_number int not null primary key auto_increment,
                Name varchar(100),Secret_Identity varchar(100),ALter_name varchar(100),Date_of_birth date,Bank_balance int,Sex varchar(100)''')
                mycom.commit()
            e1.destroy()
            l1.destroy()
            l2.destroy()
            b2.destroy()
            b1.destroy()
            Main_Menu.main(root, password)
    except mysql.ProgrammingError:
        from tkinter import messagebox
        messagebox.showerror('Error', 'Incorrect password (Hint: Type your Mysql password)')
        e1.delete(0, END)


def main_main():
    global e1, l1, l2, b1, b2
    l1 = Label(root, text='Gotham Police', fg='red', bg='black', relief='solid', padx=250, font=('Times', '40'),
               highlightthickness=2, highlightbackground='grey'
               )
    l1.grid(row=0, columnspan=2, column=0, sticky=W + E)
    l2 = Label(root, text='Enter Password', fg='red', bg='black', relief='solid', font=('Times', '25'),
               highlightthickness=2, highlightbackground='grey'
               )
    l2.grid(row=1, column=0, sticky=W + E)
    e1 = Entry(root, fg='red', bg='black', relief='solid', font=('Times', '25'),
              highlightthickness=2, highlightbackground='grey'
              )
    e1.grid(row=1, column=1, sticky=W + E)
    b1 = Button(root, fg='red', bg='black', relief='solid', font=('Times', '25'), text='Exit',
               command=lambda: root.quit(),
               highlightthickness=2, highlightbackground='grey'
               )
    b1.grid(row=2, column=0, sticky=W + E)
    b2 = Button(root, fg='red', bg='black', relief='solid', font=('Times', '25'), text='Enter', command=check,
                highlightthickness=2, highlightbackground='grey'
                )
    b2.grid(row=2, column=1, sticky=W + E)


main_main()

mainloop()

