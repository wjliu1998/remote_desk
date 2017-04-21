#!/usr/bin/python
# encoding: utf-8
# File Name: makeform.py
# Author: Fang Yuan
# Mail: yfang@nju.edu.cn
# Created Time: Mon 30 May 2016 01:06:20 PM CST

from Tkinter import *
#注册窗口
class MakeForm2(Frame):
    vars = []
    def __init__(self, parent=None):
	Frame.__init__(self, parent)
	fontsel = ('Courier', 20, 'bold')
	self.pack()
        
        #生成用户名和口令窗口
        e = '用户名'
        row=Frame(self)
        lab=Label(row, font=fontsel, width=10, text=e)
        self.en1 = Entry(row,width=16,font=fontsel)
        row.pack(side=TOP,fill=X)
        lab.pack(side=LEFT)
        self.en1.pack(side=RIGHT,expand=YES,fill=X,padx=5, pady=5)
        self.vars.append(self.en1)

        e='口令'
        row=Frame(self)
        lab=Label(row, font=fontsel, width=10, text=e)
        self.en2 = Entry(row,width=16,font=fontsel,show='*')
        row.pack(side=TOP,fill=X)
        lab.pack(side=LEFT)
        self.en2.pack(side=RIGHT,expand=YES,fill=X,padx=5, pady=5)
        self.vars.append(self.en2)

	e='验证口令'
        row=Frame(self)
        lab=Label(row, font=fontsel, width=10, text=e)
        self.en3 = Entry(row,width=16,font=fontsel,show='*')
        row.pack(side=TOP,fill=X)
        lab.pack(side=LEFT)
        self.en3.pack(side=RIGHT,expand=YES,fill=X,padx=5, pady=5)
        self.vars.append(self.en3)

                
        #生成button

        self.login = Button(self)
        self.login["text"] = '注册'
        self.login["command"] = self.show #点击"注册" button 就可以输出密码和账号了,没有做验证
        self.login.pack({"side": "left"})

    def show(self):
        print "username:",self.en1.get()
        print "passwd:",self.en2.get()
	self.destroy()
	MakeForm().mainloop()


#登陆窗口
class MakeForm(Frame):
    vars = []
    def __init__(self, parent=None):
	Frame.__init__(self, parent)
	fontsel = ('Courier', 20, 'bold')
	self.pack()
        
	#生成用户名和口令窗口
	e = '用户名'
        row=Frame(self)
        lab=Label(row, font=fontsel, width=10, text=e)
        self.en1 = Entry(row,width=16,font=fontsel)
        row.pack(side=TOP,fill=X)
        lab.pack(side=LEFT)
        self.en1.pack(side=RIGHT,expand=YES,fill=X,padx=5, pady=5)
        self.vars.append(self.en1)

        e='口令'
        row=Frame(self)
        lab=Label(row, font=fontsel, width=10, text=e)
        self.en2 = Entry(row,width=16,font=fontsel,show='*')
        row.pack(side=TOP,fill=X)
        lab.pack(side=LEFT)
        self.en2.pack(side=RIGHT,expand=YES,fill=X,padx=5, pady=5)
        self.vars.append(self.en2)
	
	#生成两个button

        self.login = Button(self)
        self.login["text"] = '登陆'
	self.login["command"] = self.show
	#点击"log in" button 就可以输出密码和账号了,改show
        self.login.pack({"side": "left"})

	self.Make_acconts = Button(self)
        self.Make_acconts["text"] = '注册'
        self.Make_acconts["command"] = self.make #点击'make' button 就可以注册了
        self.Make_acconts.pack({"side": "left"})

    def show(self):
        print "username:",self.en1.get()
        print "passwd:",self.en2.get()
	exit()
	
    def make(self):
	self.destroy()
	MakeForm2().mainloop()



if __name__ == '__main__':
	MakeForm().mainloop()
