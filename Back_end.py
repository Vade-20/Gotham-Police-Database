class Villain:
    def __init__(self, root,password):
        self.root = root
        self.password = password

    def registration(self, original_screen): #For adding a record in database
        import tkinter
        import mysql.connector as mysql
        global e1, e2, e3, e4, e5, e6
        mycom = mysql.connect(host="localhost", user="root", password=self.password, database="dc_comics")
        cur = mycom.cursor()

        def back(n=None): #Goes back to the main menu
            import Main_Menu
            Main_Menu.main(original_screen, self.password,self.root)

        def yes(n=None): #ask if the values enter in the entery box are correct
            try:
                cur.execute('select * from gotham_villain')
                data = cur.fetchall()
                a = len(data) + 1
                d = f"insert into gotham_villain values({a},'{e1.get()}','{e2.get()}','{e3.get()}','{e4.get()}',{int(e5.get())},'{e6.get()}"
                sen = f"insert into gotham_villain values({a},'{e1.get()}','{e2.get()}','{e3.get()}','{e4.get()}',{int(e5.get())},'{e6.get()}') "
                cur.execute(sen)
                mycom.commit()
                e1.delete(0, tkinter.END)
                e2.delete(0, tkinter.END)
                e3.delete(0, tkinter.END)
                e4.delete(0, tkinter.END)
                e5.delete(0, tkinter.END)
                e6.delete(0, tkinter.END)    
                e1.focus_set()           
            except:
                from tkinter import messagebox
                error = messagebox.showerror('Error', 'Please enter the proper information in proper format')


        def no(): #delete the existing value inside the entry boxes
            global r
            original_screen.geometry('920x375')
            tkinter.Label(self.root, text="Do you want to erase all entries", fg='red', bg='black',
                          font=('Times', '20'),
                          highlightbackground='grey', highlightthickness=2,
                          relief='solid').grid(row=7, column=0, sticky=tkinter.W + tkinter.E)
            r = tkinter.IntVar()
            r1 = tkinter.Radiobutton(self.root, text='Yes', variable=r, value=1, fg='red', command=delete_values, bg='black',
                                     font=('Times', '18'),
                                     width=5, borderwidth=2,
                                     relief='solid', highlightbackground='grey', highlightthickness=2)
            r1.grid(row=7, column=1, sticky=tkinter.W + tkinter.E)
            r1.deselect()
            r2 = tkinter.Radiobutton(self.root, text='No', variable=r, value=0, fg='red', bg='black', command=delete_values,
                                     font=('Times', '18'),
                                     width=5, borderwidth=2,
                                     relief='solid', highlightbackground='grey', highlightthickness=2)
            r2.grid(row=7, column=2, sticky=tkinter.W + tkinter.E)
            r2.deselect()

        def delete_values(): #Check if you want delete all the values inside the entry box
            global r
            if r.get() == 1:
                e1.delete(0, tkinter.END)
                e2.delete(0, tkinter.END)
                e3.delete(0, tkinter.END)
                e4.delete(0, tkinter.END)
                e5.delete(0, tkinter.END)
                e6.delete(0, tkinter.END)
                tkinter.Label(self.root, text="Are the given Entries correct-", fg='red', bg='black',
                              font=('Times', '20'),
                              highlightbackground='grey', highlightthickness=5,
                              relief='solid').grid(row=7, column=0, sticky=tkinter.W + tkinter.E)
                tkinter.Button(self.root, text='Yes', command=yes, fg='red', bg='black', font=('Times', '18'), width=5,
                               borderwidth=2,
                               relief='solid',
                               highlightbackground='grey', highlightthickness=1).grid(row=7, column=1,
                                                                                      sticky=tkinter.W + tkinter.E)
                tkinter.Button(self.root, text='No', command=no, fg='red', bg='black', font=('Times', '18'), width=5,
                               borderwidth=2,
                               relief='solid',
                               highlightbackground='grey', highlightthickness=1).grid(row=7, column=2,
                                                                                      sticky=tkinter.W + tkinter.E)
            else:
                tkinter.Label(self.root, text="Are the given Entries correct-", fg='red', bg='black',
                              font=('Times', '20'),
                              highlightbackground='grey', highlightthickness=5,
                              relief='solid').grid(row=7, column=0, sticky=tkinter.W + tkinter.E)
                tkinter.Button(self.root, text='Yes', command=yes, fg='red', bg='black', font=('Times', '18'), width=5,
                               borderwidth=2,
                               relief='solid',
                               highlightbackground='grey', highlightthickness=1).grid(row=7, column=1,
                                                                                      sticky=tkinter.W + tkinter.E)
                tkinter.Button(self.root, text='No', command=no, fg='red', bg='black', font=('Times', '18'), width=5,
                               borderwidth=2,
                               relief='solid',
                               highlightbackground='grey', highlightthickness=1).grid(row=7, column=2,
                                                                                      sticky=tkinter.W + tkinter.E)

        l1 = tkinter.Label(self.root, text="Gotham Villain New Member Form", fg='red', bg='black', font=('Times', '25'),
                           highlightbackground='grey',
                           highlightthickness=2,
                           relief='solid')
        l1.grid(row=0, column=0, columnspan=3, sticky=tkinter.W + tkinter.E)
        l2 = tkinter.Label(self.root, text="Enter the real name of  criminal", fg='red', bg='black', font=('Times', '20'),
                           highlightbackground='grey',
                           highlightthickness=2,
                           relief='solid')
        l2.grid(row=1, column=0, sticky=tkinter.W + tkinter.E)
        l3 = tkinter.Label(self.root, text="Enter the criminal Alias", fg='red', bg='black', font=('Times', '20'),
                           highlightbackground='grey',
                           highlightthickness=2,
                           relief='solid')
        l3.grid(row=2, column=0, sticky=tkinter.W + tkinter.E)
        l4 = tkinter.Label(self.root, text="Enter the criminal other alias ", fg='red', bg='black',
                           font=('Times', '20'),
                           highlightbackground='grey', highlightthickness=2,
                           relief='solid')
        l4.grid(row=3, column=0, sticky=tkinter.W + tkinter.E)
        l5 = tkinter.Label(self.root, text="Enter date of birth of criminal (YYYY-MM-DD) ", fg='red', bg='black', font=('Times', '20'),
                           highlightbackground='grey', highlightthickness=2,
                           relief='solid')
        l5.grid(row=4, column=0, sticky=tkinter.W + tkinter.E)
        l6 = tkinter.Label(self.root, text="Enter the criminal bank balance", fg='red', bg='black', font=('Times', '20'),
                           highlightbackground='grey',
                           highlightthickness=2,
                           relief='solid')
        l6.grid(row=5, column=0, sticky=tkinter.W + tkinter.E)
        l7 = tkinter.Label(self.root, text="Enter the Gender of the criminal", fg='red', bg='black', font=('Times', '20'),
                           highlightbackground='grey',
                           highlightthickness=2,
                           relief='solid')
        l7.grid(row=6, column=0, sticky=tkinter.W + tkinter.E)
        l8 = tkinter.Label(self.root, text="Are the given Entries correct-", fg='red', bg='black', font=('Times', '20'),
                           highlightbackground='grey', highlightthickness=2, borderwidth=4,
                           relief='solid')
        l8.grid(row=7, column=0, sticky=tkinter.W + tkinter.E)

        e1 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e2 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e3 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e4 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e5 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e6 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e7 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e8 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e1.grid(row=1, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)
        e2.grid(row=2, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)
        e3.grid(row=3, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)
        e4.grid(row=4, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)
        e5.grid(row=5, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)
        e6.grid(row=6, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)
        e7.grid(row=7, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)
        e8.grid(row=7, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)

        b1 = tkinter.Button(self.root, text='Yes', command=yes, fg='red', bg='black', font=('Times', '15'), width=10,
                            relief='solid',
                            highlightbackground='grey', highlightthickness=2)
        b1.grid(row=7, column=1, sticky=tkinter.W + tkinter.E)
        b2 = tkinter.Button(self.root, text='No', command=no, fg='red', bg='black', font=('Times', '15'), width=20,
                            relief='solid',
                            highlightbackground='grey', highlightthickness=2)
        b2.grid(row=7, column=2, sticky=tkinter.W + tkinter.E)
        b3 = tkinter.Button(self.root, text='Back', command=back, fg='red', bg='black', font=('Times', '15'), width=10,
                            relief='solid',
                            highlightbackground='grey', highlightthickness=2)
        b3.grid(row=8, column=0, sticky=tkinter.W + tkinter.E, columnspan=3)
        original_screen.bind('<Escape>',back)
        original_screen.bind('<Return>',yes)


    def show_records(self, original_screen):
        import mysql.connector as mysql
        import tkinter
        mycom = mysql.connect(host='localhost', user='root', password=self.password, database='dc_comics')
        cur = mycom.cursor()
        def back(n=None):   #Goes back to the main menu
            import Main_Menu
            Main_Menu.main(original_screen, self.password,self.root)
        
        cur.execute('desc gotham_villain')
        la = tkinter.Label(self.root, text="Gotham Criminals", fg='red', bg='black', font=('Times', '25'),
                           highlightbackground='grey',
                           highlightthickness=2,
                           relief='solid')
        la.grid(row=0, column=0, columnspan=7, sticky=tkinter.W + tkinter.E)
        data = cur.fetchall()
        for a,i in enumerate(data):
            l1 = tkinter.Label(self.root, text=i[0], fg='red', bg='black', font=('Times', '18'),
                               highlightbackground='grey',
                               highlightthickness=2, relief='solid')
            l1.grid(row=1, column=a, sticky=tkinter.W + tkinter.E)

        cur.execute('select * from gotham_villain')
        data = cur.fetchall()
        for r,i in enumerate(data,start=2):
            for j in range(0, 7):
                ran = tkinter.Label(self.root, text=i[j], fg='red', bg='black', font=('Times', '15'), padx=20,
                                    highlightbackground='grey',
                                    highlightthickness=2, relief='solid')
                ran.grid(row=r, column=j, sticky=tkinter.W + tkinter.E)
        b3 = tkinter.Button(self.root, text='Back', command=back, fg='red', bg='black', font=('Times', '15'), width=10,
                            relief='solid',
                            highlightbackground='grey', highlightthickness=2)
        b3.grid(row=len(data) + 2, column=0, columnspan=7, sticky=tkinter.W + tkinter.E)
        original_screen.bind('<Escape>',back)


    def deleted(self, original_screen): #For deleting record from database
        import tkinter
        import mysql.connector as mysl
        mycom = mysl.connect(host='localhost', user='root', password=self.password, database='dc_comics')
        cur = mycom.cursor()

        def back(n=None): #Goes back to the main menu
            import Main_Menu
            Main_Menu.main(original_screen, self.password,self.root)


        def delete_record():
            global e1
            alias = e1.get()
            alias = alias.split('--')
            cur.execute(f'delete from gotham_villain where serial_number = "{alias[0]}" ')
            mycom.commit()
            slide = tkinter.OptionMenu(self.root, default, *criminal_list(), command=show)
            slide.config(fg='red', bg='black', font=('Times', '15'), width=40, relief='solid',
                         highlightbackground='grey', highlightthickness=2)
            slide.grid(row=1, column=0, sticky=tkinter.W + tkinter.E, columnspan=3)
            e1.delete(0, tkinter.END)

        def criminal_list():
            cur.execute('select * from gotham_villain')
            data = cur.fetchall()
            a = ['Show the Member of Gotham Villain']
            for i in data:
                sen = str(i[0]) + '--' + str(i[2])
                a.append(sen)
            return a

        def show(value): #insert value inside the entry box
            if default.get()!="Show the Member of Gotham Villain":
                global e1
                e1 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '18'), width=20, borderwidth=2,
                                    relief='solid',
                                    highlightbackground='grey', highlightthickness=2)
                e1.grid(row=0, column=3, sticky=tkinter.W + tkinter.E)
                e1.insert(0, default.get())

                default.set(criminals[0])

        criminals = criminal_list()
        default = tkinter.StringVar()
        default.set(criminals[0])
        slide = tkinter.OptionMenu(self.root, default, *criminals, command=show)
        slide.config(fg='red', bg='black', font=('Times', '15'), width=40, relief='solid',
                     highlightbackground='grey', highlightthickness=2)
        slide.grid(row=1, column=0, sticky=tkinter.W + tkinter.E, columnspan=3)
        b3 = tkinter.Button(self.root, text='Delete', command=delete_record, fg='red', bg='black', font=('Times', '15'),
                            width=10,
                            relief='solid',
                            highlightbackground='grey', highlightthickness=2)
        b3.grid(row=1, column=3, sticky=tkinter.W + tkinter.E)
        tkinter.Label(self.root, text='Criminal Id-', fg='red', bg='black', font=('Times', '18'), width=20,
                      borderwidth=2,
                      relief='solid',
                      highlightbackground='grey', highlightthickness=2).grid(row=0, column=0, columnspan=3,
                                                                             sticky=tkinter.W + tkinter.E)
        tkinter.Label(self.root, text='------------------', fg='red', bg='black', font=('Times', '18'), width=20,
                      borderwidth=2,
                      relief='solid',
                      highlightbackground='grey', highlightthickness=2).grid(row=0, column=3,
                                                                             sticky=tkinter.W + tkinter.E)
        b3 = tkinter.Button(self.root, text='Back', command=back, fg='red', bg='black', font=('Times', '15'), width=10,
                            relief='solid',
                            highlightbackground='grey', highlightthickness=2)
        b3.grid(row=2, column=0, columnspan=4, sticky=tkinter.W + tkinter.E)
        original_screen.bind('<Escape>',back)


    def updated(self, original_screen):
        import tkinter
        import mysql.connector as mysql
        global e1, e2, e3, e4, e5, e6
        mycom = mysql.connect(host="localhost", user="root", password=self.password, database="dc_comics")
        cur = mycom.cursor()

        def back(n=None):
            import Main_Menu
            Main_Menu.main(original_screen, self.password,self.root)

        def criminal_list():
            cur.execute('select * from gotham_villain')
            data = cur.fetchall()
            a = ['Show the Member of Gotham Villain']
            for i in data:
                sen = str(i[0]) + '--' + str(i[1]) + '--' + str(i[2]) + '--' + str(i[3]) + '--' + str(
                    i[4]) + '--' + str(i[5]) + '--' + str(i[6])
                a.append(sen)
            return a

        def insert_record():
            try:
                global e10
                value = e10.get()
                value = value.split('--')
                e1.delete(0, tkinter.END)
                e2.delete(0, tkinter.END)
                e3.delete(0, tkinter.END)
                e4.delete(0, tkinter.END)
                e5.delete(0, tkinter.END)
                e6.delete(0, tkinter.END)

                e1.insert(0, value[1])
                e2.insert(0, value[2])
                e3.insert(0, value[3])
                e4.insert(0, value[4])
                e5.insert(0, value[5])
                e6.insert(0, value[6])
            except IndexError:
                pass

        def updates_record(n=None):
            global e10
            value = e10.get()
            value = value.split('--')
            v1 = e1.get()
            v2 = e2.get()
            v3 = e3.get()
            v4 = e4.get()
            v5 = e5.get()
            v6 = e6.get()
            sen = f'update gotham_villain set name="{v1}",secret_identity="{v2}",alter_name="{v3}",date_of_birth="{v4}",' \
                  f'bank_balance={v5},sex="{v6}" where serial_number = {value[0]} '
            cur.execute(sen)
            mycom.commit()
            e1.delete(0, tkinter.END)
            e2.delete(0, tkinter.END)
            e3.delete(0, tkinter.END)
            e4.delete(0, tkinter.END)
            e5.delete(0, tkinter.END)
            e6.delete(0, tkinter.END)
            e10.delete(0, tkinter.END)

            slide = tkinter.OptionMenu(self.root, checking, *a, command=show)
            slide.config(fg='red', bg='black', font=('Times', '15'), width=40, relief='solid',
                         highlightbackground='grey', highlightthickness=2)
            slide.grid(row=7, column=0, sticky=tkinter.W + tkinter.E, columnspan=3)

        def show(value):
            if checking.get() != 'Show the Member of Gotham Villain':
                global e10
                e10 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '18'), width=20, borderwidth=2,
                                    relief='solid',
                                    highlightbackground='grey', highlightthickness=2)
                e10.grid(row=9, column=0, columnspan=3, sticky=tkinter.W + tkinter.E)
                
                e10.insert(0, checking.get())
                insert_record()
                checking.set(a[0])

        a = criminal_list()
        checking = tkinter.StringVar()
        checking.set(a[0])
        slide = tkinter.OptionMenu(self.root, checking, *a, command=show)
        slide.config(fg='red', bg='black', font=('Times', '15'), width=40, relief='solid',
                     highlightbackground='grey', highlightthickness=2)
        slide.grid(row=7, column=0, sticky=tkinter.W + tkinter.E, columnspan=3)
        l1 = tkinter.Label(self.root, text="Gotham Villain Update Form", fg='red', bg='black', font=('Times', '25'),
                           highlightbackground='grey',
                           highlightthickness=2,
                           relief='solid')
        l1.grid(row=0, column=0, columnspan=3, sticky=tkinter.W + tkinter.E)
        l8 = tkinter.Label(self.root, text="Enter the name of  criminal", fg='red', bg='black', font=('Times', '20'),
                           highlightbackground='grey',
                           highlightthickness=2,
                           relief='solid')
        l8.grid(row=1, column=0, sticky=tkinter.W + tkinter.E)
        l2 = tkinter.Label(self.root, text="Enter the crimial alias", fg='red', bg='black', font=('Times', '20'),
                           highlightbackground='grey',
                           highlightthickness=2,
                           relief='solid')
        l2.grid(row=2, column=0, sticky=tkinter.W + tkinter.E)
        l3 = tkinter.Label(self.root, text="Enter the criminal other alias ", fg='red', bg='black',
                           font=('Times', '20'),
                           highlightbackground='grey', highlightthickness=2,
                           relief='solid')
        l3.grid(row=3, column=0, sticky=tkinter.W + tkinter.E)
        l4 = tkinter.Label(self.root, text="Enter the criminal date of birth", fg='red', bg='black', font=('Times', '20'),
                           highlightbackground='grey', highlightthickness=2,
                           relief='solid')
        l4.grid(row=4, column=0, sticky=tkinter.W + tkinter.E)
        l5 = tkinter.Label(self.root, text="Enter the criminal bank balance", fg='red', bg='black', font=('Times', '20'),
                           highlightbackground='grey',
                           highlightthickness=2,
                           relief='solid')
        l5.grid(row=5, column=0, sticky=tkinter.W + tkinter.E)
        l6 = tkinter.Label(self.root, text="Enter the Gender of the criminal", fg='red', bg='black', font=('Times', '20'),
                           highlightbackground='grey',
                           highlightthickness=2,
                           relief='solid')
        l6.grid(row=6, column=0, sticky=tkinter.W + tkinter.E)

        e1 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e2 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e3 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e4 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e5 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e6 = tkinter.Entry(self.root, fg='red', bg='black', font=('Times', '20'), width=20, borderwidth=2,
                           relief='solid',
                           highlightbackground='grey', highlightthickness=2)
        e1.grid(row=1, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)
        e2.grid(row=2, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)
        e3.grid(row=3, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)
        e4.grid(row=4, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)
        e5.grid(row=5, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)
        e6.grid(row=6, column=1, columnspan=2, sticky=tkinter.W + tkinter.E)

        b3 = tkinter.Button(self.root, text='Update', command=updates_record, fg='red', bg='black', font=('Times', '15'),
                            width=10,
                            relief='solid',
                            highlightbackground='grey', highlightthickness=2)
        b3.grid(row=8, column=0, columnspan=2, sticky=tkinter.W + tkinter.E)
        b4 = tkinter.Button(self.root, text='Back', command=back, fg='red', bg='black', font=('Times', '15'), width=10,
                            relief='solid',
                            highlightbackground='grey', highlightthickness=2)
        b4.grid(row=8, column=2, sticky=tkinter.W + tkinter.E)
        original_screen.bind('<Escape>',back)
        original_screen.bind('<Return>',updates_record)
