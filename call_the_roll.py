from tkinter import *
from tkinter import messagebox
import os,time,random,csv




lists = ['','','','','','','']#设置一个全局变量 保存数据；0:开始的提示语；1：班级列表；2：选择的班级
#3:学号   4：姓名    5:评分    6:时间戳
def how0():
    grade_pack=[]
    pack=os.listdir('/gitwork/call_the_roll/grade')
    word = '检测出有这些班级，请输入您想选择的班级\n'
    for i in pack:
        if '.csv' in i:
            i=i.split('.')[0]
            grade_pack.append(i)
            word+=i+'\t'
    return word,grade_pack
class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.master.geometry('450x450')
        self.master.resizable(0, 0)  	# 阻止Python GUI的大小调整
        self.createWidgets()
    def call_roll(self,grade_table):
        if '.csv' not in grade_table:
            grade_table+='.csv'
        with open('/gitwork/call_the_roll/grade/'+grade_table,'r',encoding='utf-8') as f:
            name_pack=[i for i in csv.reader(f)][1:]
            call_sb=random.sample(name_pack,1)[0]
            lists[3],lists[4]= call_sb[0],call_sb[1]
            self.sNO_value.set(lists[3])
            self.sname_value.set(lists[4])

    def createWidgets(self):
        # 增加菜单
        self.menuBar = Menu(self.master)  # 创建菜单的实例
        self.master.config(menu=self.menuBar)  # 将根窗口的顶级菜单设置为menu
        # 设置菜单选项
        # 创建一个下拉菜单‘关于’，这个菜单是挂在menubar（顶级菜单）上的
        # tearoff的值有0和1，为0时表示子菜单不独立出来。
        aboutMenu = Menu(self.menuBar, tearoff=0)
        # 创建一个下拉菜单‘功能’，这个菜单是挂在menubar（顶级菜单）上的
        moreMenu = Menu(self.menuBar, tearoff=0)
        # 用add_cascade()将菜单添加到顶级菜单中，按添加顺序排列
        self.menuBar.add_cascade(label='功能', menu=moreMenu)
        self.menuBar.add_cascade(label='帮助', menu=aboutMenu)
        # 下拉菜单的具体项目，使用add_command()方法
        aboutMenu.add_command(label='关于', command=self.About)
        moreMenu.add_command(label='其他', command=self.Other)
        #  增加输入框，确认班级，开始点名 ----------------------------
        self.textBar1 = Entry(self.master,bd='5')
        self.textBar1.place(x=0, y=120, width=120, height=40)
        self.Button4 = Button(self.master, text='确认班级', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0, \
                                              command=lambda: self.get_value())
        self.Button4.place(x=150, y=120, width=110, height=40)
        self.Button1 = Button(self.master, text='点名', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0, \
                                      command=lambda:   self.call_roll(lists[2]))
        self.Button1.place(x=300, y=120, width=80, height=40)
        # 显示面板
        self.result = StringVar()
        lists[0],lists[1]=how0()
        self.result.set(lists[0])  # 确认班级的显示板
        self.label2 = Label(self.master, font=('微软雅黑', 20), bg='#FFFFFF', bd='5', fg='black', anchor='center', \
                            textvariable=self.result)
        self.label2.place(y=0, width=450, height=120)
        ###################点名信息###############################
        self.sNO=StringVar()
        self.sNO_value=StringVar()
        self.grade_name=StringVar()
        self.grade_name_value=StringVar()
        self.sname=StringVar()
        self.sname_value=StringVar()
        self.pingafen=StringVar()
        self.pingafen_value=StringVar()
        self.grade_name.set('班级：')
        self.grade_name_value.set('')
        self.sNO.set('学号：')
        self.sNO_value.set('')
        self.sname.set('姓名：')
        self.sname_value.set('')
        self.pingafen.set('评分：')
        self.pingafen_value.set('')
        self.label7=Label(self.master,font=('微软雅黑', 20), bg='#FFFFFF', bd='10', fg='#828282', anchor='center',textvariable=self.grade_name)
        self.label3=Label(self.master,font=('微软雅黑', 20), bg='#FFFFFF', bd='10', fg='#828282', anchor='center',textvariable=self.sNO)
        self.label4=Label(self.master,font=('微软雅黑', 20), bg='#FFFFFF', bd='10', fg='#828282', anchor='center',textvariable=self.sname)
        self.label5=Label(self.master,font=('微软雅黑', 20), bg='#FFFFFF', bd='10', fg='#828282', anchor='center',textvariable=self.sname_value)
        self.label6=Label(self.master,font=('微软雅黑', 20), bg='#FFFFFF', bd='10', fg='#828282', anchor='center',textvariable=self.sNO_value)
        self.label8=Label(self.master,font=('微软雅黑', 20), bg='#FFFFFF', bd='10', fg='#828282', anchor='center',textvariable=self.grade_name_value)
        self.label9=Label(self.master,font=('微软雅黑', 20), bg='#FFFFFF', bd='10', fg='#828282', anchor='center',textvariable=self.pingafen)
        self.label10=Label(self.master,font=('微软雅黑', 20), bg='#FFFFFF', bd='10', fg='#828282', anchor='center',textvariable=self.pingafen_value)
        self.label3.place(x=200,y=165,width=70, height=50)#学号
        self.label4.place(x=5,y=225,width=70, height=50)#姓名
        self.label5.place(x=70,y=225,width=120, height=50)#姓名值
        self.label6.place(x=280,y=165,width=120, height=50)#学号值
        self.label7.place(x=5,y=165,width=70, height=50)#班级
        self.label8.place(x=70,y=165,width=120, height=50)#班级值
        self.label9.place(x=200,y=225,width=70, height=50)#评分
        self.label10.place(x=280,y=225,width=120, height=50)#评分值
        ######################打分键###########################

        self.result2 = StringVar()  # 显示面板显示结果2，用于显示计算过程
        self.result2.set('评分:')
        self.label = Label(self.master, font=('黑体', 15), bg='#FFFFFF', bd='10', fg='#828282', anchor='center', \
                                textvariable=self.result2)
        self.label.place(x=0,y=300,width=50, height=50)
        self.Button2 = Button(self.master, text='A', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=5, \
                              command=lambda: self.pingfen('A'))
        self.Button2.place(x=50, y=300, width=80, height=50)
        self.Button3 = Button(self.master, text='B', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0, \
                              command=lambda: self.pingfen('B'))
        self.Button3.place(x=150, y=300, width=80, height=50)
        self.Button4 = Button(self.master, text='C', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0, \
                                      command=lambda: self.pingfen('C'))
        self.Button4.place(x=250, y=300, width=80, height=50)
        self.Button5 = Button(self.master, text='D', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0, \
                                      command=lambda: self.pingfen('D'))
        self.Button5.place(x=350, y=300, width=80, height=50)
        self.Button6 = Button(self.master, text='确认打分', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0, \
                                              command=lambda:   self.save_result())
        self.Button6.pack(side=BOTTOM,pady=50)
    def pingfen(self, val):
        lists[5]=val
        self.pingafen_value.set(lists[5])
    def get_value(self):
        value=self.textBar1.get()
        if str(value) in lists[1]:
            messagebox.showinfo('确认提示','你选择的要点名的班级是{ggrade}'.format(ggrade=value))
            lists[2]=value
            self.result.set('')  # 确认班级的显示板
            self.grade_name_value.set(lists[2])
            for kk in range(-3,0):
                lists[kk]=''
            self.pingafen_value.set('')
            self.sname_value.set('')
            self.sNO_value.set('')
        else:
            messagebox.showerror('提示','没有这个班级，请重新输入')
            lists[2]=''
            self.result.set(lists[0])
    def About(self):
        messagebox.showinfo('关于', 'Ver 1.0 \n---\nBy zeis\n')

    def Other(self):
        messagebox.showinfo('功能', ' 暂时没有其他功能\n emmmm...')
    def save_result(self):
        timeArray = time.localtime(int(time.time()))
        otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        lists[6]=otherStyleTime
        if '' in lists:
            messagebox.showwarning('结果有误','结果格式不正确，有空值')
        else:
            with open('result.csv','a',encoding='utf-8') as f:
                write=csv.writer(f)
                write.writerow(lists[-5:])
            messagebox.showinfo('打分成功','已成功打分，结果已保存')
                

        

#实例化Application()类
app = Application()
# 设置窗口标题:
app.master.title('点名')
# 主消息循环:
app.mainloop()