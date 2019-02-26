import sys
import datetime
import MySQLdb
import atexit
from PyQt4 import QtCore, QtGui
import xlsxwriter
import sqlite3

host=None
port=None
userd=None
passwdd=None
dbb=None
conn = sqlite3.connect('dbdetail.db')
c = conn.cursor()
c.execute("SELECT * FROM db")
data1 = c.fetchall()
for row in data1:
    host=row[2]
    port=row[1]
    userd=row[0]
    passwdd=row[3]
    dbb=row[4]

def getdb():
    conn = sqlite3.connect('dbdetail.db')
    c = conn.cursor()
    c.execute("SELECT * FROM db")
    data1 = c.fetchall()
    for row in data1:
        host=row[2]
        port=row[1]
        userd=row[0]
        passwdd=row[3]
        dbb=row[4]
db2=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
cursor1 = db1.cursor()
cursor2 = db2.cursor()
now = datetime.datetime.now()
p = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
t = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
tp = str(now.day) + "-" + str(now.month) + "-" + str(now.year)

def setdt():
    p = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
    t = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    tp = str(now.day) + "-" + str(now.month) + "-" + str(now.year)


da=now.weekday()
flags = QtCore.Qt.ItemFlags()
flags != QtCore.Qt.ItemIsEnabled

class Ui_dbedit(object):
    def setupUi(self, dbedit):
        dbedit.resize(428, 409)
        self.pushButton = QtGui.QPushButton(dbedit)
        self.pushButton.setGeometry(QtCore.QRect(20, 370, 85, 28))
        self.pushButton_2 = QtGui.QPushButton(dbedit)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 370, 85, 28))
        self.toolButton = QtGui.QToolButton(dbedit)
        self.toolButton.setGeometry(QtCore.QRect(240, 170, 51, 27))
        self.hostedit = QtGui.QLineEdit(dbedit)
        self.hostedit.setGeometry(QtCore.QRect(30, 70, 171, 28))
        self.useredit = QtGui.QLineEdit(dbedit)
        self.useredit.setGeometry(QtCore.QRect(230, 70, 161, 28))
        self.passedit = QtGui.QLineEdit(dbedit)
        self.passedit.setGeometry(QtCore.QRect(30, 170, 171, 28))
        self.portedit = QtGui.QLineEdit(dbedit)
        self.portedit.setGeometry(QtCore.QRect(30, 260, 171, 28))
        self.dbaseedit = QtGui.QLineEdit(dbedit)
        self.dbaseedit.setGeometry(QtCore.QRect(222, 260, 161, 28))
        self.label = QtGui.QLabel(dbedit)
        self.label.setGeometry(QtCore.QRect(40, 40, 66, 20))
        self.label_2 = QtGui.QLabel(dbedit)
        self.label_2.setGeometry(QtCore.QRect(240, 40, 71, 20))
        self.label_3 = QtGui.QLabel(dbedit)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 71, 20))
        self.label_4 = QtGui.QLabel(dbedit)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 66, 20))
        self.label_5 = QtGui.QLabel(dbedit)
        self.label_5.setGeometry(QtCore.QRect(230, 230, 66, 20))
        self.passedit.setEchoMode(QtGui.QLineEdit.Password)
        self.pushButton.clicked.connect(self.change)
        self.pushButton.clicked.connect(self.close)
        self.toolButton.pressed.connect(self.pas)
        self.toolButton.released.connect(self.ps)

        self.retranslateUi(dbedit)
        QtCore.QMetaObject.connectSlotsByName(dbedit)
    def pas(self):
        self.passedit.setEchoMode(QtGui.QLineEdit.Normal)

    def ps(self):
        self.passedit.setEchoMode(QtGui.QLineEdit.Password)
    def change(self):
        conn = sqlite3.connect('dbdetail.db')
        c = conn.cursor()
        a1=self.hostedit.text()
        b1=self.passedit.text()
        c1=self.useredit.text()
        d1=int(self.portedit.text())
        e1=self.dbaseedit.text()
        c.execute("UPDATE db SET user='%s', port='%s', host='%s', password='%s', dbb='%s' WHERE user='%s'"%(c1,d1,a1,b1,e1,userd))
        conn.commit()
        self.uip = Dialog(20)
        self.uip.show()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()

    def retranslateUi(self, dbedit):
        dbedit.setWindowTitle("Database")
        self.pushButton.setText("Edit")
        self.pushButton_2.setText("Cancel")
        self.toolButton.setText("Show")
        self.label.setText("Host")
        self.label_2.setText("User")
        self.label_3.setText("Password")
        self.label_4.setText("Port")
        self.label_5.setText("Database")
        self.hostedit.setText(host)
        self.useredit.setText(userd)
        self.passedit.setText(passwdd)
        self.portedit.setText(str(port))
        self.dbaseedit.setText(dbb)

class dbedit(QtGui.QDialog, Ui_dbedit):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)

        self.setupUi(self)



class user():
    username = None
    name = None
    admin = None
    password = None
    shift = None


    def getdata(self):
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT * FROM USER WHERE username='%s'" % (self.username))
        data1 = cursor1.fetchall()
        if now.hour < 7 or now.hour >= 21:
            self.shift = 'Night'
        elif now.hour >= 14 and now.hour < 21:
            self.shift = "Evening"
        elif now.hour < 14 and now.hour >= 7:
            self.shift = "Morning"
        for row in data1:
            self.username = row[0]
            self.password = row[1]
            self.name = row[2]
            self.admin = row[5]
def datecheck():
    if now.hour>=0 and now.hour<7 :
        p = str(now.day-1) + "-" + str(now.month) + "-" + str(now.year)
    elif now.hour==7 and now.minute<30:
        p=str(now.day-1) + "-" + str(now.month) + "-" + str(now.year)
    else:
        p = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
u1 = user()

class Ui_Printwindow(object):

    def setupUi(self, Printwindow):
        datecheck()
        self.centralwidget = QtGui.QWidget(Printwindow)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.gridLayout.addWidget(self.dateEdit, 1, 2, 1, 1)
        self.dateEdit.setCalendarPopup(True)
        self.label = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 3, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("Morning")
        self.comboBox.addItem("Evening")
        self.comboBox.addItem("Night")
        self.dateEdit.setDisplayFormat( "d/M/yyyy")
        self.dateEdit.setDate(datetime.datetime.strptime(p, "%d-%m-%Y"))
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        Printwindow.setCentralWidget(self.centralwidget)
        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton.clicked.connect(self.prnt)
        self.retranslateUi(Printwindow)
        QtCore.QMetaObject.connectSlotsByName(Printwindow)

    def retranslateUi(self, Printwindow):
        Printwindow.setWindowTitle( "Print")
        self.label.setText( "Shift")
        self.pushButton_2.setText( "Cancel")
        self.label_2.setText( "Date")
        self.pushButton.setText( "Export")

    def cancel(self):
        self.ui1 = MainWindow_1()
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def prnt(self):
        text = str(self.comboBox.currentText())
        dob = self.dateEdit.date().toString("d-M-yyyy")
        if u1.admin=="YES":
            p=printdata()
            p.printo(dob,text)
            self.uip = Dialog(12)
            self.uip.show()
        else:
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("SELECT * FROM USERLOG WHERE FLAG='1' AND SHIFT='%s' AND `DATE`='%s'"%(text,dob))
            data = cursor1.fetchall()
            if data==None:
                self.uip = Dialog(13)
                self.uip.show()
            else:
                p=printdata()
                p.printo(dob,text)
                self.uip = Dialog(12)
                self.uip.show()
        self.cancel()

class Printwindow(QtGui.QMainWindow, Ui_Printwindow):

    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class printdata(object):

    def printo(self,date,shift):
        datecheck()
        workbook = xlsxwriter.Workbook('LOG_%s.xlsx'%(p))
        worksheet = workbook.add_worksheet()
        worksheet.set_landscape()
        worksheet.set_paper(9)
        worksheet.fit_to_pages(1,1)
        bold = workbook.add_format({'bold': True})
        merge_format = workbook.add_format({'align': 'center','bold': True})
        merge_format2 = workbook.add_format({'align': 'center','bold': True})
        merge_format.set_bg_color("gray")
        merge_data=workbook.add_format({'align':'indent','valign':'vjustify','bold': True})
        workbook.set_properties({'title':'Shift record','subject': 'Shift tool','author':'Tony Benoy','comments': 'Created with Python and XlsxWriter'})
        if shift=="Evening":
            worksheet.merge_range('A1:D1', 'Evening Duty (14:00 To 21:00 Hrs)', merge_format)
        elif shift=="Morning":
            worksheet.merge_range('A1:D1', 'Morning Duty (7:00 To 14:00 Hrs)', merge_format)
        elif shift=="Night":
            worksheet.merge_range('A1:D1', 'Night Duty (21:00 To 7:00 Hrs)', merge_format)
        worksheet.merge_range('F1:L1', 'DATE:  %s'%(p), merge_format)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT UNAME FROM USERLOG WHERE SHIFT='%s' AND `DATE`='%s' AND FLAG='1'"%(shift,date))
        data=cursor1.fetchall()
        name=[]
        ddd=0
        for row in data:
            if row[0] not in name:
                name.append(row[0])
                ddd+=1
        worksheet.write('A2','SHIFT ENGINEER\'S', merge_format)
        ggg=0
        for l in range(3,ddd+3):
            worksheet.write('A%s'%(l), name[ggg], bold)
            ggg+=1
        worksheet.merge_range('B2:D2', 'ENGINEER\'S SIGNATURE', merge_data)
        worksheet.merge_range('B3:D3', '', merge_data)
        worksheet.merge_range('B4:D4', '', merge_data)
        worksheet.merge_range('B5:D5', '', merge_data)
        a=g=6
        worksheet.set_header('&CDAILY ACTIVITY LOG FOR FOIS DBA SERVER ROOM,CHANAKYAPURI,NEW DELHI -110021')
        worksheet.merge_range('A%s:D%s'%(a,a), 'DAILY ROUTINE TASK', merge_format)
        worksheet.hide_gridlines(0)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT TASK,STATUS FROM DRT WHERE SHIFT = '%s' AND DATE = '%s'"%(shift,date))
        a+=1
        data = cursor1.fetchall()
        worksheet.set_column('A:C', 15)
        worksheet.merge_range('A%s:C%s'%(a,a), "TASK", merge_data)
        worksheet.write('D%s'%(a), 'STATUS', bold)
        a+=1
        for ro in data:
            worksheet.merge_range('A%s:C%s'%(a,a), ro[0], merge_data)
            worksheet.write('D%s'%(a), ro[1])
            a+=1
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT DATA FROM DOS WHERE SHIFT = '%s' AND DATE = '%s'"%(shift,date))
        data = cursor1.fetchall()
        worksheet.merge_range('F2:L2', 'Description of Shift', merge_format)
        tops=""
        for row in data:
            tops=tops+str(row[0])+"\n"
        worksheet.merge_range('F3:L21',tops, merge_data)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT DATA FROM VIFNS WHERE SHIFT = '%s' AND DATE = '%s'"%(shift,date))
        data = cursor1.fetchall()
        worksheet.merge_range('F22:L22', 'Very Important for Next shift', merge_format)
        tops=""
        worksheet.merge_range('E1:E%s'%(a),"",merge_data)
        for row in data:
            tops=tops+str(row[0])+"\n"
        worksheet.merge_range('F23:L32',tops, merge_data)
        a+=1
        worksheet.merge_range('E1:E%s'%(a),"",merge_data)
        for n in xrange(a,34):
            worksheet.merge_range('A%s:D%s'%(n,n), "", merge_data)
        worksheet.set_column('E:E', 2)
        worksheet1 = workbook.add_worksheet()
        worksheet1.set_landscape()
        worksheet1.set_paper(9)
        worksheet1.fit_to_pages(1,1)
        worksheet1.merge_range('A1:D1', 'Evening Duty (14:00 To 21:00 Hrs)', merge_format)
        worksheet1.merge_range('F1:L1', 'DATE:  %s'%(p), merge_format)
        a=2
        worksheet1.merge_range('A%s:D%s'%(a,a), 'HOURLY TASK', merge_format)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT `TIME` FROM project.HOURLY WHERE SHIFT='%s' AND DATE = '%s'"%(shift,date))
        data = cursor1.fetchall()
        lit=[]
        for row in data:
            if row[0] not in lit:
                lit.append(row[0])
        a+=1
        worksheet1.merge_range('A%s:B%s'%(a,a), "TASK", merge_data)
        n=2
        for t in lit:
            worksheet1.write(2,n,t,bold)
            n+=1
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT `TASK` FROM project.HOURLY WHERE SHIFT='%s' AND DATE = '%s'"%(shift,date))
        data = cursor1.fetchall()
        tas=[]
        for row in data:
            if row[0] not in tas:
                tas.append(row[0])
        n=4
        for t in tas:
            worksheet1.merge_range('A%s:B%s'%(n,n), t, merge_data)
            n+=1
        n=3
        for t in tas:
            lo=2
            for l in lit:
                db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
                cursor1 = db1.cursor()
                cursor1.execute("SELECT `STATUS` from project.HOURLY WHERE `DATE`='%s' AND `TASK`='%s' AND `TIME`='%s'"%(date,t,l))
                data =cursor1.fetchall()
                for ro in data:
                    worksheet1.write(n,lo,ro[0])
                    lo+=1
            n+=1
        a=n+2
        n=a
        s=n
        worksheet1.hide_gridlines(0)
        worksheet1.merge_range('A%s:D%s'%(a,a), 'TASK at shift change', merge_format)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT TASK,STATUS FROM TASC WHERE SHIFT = '%s' AND DATE = '%s'"%(shift,date))
        a+=1
        data = cursor1.fetchall()
        worksheet1.set_column('A:C', 15)
        worksheet1.merge_range('A%s:C%s'%(a,a), "TASK", merge_data)
        worksheet1.write('D%s'%(a), 'STATUS', bold)
        a+=1
        for ro in data:
            worksheet1.merge_range('A%s:C%s'%(a,a), ro[0], merge_data)
            worksheet1.write('D%s'%(a), ro[1])
            a+=1
        worksheet1.merge_range('F%s:I%s'%(n,n), 'Shift End Activity', merge_format)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT TASK,STATUS FROM SEA WHERE SHIFT = '%s' AND DATE = '%s'"%(shift,date))
        n+=1
        data = cursor1.fetchall()
        worksheet1.set_column('F:H', 15)
        worksheet1.merge_range('F%s:H%s'%(n,n), "TASK", merge_data)
        worksheet1.write('I%s'%(n), 'STATUS', bold)
        n+=1
        for ro in data:
            worksheet1.merge_range('F%s:H%s'%(n,n), ro[0], merge_data)
            worksheet1.write('I%s'%(n), ro[1])
            n+=1
        n=a+1
        worksheet1.merge_range('F%s:I%s'%(n,n), 'Date Dependent Activity', merge_format)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT TASK,STATUS FROM DDA WHERE SHIFT = '%s' AND DATE = '%s'"%(shift,date))
        n+=1
        data = cursor1.fetchall()
        worksheet1.set_column('A:S', 15)
        worksheet1.merge_range('F%s:H%s'%(n,n), "TASK", merge_data)
        worksheet1.write('I%s'%(n), 'STATUS', bold)
        n+=1
        for ro in data:
            worksheet1.merge_range('F%s:H%s'%(n,n), ro[0], merge_data)
            worksheet1.write('I%s'%(n), ro[1])
            n+=1
        a+=1
        worksheet1.merge_range('A%s:D%s'%(a,a), 'Miscellaneous', merge_format)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT TASK,STATUS FROM MISCDATA WHERE SHIFT = '%s' AND DATE = '%s'"%(shift,date))
        a+=1
        data = cursor1.fetchall()
        worksheet1.merge_range('A%s:C%s'%(a,a), "TASK", merge_data)
        worksheet1.write('D%s'%(a), 'STATUS', bold)
        a+=1
        for ro in data:
            worksheet1.merge_range('A%s:C%s'%(a,a), ro[0], merge_data)
            worksheet1.write('D%s'%(a), ro[1])
            a+=1
        if n>=a:
            a=n
        a+=1
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT `TIME` FROM project.TWOHOUR WHERE SHIFT='%s' AND DATE = '%s'"%(shift,date))
        data = cursor1.fetchall()
        lit=[]
        for row in data:
            if row[0] not in lit:
                lit.append(row[0])
        worksheet1.merge_range('A%s:K%s'%(a,a), 'TASK at every 2 Hours', merge_format)
        a+=1
        worksheet1.merge_range('B%s:I%s'%(a,a), 'CPU',merge_format2)
        n=a+1
        for k in lit:
            worksheet1.write(n,0,k,bold)
            n+=1
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SHOW columns FROM TWOHOUR;")
        data= cursor1.fetchall()
        tas=[]
        for row in data:
            tas.append(row[0])
        n=a
        k=1
        tas.remove("DATE")
        tas.remove("SHIFT")
        tas.remove("TIME")
        for t in tas:
            if t[0:3]=="CPU":
                worksheet1.write(n,k,t[4:len(t)],bold)
                k+=1
        n=a+1
        for l in lit:
            lo=1
            for t in tas:
                if t[0:3]=="CPU":
                    db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
                    cursor1 = db1.cursor()
                    cursor1.execute("SELECT `%s` from TWOHOUR WHERE `DATE`='%s' AND `TIME`='%s' AND SHIFT ='%s'"%(t,date,l,shift))
                    data =cursor1.fetchall()
                    for ro in data:
                        worksheet1.write(n,lo,ro[0])
                        lo+=1
            n+=1
        a=n+2
        worksheet1.merge_range('B%s:E%s'%(a,a), 'LOAD AVERAGE', merge_format2)
        worksheet1.merge_range('F%s:G%s'%(a,a),'MEMORY QUEUE',merge_format2)
        worksheet1.merge_range('H%s:I%s'%(a,a),'DISK QUEUE',merge_format2)
        worksheet1.merge_range('J%s:K%s'%(a,a),'CONNECTED USER',merge_format2)
        n=a+1
        for k in lit:
            worksheet1.write(n,0,k,bold)
            n+=1
        n=a
        k=1
        for t in tas:
            if t[0:7]=="LOADAVG":
                worksheet1.write(n,k,t[8:len(t)],bold)
                k+=1
            elif t[0:4]=="MEMQ":
                worksheet1.write(n,k,t[5:len(t)],bold)
                k+=1
            elif t[0:5]=="DISKQ":
                worksheet1.write(n,k,t[6:len(t)],bold)
                k+=1
            elif t[0:4]=="USER":
                worksheet1.write(n,k,t[5:len(t)],bold)
                k+=1
        n=a+1
        for l in lit:
            lo=1
            for t in tas:
                if t[0:7]=="LOADAVG":
                    db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
                    cursor1 = db1.cursor()

                    cursor1.execute("SELECT `%s` from TWOHOUR WHERE `DATE`='%s' AND `TIME`='%s' AND SHIFT ='%s'"%(t,date,l,shift))
                    data =cursor1.fetchall()
                    for ro in data:
                        worksheet1.write(n,lo,ro[0])
                        lo+=1
                elif t[0:4]=="MEMQ":
                    db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
                    cursor1 = db1.cursor()
                    cursor1.execute("SELECT `%s` from TWOHOUR WHERE `DATE`='%s' AND `TIME`='%s' AND SHIFT ='%s'"%(t,date,l,shift))
                    data =cursor1.fetchall()
                    for ro in data:
                        worksheet1.write(n,lo,ro[0])
                        lo+=1
                elif  t[0:5]=="DISKQ":
                    db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
                    cursor1 = db1.cursor()
                    cursor1.execute("SELECT `%s` from TWOHOUR WHERE `DATE`='%s' AND `TIME`='%s' AND SHIFT ='%s'"%(t,date,l,shift))
                    data =cursor1.fetchall()
                    for ro in data:
                        worksheet1.write(n,lo,ro[0])
                        lo+=1
                elif t[0:4]=="USER":
                    cursor1.execute("SELECT `%s` from TWOHOUR WHERE `DATE`='%s' AND `TIME`='%s' AND SHIFT ='%s'"%(t,date,l,shift))
                    data =cursor1.fetchall()
                    for ro in data:
                        worksheet1.write(n,lo,ro[0])
                        lo+=1
            n+=1
        a=s
        worksheet1.merge_range('K%s:M%s'%(a,a), 'CASE', merge_format)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT CASEID,VENDOR,STATUS FROM project.CASE WHERE DATE = '%s'"%(date))
        r=cursor1.rowcount
        a+=1
        data = cursor1.fetchall()
        worksheet1.write('K%s'%(a), "CASE ID", bold)
        worksheet1.write('L%s'%(a), 'VENDOR', bold)
        worksheet1.write('M%s'%(a), 'STATUS', bold)
        a+=1
        for ro in data:
            worksheet1.write('K%s'%(a), ro[0])
            worksheet1.write('L%s'%(a), ro[1])
            worksheet1.write('M%s'%(a), ro[2])
        workbook.close()

class Ui_EDTASK(object):
    table=None
    shift=None
    dt=None

    def setupUi(self, EDTASK):
        datecheck()
        self.centralwidget = QtGui.QWidget(EDTASK)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(5)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT * FROM %s WHERE SHIFT = '%s' AND DATE = '%s'"%(self.table,self.shift,self.dt))
        r=cursor1.rowcount
        self.tableWidget.setRowCount(r)
        data = cursor1.fetchall()
        if r==0:
            self.uip = Dialog(17)
            self.uip.show()
            self.cancel()
        else:
            n=0
            for ro in data:
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                self.tableWidget.setItem(n, 0, item)
                item = QtGui.QTableWidgetItem()
                item.setText(ro[3])
                self.tableWidget.setItem(n, 1, item)
                item = QtGui.QTableWidgetItem()
                item.setText(ro[2])
                self.tableWidget.setItem(n, 2, item)
                item = QtGui.QTableWidgetItem()
                item.setText(ro[4])
                self.tableWidget.setItem(n, 3, item)
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 4, item)
                item.setText(ro[1])
                if n==r:
                    break
                else:
                    n+=1
            self.tableWidget.setRowCount(r)
            self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        EDTASK.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.cancel)
        self.retranslateUi(EDTASK)
        QtCore.QMetaObject.connectSlotsByName(EDTASK)

    def retranslateUi(self, EDTASK):
        EDTASK.setWindowTitle("Edit Task")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Task")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Date")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Time")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("Shift")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText("Status")
        self.pushButton.setText("Done")
        self.pushButton_2.setText("Cancel")

    def insert(self):
        allRows = self.tableWidget.rowCount()
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("DELETE FROM %s WHERE SHIFT = '%s' AND DATE = '%s'"%(self.table,self.shift,self.dt))
        for row in xrange (0,allRows):
            a = self.tableWidget.item(row,0).text()
            b = self.tableWidget.item(row,1).text()
            g = self.tableWidget.item(row,2).text()
            d = self.tableWidget.item(row,3).text()
            e = self.tableWidget.item(row,4).text()
            cursor1.execute ("INSERT INTO %s (TASK,STATUS,TIME, DATE,SHIFT) VALUES('%s','%s','%s','%s','%s')"%(self.table,a,e,g,b,d))
            db1.commit()
        self.uip = Dialog(11)
        self.uip.show()
        self.cancel

    def cancel(self):
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

class EDTASK(QtGui.QMainWindow, Ui_EDTASK):

    def __init__(self,t,d,p, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.table=t
        self.dt=d
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.shift=p
        self.setupUi(self)

class Ui_edcase(object):
    dt=None

    def setupUi(self, edcase):
        datecheck()
        self.centralwidget = QtGui.QWidget(edcase)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(5)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()

        cursor1.execute("SELECT * FROM project.`CASE` WHERE `DATE`='%s'"%(self.dt))
        r=cursor1.rowcount
        if r==0:
            self.uip = Dialog(18)
            self.uip.show()
            self.cancel()
        else:
            self.tableWidget.setRowCount(r)
            data = cursor1.fetchall()
            n=0
            for ro in data:
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                self.tableWidget.setItem(n, 0, item)
                item = QtGui.QTableWidgetItem()
                item.setText(ro[1])
                self.tableWidget.setItem(n, 1, item)
                item = QtGui.QTableWidgetItem()
                item.setText(ro[2])
                self.tableWidget.setItem(n, 2, item)
                item = QtGui.QTableWidgetItem()
                item.setText(ro[4])
                self.tableWidget.setItem(n, 3, item)
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 4, item)
                item.setText(ro[3])
                if n==r:
                    break
                else:
                    n+=1
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(2, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(3, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(4, item)
            self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
            self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
            self.pushButton = QtGui.QPushButton(self.centralwidget)
            self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
            self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
            self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
            spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
            edcase.setCentralWidget(self.centralwidget)
            self.pushButton.clicked.connect(self.insert)
            self.pushButton_2.clicked.connect(self.cancel)
        self.retranslateUi(edcase)
        QtCore.QMetaObject.connectSlotsByName(edcase)

    def retranslateUi(self, edcase):
        edcase.setWindowTitle("Edit Case")
        self.pushButton.setText("Modify")
        self.pushButton_2.setText("Cancel")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Case Id")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Vendor")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Status")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("Time")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText("Date")

    def insert(self):
        allRows = self.tableWidget.rowCount()
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("DELETE FROM project.`CASE` WHERE `DATE` = '%s'"%(self.dt))
        for row in xrange (0,allRows):
            a = self.tableWidget.item(row,0).text()
            b = self.tableWidget.item(row,1).text()
            g = self.tableWidget.item(row,2).text()
            d = self.tableWidget.item(row,3).text()
            e = self.tableWidget.item(row,4).text()
            cursor1.execute ("INSERT INTO project.`CASE` ( CASEID, VENDOR, STATUS, `DATE`, `TIME`)VALUES('%s', '%s', '%s', '%s', '%s')"%(a,b,g,e,d))
        db1.commit()
        self.uip = Dialog(11)
        self.uip.show()

    def cancel(self):
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

class edcase(QtGui.QMainWindow, Ui_edcase):

    def __init__(self,p, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.dt=p
        self.setupUi(self)

class Ui_VIEWTASK(object):

    def setupUi(self, VIEWTASK):
        datecheck()
        self.centralwidget = QtGui.QWidget(VIEWTASK)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.gridLayout.addWidget(self.comboBox_2, 5, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 7, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.gridLayout.addWidget(self.dateEdit, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 7, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        VIEWTASK.setCentralWidget(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("Morning")
        self.comboBox.addItem("Evening")
        self.comboBox.addItem("Night")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat( "d/M/yyyy")
        self.dateEdit.setDate(datetime.datetime.strptime(p, "%d-%m-%Y"))
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("Task At Shift Change")
        self.comboBox_2.addItem("Daily Routine Task")
        self.comboBox_2.addItem("Date Dependent Activity")
        self.comboBox_2.addItem("HOURLY Task")
        self.comboBox_2.addItem("Two Hourly Task")
        self.comboBox_2.addItem("Shift End Activity")
        self.comboBox_2.addItem("MISC")
        self.comboBox_2.addItem("Case")
        self.pushButton.clicked.connect(self.get)
        self.pushButton_2.clicked.connect(self.cancel)
        self.retranslateUi(VIEWTASK)
        QtCore.QMetaObject.connectSlotsByName(VIEWTASK)

    def retranslateUi(self, VIEWTASK):
        VIEWTASK.setWindowTitle( "View Task")
        self.pushButton_2.setText( "Cancel")
        self.label_2.setText( "Date")
        self.label.setText( "Shift")
        self.label_3.setText( "TASK")
        self.pushButton.setText( "View")

    def get(self):
        text = str(self.comboBox.currentText())
        text2 = str(self.comboBox_2.currentText())
        dob = self.dateEdit.date().toString("d-M-yyyy")
        if text2=="Two Hourly Task":
            self.ui1 = TVIEW(dob,text)
            self.ui1.setupUi(MainWindow)
        elif text2=="Case":
            self.ui1 = edcase(dob)
            self.ui1.setupUi(MainWindow)
            MainWindow.show()
        else:
            if text2=="Task At Shift Change":
                text2="TASC"
            elif text2=="Daily Routine Task":
                text2="DRT"
            elif text2=="Shift End Activity":
                text2="SEA"
            elif text2=="Date Dependent Activity":
                text2="DDA"
            elif text2=="MISC":
                text2="MISCDATA"
            elif text2=="Hourly Task":
                text2="HOURLY"
            self.ui1 = EDTASK(text2,dob,text)
            self.ui1.setupUi(MainWindow)
            MainWindow.show()

    def cancel(self):
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

class VIEWTASK(QtGui.QMainWindow, Ui_VIEWTASK):

    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_Text(object):
    tab=None

    def setupUi(self, Text):
        datecheck()
        self.centralwidget = QtGui.QWidget(Text)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(1)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT DATA FROM %s WHERE DATE='%s' AND SHIFT='%s'"%(self.tab,p,u1.shift))
        r=cursor1.rowcount
        self.tableWidget.setRowCount(r+1)
        n=0
        if r==0:
            self.tableWidget.insertRow(0)
        else:
            data = cursor1.fetchall()
            for ro in data:
                if ro[0]==None:
                    continue
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                self.tableWidget.setItem(n, 0, item)
                if n==r:
                    break
                else:
                    n+=1
        self.tableWidget.insertRow(n)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(1500)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        Text.setCentralWidget(self.centralwidget)
        self.retranslateUi(Text)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.cancel)
        QtCore.QMetaObject.connectSlotsByName(Text)

    def retranslateUi(self, Text):
            if self.tab=="DOS":
                Text.setWindowTitle("Description of Shift")
            elif self.tab=="VIFNS":
                Text.setWindowTitle("Very Important for Next shift")
            self.pushButton.setText("Done")
            self.pushButton_2.setText("Cancel")
            self.label.setText("Enter Data")
            item = self.tableWidget.verticalHeaderItem(0)
            item.setText("1")
            item = self.tableWidget.horizontalHeaderItem(0)
            if self.tab=="DOS":
                item.setText("Description of Shift")
            elif self.tab=="VIFNS":
                item.setText("Very Important For Next Shift")

    def insert(self):
            allRows = self.tableWidget.rowCount()
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("DELETE FROM %s WHERE DATE='%s' AND SHIFT='%s'"%(self.tab,p,u1.shift))
            for row in xrange (0,allRows):
                if self.tableWidget.item(row,0)!=None:
                    a = self.tableWidget.item(row,0).text()
                    cursor1.execute ("INSERT INTO %s (`DATA`, `DATE`, `TIME`, SHIFT)VALUES('%s', '%s', '%s', '%s')"%(self.tab,a,p,t,u1.shift))
            self.tableWidget.insertRow(allRows+1)
            db1.commit()
            self.uip = Dialog(6)
            self.uip.show()
            self.cancel()

    def cancel(self):
            self.ui = Ui_Shift()
            self.ui.setupUi(MainWindow)
            MainWindow.show()
            self.close()

class Text(QtGui.QMainWindow, Ui_Text):

    def __init__(self,p, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.tab=p
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_Task(object):
    table=None

    def setupUi(self, Task):
        datecheck()
        self.centralwidget = QtGui.QWidget(Task)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(2)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        if self.table=="SEA" or self.table=="TASC":
            cursor1.execute("SELECT %s FROM TASK WHERE %s IS NOT NULL"%(self.table,self.table))
            r=cursor1.rowcount
            if r==0:
                self.uip = Dialog(15)
                self.uip.show()
                self.cancel()
            self.tableWidget.setRowCount(r)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, item)
            data = cursor1.fetchall()
            n=0
            for ro in data:
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                item.setFlags(flags)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.tableWidget.setItem(n, 0, item)
                item = QtGui.QTableWidgetItem()
                db2=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
                cursor2 = db2.cursor()
                cursor2.execute("SELECT STATUS FROM %s WHERE TASK='%s' AND DATE='%s' AND SHIFT='%s' "%(self.table,ro[0],p,u1.shift))
                data2 = cursor2.fetchall()
                if data2!=None:
                    for roww in data2:
                        item.setText(roww[0])
                self.tableWidget.setItem(n, 1, item)
                if n==r:
                    break
                else:
                    n+=1

        elif self.table=="DRT":
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("SELECT %s FROM project.DAILY WHERE %s IS NOT NULL"%(u1.shift,u1.shift))
            r=cursor1.rowcount
            if r==0:
                self.uip = Dialog(15)
                self.uip.show()
                self.cancel()
            self.tableWidget.setRowCount(r)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, item)
            data = cursor1.fetchall()
            for k in range (0,r):
                item = QtGui.QTableWidgetItem()
                item.setText("")
                self.tableWidget.setItem(k, 1, item)
            n=0
            for ro in data:
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                item.setFlags(flags)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.tableWidget.setItem(n, 0, item)
                db2=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
                cursor2 = db2.cursor()
                cursor2.execute("SELECT STATUS FROM %s WHERE TASK='%s' AND DATE='%s' AND SHIFT='%s' "%(self.table,ro[0],p,u1.shift))
                data2 = cursor2.fetchall()
                item = QtGui.QTableWidgetItem()
                if data2!=None:
                    for roww in data2:
                        item.setText(roww[0])
                    self.tableWidget.setItem(n, 1, item)
                if n==r:
                    break
                else:
                    n+=1
        elif self.table=="DDA":
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("SELECT `%s` FROM project.DATEDEPENDENT WHERE `%s` IS NOT NULL"%(str(now.day),str(now.day)))
            r=cursor1.rowcount
            if r==0:
                self.uip = Dialog(15)
                self.uip.show()
                self.cancel()
            self.tableWidget.setRowCount(r)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, item)
            data = cursor1.fetchall()
            for k in range (0,r):
                item = QtGui.QTableWidgetItem()
                item.setText("")
                self.tableWidget.setItem(k, 1, item)
            n=0
            for ro in data:
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                item.setFlags(flags)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.tableWidget.setItem(n, 0, item)
                item = QtGui.QTableWidgetItem()
                item.setText(p)
                item.setFlags(flags)
                self.tableWidget.setItem(n, 1, item)
                item = QtGui.QTableWidgetItem()
                db2=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
                cursor2 = db2.cursor()
                cursor2.execute("SELECT STATUS FROM %s WHERE TASK='%s' AND DATE='%s' AND SHIFT='%s' "%(self.table,ro[0],p,u1.shift))
                data2 = cursor2.fetchall()
                if data2!=None:
                    for roww in data2:
                        item = QtGui.QTableWidgetItem()
                        item.setText(roww[0])
                        self.tableWidget.setItem(n, 1, item)
                if n==r:
                    break
                else:
                    n+=1
        elif self.table=="MONTHLY" or self.table=="FORTNIGHTLY":
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("SELECT %s FROM project.MISC WHERE %s IS NOT NULL"%(self.table,self.table))
            r=cursor1.rowcount
            if r==0:
                self.uip = Dialog(15)
                self.uip.show()
                self.cancel()
            self.tableWidget.setRowCount(r)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, item)
            for k in range (0,r):
                item = QtGui.QTableWidgetItem()
                item.setText("")
                self.tableWidget.setItem(k, 1, item)
            data = cursor1.fetchall()
            n=0
            for ro in data:
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                item.setFlags(flags)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.tableWidget.setItem(n, 0, item)
                db2=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
                cursor2 = db2.cursor()
                cursor2.execute("SELECT STATUS FROM project.MISCDATA WHERE TASK='%s' AND DATE='%s' AND SHIFT='%s' "%(ro[0],p,u1.shift))
                data2 = cursor2.fetchall()
                if data2!=None:
                    for roww in data2:
                        item = QtGui.QTableWidgetItem()
                        item.setText(roww[0])
                        self.tableWidget.setItem(n, 1, item)
                if n==r:
                    break
                else:
                    n+=1
        elif self.table=="DAY":
            if self.table=="DAY":
                if da==0:
                    dayy="MONDAY"
                elif da==1:
                    dayy="TUESDAY"
                elif da==2:
                    dayy="WEDNESDAY"
                elif da==3:
                    dayy="THURSDAY"
                elif da==4:
                    dayy="FRIDAY"
                elif da==5:
                    dayy="SATURDAY"
                elif da==6:
                    dayy="SUNDAY"
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("SELECT %s FROM project.MISC WHERE %s IS NOT NULL"%(dayy,dayy))
            r=cursor1.rowcount
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, item)
            if r==0:
                self.uip = Dialog(15)
                self.uip.show()
                self.cancel()
            self.tableWidget.setRowCount(r)
            data = cursor1.fetchall()
            n=0
            for k in range (0,r):
                item = QtGui.QTableWidgetItem()
                item.setText("")
                self.tableWidget.setItem(k, 1, item)
            for ro in data:
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                item.setFlags(flags)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.tableWidget.setItem(n, 0, item)
                db2=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
                cursor2 = db2.cursor()
                cursor2.execute("SELECT STATUS FROM project.MISCDATA WHERE TASK='%s' AND DATE='%s' AND SHIFT='%s' "%(ro[0],p,u1.shift))
                data2 = cursor2.fetchall()
                if data2!=None:
                    for roww in data2:
                        item = QtGui.QTableWidgetItem()
                        item.setText(roww[0])
                        self.tableWidget.setItem(n, 1, item)
                if n==r:
                    break
                else:
                    n+=1
        self.tableWidget.horizontalHeader().setDefaultSectionSize(600)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        Task.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.cancel)
        self.retranslateUi(Task)
        QtCore.QMetaObject.connectSlotsByName(Task)

    def cancel(self):
        self.ui = Ui_Shift()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def insert(self):
        ss=6
        allRows = self.tableWidget.rowCount()
        if self.table=="DAY" or self.table=="MONTHLY" or self.table=="FORTNIGHTLY":
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("DELETE FROM project.MISCDATA WHERE DATE='%s' AND SHIFT='%s'"%(p,u1.shift))
            for row in xrange (0,allRows):
                a = self.tableWidget.item(row,0).text()
                e = self.tableWidget.item(row,1).text()
                cursor1.execute ("INSERT INTO project.MISCDATA (TASK,STATUS,TIME, DATE,SHIFT) VALUES('%s','%s','%s','%s','%s')"%(a,e,t,p,u1.shift))
        else:
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("DELETE FROM %s WHERE DATE='%s' AND SHIFT='%s'"%(self.table,p,u1.shift))
            for row in xrange (0,allRows):
                a = self.tableWidget.item(row,0).text()
                e = self.tableWidget.item(row,1).text()
                if self.table=="DDA" or self.table=="TASC" or self.table=="DRT":
                    if e=="":
                        e=""
                    elif e[0]=="Y" or e[0]=="y":
                        e="YES"
                    elif e[0]=="N" or e[0]=="n":
                        e="NO"
                    else:
                        ss=8
                        e=""
                elif self.table=="SEA":
                        if e=="":
                            e=""
                        elif e[0]=="O" or e[0]=="o":
                            e="OK"
                        elif e[0]=="P" or e[0]=="p":
                            e="PROBLEM"
                        else:
                            ss=8
                            e=""
                cursor1.execute ("INSERT INTO %s (TASK,STATUS,TIME, DATE,SHIFT) VALUES('%s','%s','%s','%s','%s')"%(self.table,a,e,t,p,u1.shift))
        db1.commit()
        self.uip = Dialog(ss)
        self.uip.show()
        self.cancel()


    def retranslateUi(self, Task):
        if self.table=="DRT":
            Task.setWindowTitle("Daily Routine Task")
        elif self.table=="MONTHLY":
            Task.setWindowTitle( "Monthly")
        elif self.table=="FORTNIGHTLY":
            Task.setWindowTitle("Fortnightly")
        elif self.table=="DAY":
            Task.setWindowTitle("Day Dependant Task")
        elif self.table=="DDA":
            Task.setWindowTitle("Date Dependent Activity")
        elif self.table=="SEA":
            Task.setWindowTitle("Shift End Activity")
        elif self.table=="TASC":
            Task.setWindowTitle("Task at Shift Change")
        elif self.table=="DDA":
            Task.setWindowTitle( "Date Dependent Activity")
        self.pushButton_2.setText( "Cancel")
        self.pushButton.setText( "Done")
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText( "1")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText( "Task")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText( "Status")

class Task(QtGui.QMainWindow, Ui_Task):

    def __init__(self,t, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.table=t
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_MISC(object):

    def setupUi(self, MISC):
        datecheck()
        self.centralwidget = QtGui.QWidget(MISC)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_4, 3, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        MISC.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.day)
        self.pushButton_2.clicked.connect(self.monthly)
        self.pushButton_3.clicked.connect(self.fortnightly)
        self.pushButton_4.clicked.connect(self.cancel)
        self.retranslateUi(MISC)
        QtCore.QMetaObject.connectSlotsByName(MISC)

    def retranslateUi(self, MISC):
        MISC.setWindowTitle( "Miscellaneous")
        self.pushButton_3.setText( "Fortnightly")
        self.pushButton_4.setText( "Cancel")
        self.pushButton.setText( "Day")
        self.pushButton_2.setText( "Monthly")

    def  day(self):
        self.ui1 = Task("DAY")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def monthly(self):
        self.ui1 = Task("MONTHLY")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def fortnightly(self):
        self.ui1 = Task("FORTNIGHTLY")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def cancel(self):
        self.ui = Ui_Shift()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

class MISC(QtGui.QMainWindow, Ui_MISC):

    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_CASE(object):

    def setupUi(self, CASE):
        datecheck()
        self.centralwidget = QtGui.QWidget(CASE)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT CASEID, VENDOR, STATUS FROM project.`CASE` WHERE `DATE`='%s' and SHIFT='%s'"%(p,u1.shift))
        r=cursor1.rowcount
        if r==0:
            self.tableWidget.setRowCount(1)
        else:
            self.tableWidget.setRowCount(r+1)
        data = cursor1.fetchall()
        n=0
        for ro in data:
            item = QtGui.QTableWidgetItem()
            item.setText(ro[0])
            self.tableWidget.setItem(n, 0, item)
            item = QtGui.QTableWidgetItem()
            item.setText(ro[1])
            self.tableWidget.setItem(n, 1, item)
            item = QtGui.QTableWidgetItem()
            item.setText(ro[2])
            self.tableWidget.setItem(n, 2, item)
            if n==r:
                break
            else:
                n+=1
        self.tableWidget.insertRow(r+1)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(450)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
        CASE.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.cancel)
        self.retranslateUi(CASE)
        QtCore.QMetaObject.connectSlotsByName(CASE)

    def insert(self):
        allRows=self.tableWidget.rowCount()
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("DELETE FROM project.`CASE` WHERE `DATE`='%s' AND SHIFT='%s'"%(p,u1.shift))
        for row in xrange (0,allRows):
            if self.tableWidget.item(row,0)!=None and self.tableWidget.item(row,1)!=None and self.tableWidget.item(row,2)!=None:
                a = self.tableWidget.item(row,0).text()
                b= self.tableWidget.item(row,1).text()
                c= self.tableWidget.item(row,2).text()
                if c[0]=="O" or c[0]=="o":
                    c="Open"
                elif c[0]=="u" or c[0]=="U":
                    c="Updated"
                elif c[0]=="C" or c[0]=="c":
                    c="Closed"
                else:
                    self.uip = Dialog(8)
                    self.uip.show()
                    self.cancel()
                cursor1.execute ("INSERT INTO project.`CASE`(CASEID, VENDOR, STATUS, `DATE`, `TIME`,SHIFT)VALUES('%s', '%s', '%s', '%s', '%s','%s');"%(a,b,c,p,t,u1.shift))
        db1.commit()
        self.uip = Dialog(6)
        self.uip.show()
        self.cancel()

    def cancel(self):
        self.ui = Ui_Shift()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def retranslateUi(self, CASE):
        CASE.setWindowTitle("Case")
        self.pushButton.setText("Insert")
        self.pushButton_2.setText("Cancel")
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText("1")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Case Id")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Vendor")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Status")

class CASE(QtGui.QMainWindow, Ui_CASE):

    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_Shift(object):

    def setupUi(self, Shift):
        datecheck()
        self.centralwidget = QtGui.QWidget(Shift)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT UNAME FROM USERLOG WHERE `DATE`='%s' AND SHIFT='%s' AND FLAG='1'"%(p,u1.shift))
        data = cursor1.fetchall()
        lit=[]
        k=0
        for row in data:
            if row[0] not in lit:
                lit.append(row[0])
                k+=1
        if k==0:
            self.label_3.setText( "")
            self.label_2.setText( "")
            self.label.setText( "")
        elif k==1:
            self.label_3.setText(lit[0])
        elif k==2:
            self.label_3.setText(lit[0])
            self.label_2.setText(lit[1])
        elif k>=3:
            self.label_3.setText(lit[0])
            self.label_2.setText(lit[1])
            self.label.setText(lit[2])
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 2, 1, 1)
        Shift.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Shift)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuTask = QtGui.QMenu(self.menubar)
        self.menuDescription = QtGui.QMenu(self.menubar)
        Shift.setMenuBar(self.menubar)
        self.actionQuit = QtGui.QAction(Shift)
        self.actionDaily_Routine_Task = QtGui.QAction(Shift)
        self.actionTask_At_Shift_Change = QtGui.QAction(Shift)
        self.actionDate_Dependant_Activity = QtGui.QAction(Shift)
        self.actionShift_End_Activity = QtGui.QAction(Shift)
        self.actionDescription_of_Shift = QtGui.QAction(Shift)
        self.actionVery_Important_For_Next_Shift = QtGui.QAction(Shift)
        self.actionCase = QtGui.QAction(Shift)
        self.actionTaks_every_two_hours = QtGui.QAction(Shift)
        self.actionHourly_Task = QtGui.QAction(Shift)
        self.actionMisc = QtGui.QAction(Shift)
        self.actionChange_Password = QtGui.QAction(Shift)
        self.actionLogout = QtGui.QAction(Shift)
        self.menuFile.addAction(self.actionChange_Password)
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionQuit)
        self.menuTask.addAction(self.actionDaily_Routine_Task)
        self.menuTask.addAction(self.actionTask_At_Shift_Change)
        self.menuTask.addAction(self.actionDate_Dependant_Activity)
        self.menuTask.addAction(self.actionShift_End_Activity)
        self.menuTask.addAction(self.actionCase)
        self.menuTask.addAction(self.actionTaks_every_two_hours)
        self.menuTask.addAction(self.actionHourly_Task)
        self.menuTask.addAction(self.actionMisc)
        self.menuDescription.addAction(self.actionDescription_of_Shift)
        self.menuDescription.addAction(self.actionVery_Important_For_Next_Shift)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTask.menuAction())
        self.menubar.addAction(self.menuDescription.menuAction())
        self.menuTask.addAction(self.actionMisc)
        self.actionDaily_Routine_Task.triggered.connect(self.drt)
        self.actionTask_At_Shift_Change.triggered.connect(self.tasc)
        self.actionDate_Dependant_Activity.triggered.connect(self.dda)
        self.actionShift_End_Activity.triggered.connect(self.sea)
        self.actionHourly_Task.triggered.connect(self.hr)
        self.actionMisc.triggered.connect(self.misc)
        self.actionDescription_of_Shift.triggered.connect(self.dos)
        self.actionVery_Important_For_Next_Shift.triggered.connect(self.vf)
        self.pushButton.clicked.connect(self.cancel)
        self.actionCase.triggered.connect(self.cas)
        self.actionTaks_every_two_hours.triggered.connect(self.two)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.actionLogout.triggered.connect(self.logout)
        self.actionChange_Password.triggered.connect(self.passw)
        self.retranslateUi(Shift)
        QtCore.QMetaObject.connectSlotsByName(Shift)

    def retranslateUi(self, Shift):
        Shift.setWindowTitle( "MainWindow")
        self.pushButton.setText( "Cancel")
        self.menuFile.setTitle( "File")
        self.menuTask.setTitle( "Task")
        self.menuDescription.setTitle( "Description")
        self.actionQuit.setText( "Quit")
        self.actionDaily_Routine_Task.setText( "Daily Routine Task")
        self.actionTask_At_Shift_Change.setText( "Task At Shift Change")
        self.actionDate_Dependant_Activity.setText( "Date Dependant Activity")
        self.actionShift_End_Activity.setText( "Shift End Activity")
        self.actionDescription_of_Shift.setText( "Description of Shift")
        self.actionVery_Important_For_Next_Shift.setText( "Very Important For Next Shift")
        self.actionCase.setText( "Case")
        self.actionTaks_every_two_hours.setText( "Taks every two hours")
        self.actionHourly_Task.setText( "Hourly Task")
        self.actionMisc.setText( "Misc")
        self.actionChange_Password.setText( "Change Password")
        self.actionLogout.setText( "Logout")

    def logout(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def passw(self):
        self.u11=PASSWORD()
        self.u11.show()

    def misc(self):
        self.ui1 = MISC()
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def cas(self):
        self.ui1 = CASE()
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def two(self):
        self.ui1 = TWOHOUR(u1.shift)
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def hr(self):
        self.ui1 = HOURLY(u1.shift)
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def cancel(self):
        self.ui = Ui_MainWindow_1()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def dos(self):
        self.ui1 = Text("DOS")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def vf(self):
        self.ui1 = Text("VIFNS")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def drt(self):
        self.ui1 = Task("DRT")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def dda(self):
        table='DDA'
        self.ui1 = Task(table)
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def tasc(self):
        table='TASC'
        self.ui1 = Task(table)
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def sea(self):
        table='SEA'
        self.ui1 = Task(table)
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

class Shift(QtGui.QMainWindow, Ui_Shift):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_PASSWORD(object):

    def setupUi(self, PASSWORD):
        PASSWORD.resize(320, 240)
        self.pushButton = QtGui.QPushButton(PASSWORD)
        self.pushButton.setGeometry(QtCore.QRect(30, 200, 85, 28))
        self.pushButton_2 = QtGui.QPushButton(PASSWORD)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 200, 85, 28))
        self.label = QtGui.QLabel(PASSWORD)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 20))
        self.lineEdit = QtGui.QLineEdit(PASSWORD)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 141, 28))
        self.label_2 = QtGui.QLabel(PASSWORD)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 111, 20))
        self.lineEdit_2 = QtGui.QLineEdit(PASSWORD)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit .setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 130, 151, 28))
        self.toolButton = QtGui.QToolButton(PASSWORD)
        self.toolButton.setGeometry(QtCore.QRect(210, 90, 51, 27))
        self.pushButton.clicked.connect(self.passchange)
        self.pushButton_2.clicked.connect(self.close)
        self.toolButton.pressed.connect(self.pas)
        self.toolButton.released.connect(self.ps)
        self.retranslateUi(PASSWORD)
        QtCore.QMetaObject.connectSlotsByName(PASSWORD)

    def passchange(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        db2=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor2 = db2.cursor()
        cursor2.execute("SELECT PASSWORD FROM project.USER WHERE USERNAME='%s'"%(u1.username))
        data1=cursor2.fetchall()
        for row in data1:
            if row[0]==a:
                    cursor2.execute("UPDATE project.USER SET PASSWORD='%s'WHERE USERNAME='%s'" % (b,u1.username))
                    self.uip = Dialog(14)
                    self.uip.show()
            else:
                self.uip = Dialog(2)
                self.uip.show()
                self.close()
        db2.commit()
        self.close()

    def pas(self):
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Normal)

    def ps(self):
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Password)

    def retranslateUi(self, PASSWORD):
        PASSWORD.setWindowTitle("Password Change")
        self.pushButton.setText("Change ")
        self.pushButton_2.setText("Cancel")
        self.label.setText("Current password")
        self.label_2.setText("New Password")
        self.toolButton.setText("Show")

class PASSWORD(QtGui.QDialog, Ui_PASSWORD):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)
        self.setupUi(self)

class Ui_HOURLY(object):
    shift=None

    def setupUi(self, HOURLY):
        datecheck()
        self.centralwidget = QtGui.QWidget(HOURLY)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        if self.shift=="Evening":
            self.tableWidget.setRowCount(3)
            for n in range(0,3):
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(n, item)
                self.tableWidget.setColumnCount(9)
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(0, item)
                for n in range(1,9):
                    item = QtGui.QTableWidgetItem()
                    item.setText("")
                    self.tableWidget.setHorizontalHeaderItem(n, item)
            for k in range (0,3):
                for t in range(1,9):
                    item = QtGui.QTableWidgetItem()
                    item.setText("")
                    self.tableWidget.setItem(k, t, item)
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("SELECT STATUS FROM project.HOURLY WHERE SHIFT = '%s' AND DATE = '%s'"%(u1.shift,p))
            data = cursor1.fetchall()
            r=cursor1.rowcount
            if r!=0:
                st=[]
                for row in data:
                    st.append(row[0])
                pa=0
                for k in range (0,3):
                    for t in range(1,9):
                        item = QtGui.QTableWidgetItem()
                        item.setText(st[pa])
                        pa+=1
                        self.tableWidget.setItem(k, t, item)
        elif self.shift=="Morning":
            self.tableWidget.setRowCount(3)
            for n in range(0,3):
                item = QtGui.QTableWidgetItem()
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.tableWidget.setVerticalHeaderItem(n, item)
                self.tableWidget.setColumnCount(8)
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(0, item)
                for n in range(1,8):
                    item = QtGui.QTableWidgetItem()
                    item.setText("")
                    self.tableWidget.setHorizontalHeaderItem(n, item)
            for k in range (0,3):
                for t in range(1,8):
                    item = QtGui.QTableWidgetItem()
                    item.setText("")
                    self.tableWidget.setItem(k, t, item)
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("SELECT STATUS FROM project.HOURLY WHERE SHIFT = '%s' AND DATE = '%s'"%(u1.shift,p))
            r=cursor1.rowcount
            data = cursor1.fetchall()
            if r!=0:
                st=[]
                for row in data:
                    st.append(row[0])
                pa=0
                for k in range (0,3):
                    for t in range(1,8):
                        item = QtGui.QTableWidgetItem()
                        item.setText(st[pa])
                        pa+=1
                        self.tableWidget.setItem(k, t, item)
        elif self.shift=="Night":
            self.tableWidget.setRowCount(2)
            for n in range(0,2):
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(n, item)
                self.tableWidget.setColumnCount(12)
                for n in range(1,12):
                    item = QtGui.QTableWidgetItem()
                    item.setText("")
                    self.tableWidget.setHorizontalHeaderItem(n, item)
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(0, item)
            for k in range (0,2):
                for t in range(1,12):
                    item = QtGui.QTableWidgetItem()
                    item.setText("")
                    self.tableWidget.setItem(k, t, item)
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()

            cursor1.execute("SELECT STATUS FROM project.HOURLY WHERE SHIFT = '%s' AND DATE = '%s'"%(u1.shift,p))
            r=cursor1.rowcount
            data = cursor1.fetchall()
            if r!=0:
                st=[]
                for row in data:
                    st.append(row[0])
                pa=0
                for k in range (0,3):
                    for t in range(1,12):
                        item = QtGui.QTableWidgetItem()
                        item.setText(st[pa])
                        pa+=1
                        self.tableWidget.setItem(k, t, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        HOURLY.setCentralWidget(self.centralwidget)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.cancel)
        self.retranslateUi(HOURLY)
        QtCore.QMetaObject.connectSlotsByName(HOURLY)

    def retranslateUi(self, HOURLY):
        HOURLY.setWindowTitle("Hourly Task")
        if self.shift=="Evening":
            item = self.tableWidget.horizontalHeaderItem(1)
            item.setText("14:00")
            item = self.tableWidget.horizontalHeaderItem(2)
            item.setText("15:00")
            item = self.tableWidget.horizontalHeaderItem(3)
            item.setText("16:00")
            item = self.tableWidget.horizontalHeaderItem(4)
            item.setText("17:00")
            item = self.tableWidget.horizontalHeaderItem(5)
            item.setText("18:00")
            item = self.tableWidget.horizontalHeaderItem(6)
            item.setText("19:00")
            item = self.tableWidget.horizontalHeaderItem(7)
            item.setText("20:00")
            item = self.tableWidget.horizontalHeaderItem(8)
            item.setText("21:00")
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("SELECT %s FROM project.HOURLYTASK WHERE %s IS NOT NULL"%(self.shift,self.shift))
            r=cursor1.rowcount
            if r==0:
                self.uip = Dialog(15)
                self.uip.show()
                self.cancel()
            self.tableWidget.setRowCount(r)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            data = cursor1.fetchall()
            n=0
            for ro in data:
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                item.setFlags(flags)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.tableWidget.setItem(n, 0, item)
                if n==r:
                    break
                else:
                    n+=1
        elif self.shift=="Morning":
            item = self.tableWidget.horizontalHeaderItem(1)
            item.setText("7:00")
            item = self.tableWidget.horizontalHeaderItem(2)
            item.setText("8:00")
            item = self.tableWidget.horizontalHeaderItem(3)
            item.setText("9:00")
            item = self.tableWidget.horizontalHeaderItem(4)
            item.setText("10:00")
            item = self.tableWidget.horizontalHeaderItem(5)
            item.setText("11:00")
            item = self.tableWidget.horizontalHeaderItem(6)
            item.setText("12:00")
            item = self.tableWidget.horizontalHeaderItem(7)
            item.setText("13:00")
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("SELECT %s FROM project.HOURLYTASK WHERE %s IS NOT NULL"%(self.shift,self.shift))
            r=cursor1.rowcount
            if r==0:
                self.uip = Dialog(15)
                self.uip.show()
                self.cancel()
            self.tableWidget.setRowCount(r)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            data = cursor1.fetchall()
            n=0
            for ro in data:
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                item.setFlags(flags)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.tableWidget.setItem(n, 0, item)
                if n==r:
                    break
                else:
                    n+=1
        elif self.shift=="Night":
            item = self.tableWidget.horizontalHeaderItem(1)
            item.setText("21:00")
            item = self.tableWidget.horizontalHeaderItem(2)
            item.setText("22:00")
            item = self.tableWidget.horizontalHeaderItem(3)
            item.setText("23:00")
            item = self.tableWidget.horizontalHeaderItem(4)
            item.setText("00:00")
            item = self.tableWidget.horizontalHeaderItem(5)
            item.setText("1:00")
            item = self.tableWidget.horizontalHeaderItem(6)
            item.setText("2:00")
            item = self.tableWidget.horizontalHeaderItem(7)
            item.setText("3:00")
            item = self.tableWidget.horizontalHeaderItem(8)
            item.setText("4:00")
            item = self.tableWidget.horizontalHeaderItem(9)
            item.setText("5:00")
            item = self.tableWidget.horizontalHeaderItem(10)
            item.setText("6:00")
            item = self.tableWidget.horizontalHeaderItem(11)
            item.setText("7:00")
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("SELECT %s FROM project.HOURLYTASK WHERE %s IS NOT NULL"%(self.shift,self.shift))
            r=cursor1.rowcount
            if r==0:
                self.uip = Dialog(15)
                self.uip.show()
                self.cancel()
            self.tableWidget.setRowCount(r)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            data = cursor1.fetchall()
            n=0
            for ro in data:
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                item.setFlags(flags)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.tableWidget.setItem(n, 0, item)
                if n==r:
                    break
                else:
                    n+=1
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Task")
        self.pushButton.setText("Insert")
        self.pushButton_2.setText("Cancel")

    def insert(self):
        ss=6
        allRows = self.tableWidget.rowCount()
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("DELETE FROM project.HOURLY WHERE `DATE`='%s' AND SHIFT='%s'"%(p,u1.shift))
        for row in xrange (0,allRows):
            a = self.tableWidget.item(row,0).text()
            k=self.tableWidget.columnCount()
            for col in xrange(1,k):
                b = self.tableWidget.horizontalHeaderItem(col).text()
                c = self.tableWidget.item(row,col).text()
                if c=="":
                    c=""
                elif c[0]=="Y" or c[0]=="y":
                    c="YES"
                elif c[0]=="N" or c[0]=="n":
                    c="NO"
                elif c[0]=="O" or c[0]=="o":
                    c="OK"
                elif c[0]=="C" or c[0]=="c":
                    c="CLOSE"
                else:
                    ss=8
                    c=""
                cursor1.execute ("INSERT INTO project.HOURLY(TASK, `TIME`, `DATE`, SHIFT, STATUS)VALUES('%s', '%s', '%s', '%s', '%s')"%(a,b,p,self.shift,c))
        db1.commit()
        self.uip = Dialog(ss)
        self.uip.show()
        self.cancel()

    def cancel(self):
        self.ui = Ui_Shift()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

class HOURLY(QtGui.QMainWindow, Ui_HOURLY):

    def __init__(self, l,parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.shift=l
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_TWOHOUR(object):
    shift=None

    def setupUi(self, TWOHOUR):
        datecheck()
        self.centralwidget = QtGui.QWidget(TWOHOUR)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(18)
        if self.shift=="Evening":
                self.tableWidget.setRowCount(3)
                for n in range(0,3):
                    item = QtGui.QTableWidgetItem()
                    item.setText("")
                    self.tableWidget.setVerticalHeaderItem(n, item)
                for k in range (0,3):
                    for t in range(0,18):
                        item = QtGui.QTableWidgetItem()
                        item.setText("")
                        self.tableWidget.setItem(k, t, item)
        if self.shift=="Morning":
                self.tableWidget.setRowCount(4)
                for n in range(0,4):
                    item = QtGui.QTableWidgetItem()
                    item.setText("")
                    self.tableWidget.setVerticalHeaderItem(n, item)
                for k in range (0,4):
                    for t in range(0,18):
                        item = QtGui.QTableWidgetItem()
                        item.setText("")
                        self.tableWidget.setItem(k, t, item)
        if self.shift=="Night":
                self.tableWidget.setRowCount(5)
                for n in range(0,5):
                    item = QtGui.QTableWidgetItem()
                    item.setText("")
                    self.tableWidget.setVerticalHeaderItem(n, item)
                for k in range (0,5):
                    for t in range(0,18):
                        item = QtGui.QTableWidgetItem()
                        item.setText("")
                        self.tableWidget.setItem(k, t, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT * FROM TWOHOUR WHERE SHIFT = '%s' AND DATE = '%s'"%(u1.shift,p))
        r=cursor1.rowcount
        data = cursor1.fetchall()
        n=0
        for ro in data:
            for k in range (0,17):
                item = QtGui.QTableWidgetItem()
                item.setText(ro[k])
                self.tableWidget.setItem(n, k, item)
            if n==r:
                break
            else:
                n+=1
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        TWOHOUR.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.cancel)
        self.retranslateUi(TWOHOUR)
        QtCore.QMetaObject.connectSlotsByName(TWOHOUR)

    def retranslateUi(self, TWOHOUR):
        TWOHOUR.setWindowTitle("Two Hourly Task")
        if self.shift=="Night":
            item = self.tableWidget.verticalHeaderItem(0)
            item.setText("21:00")
            item = self.tableWidget.verticalHeaderItem(1)
            item.setText("23:00")
            item = self.tableWidget.verticalHeaderItem(2)
            item.setText("01:00")
            item = self.tableWidget.verticalHeaderItem(3)
            item.setText("03:00")
            item = self.tableWidget.verticalHeaderItem(4)
            item.setText("05:00")
        elif self.shift=="Evening":
            item = self.tableWidget.verticalHeaderItem(0)
            item.setText("15:00")
            item = self.tableWidget.verticalHeaderItem(1)
            item.setText("17:00")
            item = self.tableWidget.verticalHeaderItem(2)
            item.setText("19:00")
        if self.shift=="Morning":
            item = self.tableWidget.verticalHeaderItem(0)
            item.setText("7:00")
            item = self.tableWidget.verticalHeaderItem(1)
            item.setText("9:00")
            item = self.tableWidget.verticalHeaderItem(2)
            item.setText("11:00")
            item = self.tableWidget.verticalHeaderItem(3)
            item.setText("13:00")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("CPU - EAPP1")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("CPU - EAPP2")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("CPU - EDB2")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("CPU - EDB1")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText("CPU - PAPP1")
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText("CPU - PAPP2")
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText("CPU - PFOIS1")
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText("CPU - PFOIS2")
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText("Load Average - PAPP1")
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText("Load Average - PAPP2")
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText("Load Average - PFOIS1")
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText("Load Average - PFOIS2")
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText("Memory Queue - PAPP1")
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText("Memory Queue - PAPP2")
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText("Disk Queue - PAPP1")
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText("Disk Queue - PAPP2")
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText("Connected User - RMS")
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText("Connected User - TMS")
        self.pushButton.setText("Insert")
        self.pushButton_2.setText("Cancel")

    def cancel(self):
        self.ui = Ui_Shift()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def insert(self):
        allRows = self.tableWidget.rowCount()
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("DELETE FROM project.TWOHOUR WHERE `DATE`='%s' AND `SHIFT`='%s'"%(p,u1.shift))
        for row in xrange (0,allRows):
            a = self.tableWidget.item(row,0).text()
            b = self.tableWidget.item(row,1).text()
            c = self.tableWidget.item(row,2).text()
            d = self.tableWidget.item(row,3).text()
            e = self.tableWidget.item(row,4).text()
            f = self.tableWidget.item(row,5).text()
            g = self.tableWidget.item(row,5).text()
            h = self.tableWidget.item(row,6).text()
            i = self.tableWidget.item(row,7).text()
            j = self.tableWidget.item(row,8).text()
            k = self.tableWidget.item(row,9).text()
            l = self.tableWidget.item(row,10).text()
            m = self.tableWidget.item(row,11).text()
            n = self.tableWidget.item(row,12).text()
            o = self.tableWidget.item(row,13).text()
            pp = self.tableWidget.item(row,14).text()
            q = self.tableWidget.item(row,15).text()
            r = self.tableWidget.item(row,16).text()
            s=self.tableWidget.item(row,17).text()
            t=self.tableWidget.verticalHeaderItem(row).text()
            cursor1.execute ("INSERT INTO project.TWOHOUR(`CPU-EAPP1`, `CPU-EAPP2`, `CPU-EDB1`, `CPU-EDB2`, `CPU-PAPP1`, `CPU-PAPP2`, `CPU-PFOIS1`, `CPU-PFOIS2`, `LOADAVG-PAPP1`, `LOADAVG-PAPP2`, `LOADAVG-PFOIS1`, `LOADAVG-PFOIS2`, `MEMQ-PAPP1`, `MEMQ-PAPP2`, `DISKQ-PAPP1`, `DISKQ-PAPP2`, `USER-RMS`, `USER-TMS`,`TIME`, `DATE`, SHIFT)VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(a,b,c,d,e,f,g,h,i,j,k,l,n,o,pp,q,r,s,t,p,self.shift))
            self.tableWidget.insertRow(allRows+1)
        db1.commit()
        self.uip = Dialog(6)
        self.uip.show()
        self.cancel()

class TWOHOUR(QtGui.QMainWindow, Ui_TWOHOUR):

    def __init__(self, k,parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.shift=k
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_Log(object):

    def setupUi(self, Log):
        datecheck()
        self.centralwidget = QtGui.QWidget(Log)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(4)
        cursor1.execute("SELECT * FROM USERLOG")
        r = cursor1.rowcount
        self.tableWidget.setRowCount(r)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        data = cursor1.fetchall()
        n = 0
        for ro in data:
            item = QtGui.QTableWidgetItem()
            item.setText(ro[0])
            self.tableWidget.setItem(n, 0, item)
            item = QtGui.QTableWidgetItem()
            item.setText(ro[1])
            self.tableWidget.setItem(n, 1, item)
            item = QtGui.QTableWidgetItem()
            item.setText(ro[2])
            self.tableWidget.setItem(n, 2, item)
            item = QtGui.QTableWidgetItem()
            item.setText(ro[3])
            self.tableWidget.setItem(n, 3, item)
            if n == r:
                break
            else:
                n += 1
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        Log.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.stop)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.retranslateUi(Log)
        QtCore.QMetaObject.connectSlotsByName(Log)

    def retranslateUi(self, Log):
        Log.setWindowTitle( "User Log")
        self.pushButton.setText( "Ok")
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText( "1")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText( "Name")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText( "Date")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText( "Time")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText( "Shift")

    def stop(self):
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

class Log(QtGui.QMainWindow, Ui_Log):

    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_MT(object):
    yy=None

    def setupUi(self, MT):
        datecheck()
        self.centralwidget = QtGui.QWidget(MT)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 2, 4, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText("")
        self.tableWidget.setColumnCount(1)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT %s FROM TASK WHERE %s IS NOT NULL"%(self.yy,self.yy))
        data = cursor1.fetchall()
        r=cursor1.rowcount
        self.tableWidget.setRowCount(r)
        n=0
        for ro in data:
            item = QtGui.QTableWidgetItem()
            item.setText(ro[0])
            self.tableWidget.setItem(n, 0, item)
            if n==r:
                break
            else:
                n+=1
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(400)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 5)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        MT.setCentralWidget(self.centralwidget)
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.cancel)
        self.retranslateUi(MT)
        QtCore.QMetaObject.connectSlotsByName(MT)

    def retranslateUi(self, MT):
        MT.setWindowTitle("Modify Task")
        self.pushButton.setText("Modify")
        self.pushButton_2.setText("Cancel")
        self.pushButton_3.setText("Delete")
        self.label.setText("Enter/Edit Task")
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText("1")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Task")

    def insert(self):
        allRows = self.tableWidget.rowCount()
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("UPDATE TASK SET %s =NULL"%(self.yy))
        for row in xrange (0,allRows):
            a = self.tableWidget.item(row,0).text()
            cursor1.execute("INSERT INTO TASK(%s) VALUES('%s')"%(self.yy,a))
        cursor1.execute("DELETE FROM TASK WHERE SEA IS NULL AND TASC IS NULL")
        db1.commit()
        self.uip = Dialog(10)
        self.uip.show()
        self.cancel()

    def cancel(self):
        self.ui = Ui_AdminWindow()
        MainWindow.show()
        self.close()

    def delete(self):
        index=self.tableWidget.currentRow()
        a=self.tableWidget.item(index,0).text()
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("DELETE FROM TASK WHERE %s = '%s'"%(self.yy,a))
        cursor1.execute("DELETE FROM TASK WHERE SEA IS NULL AND TASC IS NULL")
        db1.commit()
        self.uip = Dialog(16)
        self.uip.show()
        self.ui1 = MT(self.yy)
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()
        self.cancel()

class MT(QtGui.QMainWindow, Ui_MT):

    def __init__(self, p,parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.yy=p
        self.setupUi(self)

class Ui_modt(object):
    yy=None

    def setupUi(self, modt):
        datecheck()
        self.centralwidget = QtGui.QWidget(modt)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 3, 4, 1, 1)
        if self.yy=="DDA":
            self.label.setText("Select date")
            self.spinBox = QtGui.QSpinBox(self.centralwidget)
            self.spinBox.setMinimum(1)
            self.spinBox.setMaximum(31)
            self.gridLayout.addWidget(self.spinBox, 1, 3, 1, 1)
            self.spinBox.setMinimum(1)
            self.spinBox.setMaximum(31)
            self.spinBox.valueChanged.connect(self.prn2)
        elif self.yy== "HOURLY":
            self.label.setText("Select Shift")
            self.comboBox = QtGui.QComboBox(self.centralwidget)
            self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 2)
            self.comboBox.addItem("MORNING")
            self.comboBox.addItem("EVENING")
            self.comboBox.addItem("NIGHT")
            self.comboBox.activated[str].connect(self.prn4)
        elif self.yy== "DRT":
            self.label.setText("Select Shift")
            self.comboBox = QtGui.QComboBox(self.centralwidget)
            self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 2)
            self.comboBox.addItem("MORNING")
            self.comboBox.addItem("EVENING")
            self.comboBox.addItem("NIGHT")
            self.comboBox.activated[str].connect(self.prn)
        elif self.yy== "MISC":
            self.label.setText("Select Activity")
            self.comboBox = QtGui.QComboBox(self.centralwidget)
            self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 2)
            self.comboBox.addItem("MONDAY")
            self.comboBox.addItem("MONDAY")
            self.comboBox.addItem("TUESDAY")
            self.comboBox.addItem("WEDNESDAY")
            self.comboBox.addItem("THURSDAY")
            self.comboBox.addItem("FRIDAY")
            self.comboBox.addItem("SATURDAY")
            self.comboBox.addItem("SUNDAY")
            self.comboBox.addItem("MONTHLY")
            self.comboBox.addItem("FORTNIGHTLY")
            self.comboBox.activated[str].connect(self.prn3)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 5)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 3, 1, 1)
        modt.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton_3.clicked.connect(self.delete)
        self.retranslateUi(modt)
        QtCore.QMetaObject.connectSlotsByName(modt)

    def retranslateUi(self, modt):
        modt.setWindowTitle("Modify Task")
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText("1")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Task")
        item = self.tableWidget.horizontalHeaderItem(1)
        if self.yy=="DRT":
            item.setText("Shift")
        elif self.yy=="DDA":
            item.setText("DAY")
        elif self.yy=="MISC":
            item.setText("Task of")
        self.pushButton.setText("Modify")
        self.label.setText("Select Task")
        self.pushButton_2.setText("Cancel")
        self.pushButton_3.setText( "Delete")

    def prn2(self):
        text = str(self.spinBox.value())
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT `%s` FROM project.DATEDEPENDENT WHERE `%s` IS NOT NULL"%(text,text))
        data1 = cursor1.fetchall()
        r=0
        for ro in data1:
            if ro[0]=="":
                continue
            else :
                r+=1
        self.tableWidget.setRowCount(r)
        n=0
        for ro in data1:
            if ro[0]=="":
                continue
            else:
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                self.tableWidget.setItem(n,0, item)
                item = QtGui.QTableWidgetItem()
                item.setText(text)
                self.tableWidget.setItem(n,1, item)
                if n==r:
                    break
                else:
                    n+=1

    def prn4(self):
        text = str(self.comboBox.currentText())
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT %s FROM project.HOURLYTASK WHERE %s IS NOT NULL"%(text,text))
        data1 = cursor1.fetchall()
        r=cursor1.rowcount
        self.tableWidget.setRowCount(r)
        n=0
        for ro in data1:
            item = QtGui.QTableWidgetItem()
            item.setText(ro[0])
            self.tableWidget.setItem(n,0, item)
            item = QtGui.QTableWidgetItem()
            item.setText(text)
            self.tableWidget.setItem(n,1, item)
            if n==r:
                break
            else:
                n+=1

    def prn3(self):
        text = str(self.comboBox.currentText())
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()

        cursor1.execute("SELECT %s FROM project.MISC WHERE %s IS NOT NULL"%(text,text))
        data1 = cursor1.fetchall()
        r=cursor1.rowcount
        self.tableWidget.setRowCount(r)
        n=0
        for ro in data1:
            if ro[0]==None:
                continue
            item = QtGui.QTableWidgetItem()
            item.setText(ro[0])
            self.tableWidget.setItem(n,0, item)
            item = QtGui.QTableWidgetItem()
            item.setText(text)
            self.tableWidget.setItem(n,1, item)
            if n==r:
                break
            else:
                n+=1

    def prn(self):
        text = str(self.comboBox.currentText())
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT %s FROM project.DAILY WHERE %s IS NOT NULL"%(text,text))
        data1 = cursor1.fetchall()
        r=cursor1.rowcount
        self.tableWidget.setRowCount(r)
        n=0
        for ro in data1:
            item = QtGui.QTableWidgetItem()
            item.setText(ro[0])
            self.tableWidget.setItem(n,0, item)
            item = QtGui.QTableWidgetItem()
            item.setText(text)
            self.tableWidget.setItem(n,1, item)
            if n==r:
                break
            else:
                n+=1

    def insert(self):
        if self.yy=="DDA":
            k=str(self.spinBox.value())
            allRows = self.tableWidget.rowCount()
            db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor1 = db1.cursor()
            cursor1.execute("UPDATE project.DATEDEPENDENT SET `%s`=NULL"%(k))
            cursor1.execute("DELETE FROM  project.DATEDEPENDENT WHERE `1`IS NULL AND `2`IS NULL AND `3`IS NULL AND `4`IS NULL AND `5`IS NULL AND `6`IS NULL AND `7`IS NULL AND `8`IS NULL AND `9`IS NULL AND `10`IS NULL AND `11`IS NULL AND `12`IS NULL AND `13`IS NULL AND `14`IS NULL AND `15`IS NULL AND `16`IS NULL AND `17`IS NULL AND `18`IS NULL AND `19`IS NULL AND `20`IS NULL AND `21`IS NULL AND `22`IS NULL AND `23`IS NULL AND `24`IS NULL AND `25`IS NULL AND `26`IS NULL AND `27`IS NULL AND `29`IS NULL AND `30`IS NULL AND `31`IS NULL")
            for row in xrange (0,allRows):
                a = self.tableWidget.item(row,0).text()
                b=self.tableWidget.item(row,1).text()
                cursor1.execute("INSERT INTO project.DATEDEPENDENT (`%s`) VALUES('%s')"%(b,a))
        elif self.yy=="DRT":
            k=str(self.comboBox.currentText())
            r=0
            cursor1.execute("SELECT %s FROM project.DAILY WHERE %s IS NOT NULL"%(k,k))
            data1 = cursor1.fetchall()
            for ro in data1:
                if ro[0]=="":
                    continue
                else :
                    r+=1
            cursor1.execute("UPDATE project.DAILY SET %s=NULL"%(k))
            cursor1.execute("DELETE FROM  project.DAILY WHERE MORNING IS NULL AND EVENING IS NULL AND NIGHT IS NULL ")
            for row in xrange (0,r):
                a= self.tableWidget.item(row,0).text()
                b= self.tableWidget.item(row,1).text()
                cursor1.execute("INSERT INTO project.DAILY (%s) VALUES('%s')"%(b,a))
        elif self.yy=="HOURLY":
            k=str(self.comboBox.currentText())
            r=0
            cursor1.execute("SELECT %s FROM project.HOURLYTASK WHERE %s IS NOT NULL"%(k,k))
            data1 = cursor1.fetchall()
            for ro in data1:
                if ro[0]=="":
                    continue
                else :
                    r+=1
            cursor1.execute("UPDATE project.HOURLYTASK SET %s=NULL"%(k))
            cursor1.execute("DELETE FROM  project.HOURLYTASK WHERE MORNING IS NULL AND EVENING IS NULL AND NIGHT IS NULL ")
            for row in xrange (0,r):
                a= self.tableWidget.item(row,0).text()
                b= self.tableWidget.item(row,1).text()
                cursor1.execute("INSERT INTO project.HOURLYTASK (%s) VALUES('%s')"%(b,a))
        elif self.yy=="MISC":
            k=str(self.comboBox.currentText())
            allRows = self.tableWidget.rowCount()
            cursor1.execute("UPDATE project.MISC SET %s=NULL"%(k))
            cursor1.execute("DELETE FROM  project.MISC WHERE MONDAY IS NULL AND TUESDAY IS NULL AND THURSDAY IS NULL AND WEDNESDAY IS NULL AND FRIDAY IS NULL AND SATURDAY IS NULL AND SUNDAY IS NULL AND MONTHLY IS NULL AND FORTNIGHTLY IS NULL")
            for row in xrange (0,allRows):
                a = self.tableWidget.item(row,0).text()
                b=self.tableWidget.item(row,1).text()
                cursor1.execute("INSERT INTO project.MISC (%s) VALUES('%s')"%(b,a))
        db1.commit()
        self.uip = Dialog(10)
        self.uip.show()
        self.cancel()

    def delete(self):
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        if self.yy=="DDA":
            k=str(self.spinBox.value())
            index=self.tableWidget.currentRow()
            a=self.tableWidget.item(index,0).text()
            cursor1.execute("DELETE FROM project.DATEDEPENDENT WHERE %s = '%s'"%(k,a))
        elif self.yy=="DRT":
            k=str(self.comboBox.currentText())
            index=self.tableWidget.currentRow()
            a=self.tableWidget.item(index,0).text()
            cursor1.execute("DELETE FROM project.DAILY WHERE %s = '%s'"%(k,a))
        elif self.yy=="HOURLY":
            k=str(self.comboBox.currentText())
            index=self.tableWidget.currentRow()
            a=self.tableWidget.item(index,0).text()
            cursor1.execute("DELETE FROM project.HOURLYTASK WHERE %s = '%s' "%(k,a))
        elif self.yy=="MISC":
            k=str(self.comboBox.currentText())
            index=self.tableWidget.currentRow()
            a=self.tableWidget.item(index,0).text()
            cursor1.execute("DELETE FROM project.MISC WHERE %s = '%s'"%(k,a))
        db1.commit()
        self.uip = Dialog(16)
        self.uip.show()
        self.ui1 = modt(self.yy)
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()
        self.cancel()

    def cancel(self):
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

class modt(QtGui.QMainWindow, Ui_modt):

    def __init__(self,p, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.yy=p
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_AT(object):
    yy=None

    def setupUi(self, AT):
        datecheck()
        self.centralwidget = QtGui.QWidget(AT)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        if self.yy== "DRT":
            self.comboBox = QtGui.QComboBox(self.centralwidget)
            self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
            self.label_2 = QtGui.QLabel(self.centralwidget)
            self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
            self.label_2.setText( "Shift")
            self.comboBox.addItem("")
            self.comboBox.addItem("MORNING")
            self.comboBox.addItem("EVENING")
            self.comboBox.addItem("NIGHT")
        elif self.yy=="DDA":
            self.spinBox = QtGui.QSpinBox(self.centralwidget)
            self.spinBox.setMinimum(1)
            self.spinBox.setMaximum(31)
            self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
            self.label_3 = QtGui.QLabel(self.centralwidget)
            self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
            self.label_3.setText( "Date")
        elif self.yy== "MISC":
            self.comboBox = QtGui.QComboBox(self.centralwidget)
            self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
            self.label_2 = QtGui.QLabel(self.centralwidget)
            self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
            self.label_2.setText( "TASK")
            self.comboBox.addItem("")
            self.comboBox.addItem("MONDAY")
            self.comboBox.addItem("TUESDAY")
            self.comboBox.addItem("WEDNESDAY")
            self.comboBox.addItem("THURSDAY")
            self.comboBox.addItem("FRIDAY")
            self.comboBox.addItem("SATURDAY")
            self.comboBox.addItem("SUNDAY")
            self.comboBox.addItem("MONTHLY")
            self.comboBox.addItem("FORTNIGHTLY")
        elif self.yy=="HOURLY":
            self.comboBox = QtGui.QComboBox(self.centralwidget)
            self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
            self.label_2 = QtGui.QLabel(self.centralwidget)
            self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
            self.label_2.setText( "Shift")
            self.comboBox.addItem("")
            self.comboBox.addItem("MORNING")
            self.comboBox.addItem("EVENING")
            self.comboBox.addItem("NIGHT")
        self.label = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 3)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 5, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        AT.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.cancel)
        self.retranslateUi(AT)
        QtCore.QMetaObject.connectSlotsByName(AT)

    def retranslateUi(self, AT):
        AT.setWindowTitle("Add Task")
        self.label.setText("Task")
        self.pushButton.setText("Add Task")
        self.pushButton_2.setText("Cancel")

    def cancel(self):
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def insert(self):
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        if self.yy=="DRT":
            text = str(self.comboBox.currentText())
            a = self.lineEdit.text()
            cursor1.execute("INSERT INTO project.DAILY(%s)VALUES('%s')" % (text,a))
        elif self.yy=="DDA":
            d=str(self.spinBox.value())
            a = self.lineEdit.text()
            cursor1.execute("INSERT INTO project.DATEDEPENDENT(`%s`)VALUES('%s')" %(d,a))
        elif self.yy==("MISC"):
            text = str(self.comboBox.currentText())
            a = self.lineEdit.text()
            cursor1.execute("INSERT INTO project.MISC(%s)VALUES('%s')" % (text,a))
        else:
            a = self.lineEdit.text()
            cursor1.execute("INSERT INTO TASK(%s) VALUES('%s')" % (self.yy,a))
        db1.commit()
        self.uip = Dialog(9)
        self.uip.show()
        self.cancel()

class AT(QtGui.QMainWindow, Ui_AT):

    def __init__(self,p ,parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.yy=p
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_AdminWindow(object):

    def setupUi(self, AdminWindow):
        datecheck()
        self.centralwidget = QtGui.QWidget(AdminWindow)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AdminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuCreate = QtGui.QMenu(self.menubar)
        self.menuTask = QtGui.QMenu(self.menuCreate)
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuTask_2 = QtGui.QMenu(self.menuEdit)
        self.menuView_Task = QtGui.QMenu(self.menubar)
        AdminWindow.setMenuBar(self.menubar)
        self.actionChange_Database = QtGui.QAction(AdminWindow)
        self.menuFile.addAction(self.actionChange_Database)
        self.actionLogout = QtGui.QAction(AdminWindow)
        self.actionQuit = QtGui.QAction(AdminWindow)
        self.actionUser = QtGui.QAction(AdminWindow)
        self.actionUser_2 = QtGui.QAction(AdminWindow)
        self.actionDaily_Routine_Task = QtGui.QAction(AdminWindow)
        self.actionHourly_Task = QtGui.QAction(AdminWindow)
        self.actionDate_Dependant_Task = QtGui.QAction(AdminWindow)
        self.actionShift_End_Activity = QtGui.QAction(AdminWindow)
        self.actionTask_at_shift_Change = QtGui.QAction(AdminWindow)
        self.actionDaily_Routine_Task_2 = QtGui.QAction(AdminWindow)
        self.actionDate_Dependent_Activity = QtGui.QAction(AdminWindow)
        self.actionShift_End_Activity_2 = QtGui.QAction(AdminWindow)
        self.actionTask_at_Shift_Change = QtGui.QAction(AdminWindow)
        self.actionHourly_Task_2 = QtGui.QAction(AdminWindow)
        self.actionView = QtGui.QAction(AdminWindow)
        self.actionMisc = QtGui.QAction(AdminWindow)
        self.actionMisc_2 = QtGui.QAction(AdminWindow)
        self.actionView_User_Log = QtGui.QAction(AdminWindow)
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionQuit)
        self.menuTask.addAction(self.actionDaily_Routine_Task)
        self.menuTask.addAction(self.actionHourly_Task)
        self.menuTask.addAction(self.actionDate_Dependant_Task)
        self.menuTask.addAction(self.actionShift_End_Activity)
        self.menuTask.addAction(self.actionTask_at_shift_Change)
        self.menuTask.addAction(self.actionMisc)
        self.menuCreate.addAction(self.actionUser)
        self.menuCreate.addAction(self.menuTask.menuAction())
        self.menuTask_2.addAction(self.actionDaily_Routine_Task_2)
        self.menuTask_2.addAction(self.actionDate_Dependent_Activity)
        self.menuTask_2.addAction(self.actionShift_End_Activity_2)
        self.menuTask_2.addAction(self.actionTask_at_Shift_Change)
        self.menuTask_2.addAction(self.actionHourly_Task_2)
        self.menuTask_2.addAction(self.actionMisc_2)
        self.menuEdit.addAction(self.actionUser_2)
        self.menuEdit.addAction(self.menuTask_2.menuAction())
        self.menuView_Task.addAction(self.actionView)
        self.menuView_Task.addAction(self.actionView_User_Log)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCreate.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView_Task.menuAction())
        self.actionMisc.triggered.connect(self.misc)
        self.actionMisc_2.triggered.connect(self.miscm)
        self.actionDate_Dependant_Task.triggered.connect(self.dda)
        self.actionDaily_Routine_Task.triggered.connect(self.drt)
        self.actionHourly_Task.triggered.connect(self.ht)
        self.actionShift_End_Activity.triggered.connect(self.sea)
        self.actionTask_at_shift_Change.triggered.connect(self.tasc)
        self.actionDate_Dependent_Activity.triggered.connect(self.ddam)
        self.actionDaily_Routine_Task_2.triggered.connect(self.drtm)
        self.actionHourly_Task_2.triggered.connect(self.htm)
        self.actionShift_End_Activity_2.triggered.connect(self.seam)
        self.actionTask_at_Shift_Change.triggered.connect(self.tascm)
        self.actionUser.triggered.connect(self.adduser)
        self.actionUser_2.triggered.connect(self.moduser)
        self.pushButton.clicked.connect(self.cancel)
        self.actionView.triggered.connect(self.view)
        self.actionQuit.triggered.connect(self.cancel)
        self.actionView_User_Log.triggered.connect(self.log)
        self.actionLogout.triggered.connect(self.logout)
        self.actionChange_Database.triggered.connect(self.db)
        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def logout(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def view(self):
        self.ui1 = VIEWTASK()
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def misc(self):
        self.ui1 = AT("MISC")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def miscm(self):
        self.ui1 = modt("MISC")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def tasc(self):
        self.ui1 = AT("TASC")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def sea(self):
        self.ui1 = AT("SEA")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def dda(self):
        self.ui1 = addt("DDA")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def drt(self):
        self.ui1 = addt("DRT")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def ht(self):
        self.ui1 = addt("HOURLY")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def tascm(self):
        self.ui1 = MT("TASC")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def seam(self):
        self.ui1 = MT("SEA")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def ddam(self):
        self.ui1 = modt("DDA")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def drtm(self):
        self.ui1 = modt("DRT")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def htm(self):
        self.ui1 = modt("HOURLY")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def cancel(self):
        self.ui1 = MainWindow_1()
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def log(self):
        self.ui1 = Log()
        self.ui1.setupUi(MainWindow)
        MainWindow.show()

    def adduser(self):
        self.ui1 = Ui_CU()
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def moduser(self):
        self.ui = Ui_MU()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def db(self):
        self.uip = dbedit()
        self.uip.show()
        self.close()
    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle( "Admin Window")
        self.pushButton.setText( "Cancel")
        self.menuFile.setTitle( "File")
        self.menuCreate.setTitle( "Create")
        self.menuTask.setTitle( "Task")
        self.menuEdit.setTitle( "Edit")
        self.menuTask_2.setTitle( "Task")
        self.menuView_Task.setTitle( "View")
        self.actionLogout.setText( "Logout")
        self.actionQuit.setText( "Quit")
        self.actionUser.setText( "User")
        self.actionUser_2.setText( "User")
        self.actionDaily_Routine_Task.setText( "Daily Routine Task")
        self.actionHourly_Task.setText( "Hourly Task")
        self.actionDate_Dependant_Task.setText( "Date Dependant Task")
        self.actionShift_End_Activity.setText( "Shift End Activity")
        self.actionTask_at_shift_Change.setText( "Task at Shift Change")
        self.actionDaily_Routine_Task_2.setText( "Daily Routine Task")
        self.actionDate_Dependent_Activity.setText( "Date Dependent Activity")
        self.actionShift_End_Activity_2.setText( "Shift End Activity")
        self.actionTask_at_Shift_Change.setText( "Task at Shift Change")
        self.actionHourly_Task_2.setText( "Hourly Task")
        self.actionChange_Database.setText("Change Database")
        self.actionView.setText( " View Task")
        self.actionMisc.setText( "Misc")
        self.actionMisc_2.setText( "Misc")
        self.actionView_User_Log.setText( "View User Log")

class AdminWindow(QtGui.QMainWindow, Ui_AdminWindow):

    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_addt(object):
    yy=None

    def setupUi(self, addt):
        datecheck()
        self.centralwidget = QtGui.QWidget(addt)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 420, 85, 28))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 230, 66, 20))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 280, 481, 28))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 420, 85, 28))
        if self.yy== "DRT":
            self.comboBox = QtGui.QComboBox(self.centralwidget)
            self.comboBox.setGeometry(QtCore.QRect(50, 110, 86, 28))
            self.label_2 = QtGui.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(40, 40, 66, 20))
            self.label_2.setText( "Shift")
            self.comboBox.addItem("")
            self.comboBox.addItem("MORNING")
            self.comboBox.addItem("EVENING")
            self.comboBox.addItem("NIGHT")
        elif self.yy=="DDA":
            self.spinBox = QtGui.QSpinBox(self.centralwidget)
            self.spinBox.setGeometry(QtCore.QRect(50, 110, 71, 29))
            self.spinBox.setMinimum(1)
            self.spinBox.setMaximum(31)
            self.label_3 = QtGui.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(40, 40, 66, 20))
            self.label_3.setText( "Date")
        elif self.yy== "HOURLY":
            self.comboBox = QtGui.QComboBox(self.centralwidget)
            self.comboBox.setGeometry(QtCore.QRect(50, 110, 86, 28))
            self.label_2 = QtGui.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(40, 40, 66, 20))
            self.label_2.setText( "Shift")
            self.comboBox.addItem("")
            self.comboBox.addItem("MORNING")
            self.comboBox.addItem("EVENING")
            self.comboBox.addItem("NIGHT")
        addt.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.cancel)
        self.retranslateUi(addt)
        QtCore.QMetaObject.connectSlotsByName(addt)

    def retranslateUi(self, addt):
        addt.setWindowTitle( "Add Task")
        self.pushButton.setText( "Add Task")
        self.label.setText( "Task")
        self.pushButton_2.setText( "Cancel")

    def cancel(self):
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def insert(self):
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        if self.yy=="DRT":
            text = str(self.comboBox.currentText())
            a = self.lineEdit.text()
            cursor1.execute("INSERT INTO project.DAILY(%s)VALUES('%s')" % (text,a))
        elif self.yy=="HOURLY":
            text = str(self.comboBox.currentText())
            a = self.lineEdit.text()
            cursor1.execute("INSERT INTO project.HOURLYTASK(%s)VALUES('%s')" % (text,a))
        elif self.yy=="DDA":
            d=str(self.spinBox.value())
            a = self.lineEdit.text()
            cursor1.execute("INSERT INTO project.DATEDEPENDENT(`%s`)VALUES('%s')" %(d,a))
        else:
            a = self.lineEdit.text()
            cursor1.execute("INSERT INTO TASK(%s) VALUES('%s')" % (self.yy,a))
        db1.commit()
        self.uip = Dialog(9)
        self.uip.show()
        self.cancel()

class addt(QtGui.QMainWindow, Ui_addt):

    def __init__(self,p ,parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.yy=p
        self.setupUi(self)

class Ui_TVIEW(object):
    d=None
    shift=None

    def setupUi(self, TVIEW):
        datecheck()
        self.centralwidget = QtGui.QWidget(TVIEW)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(21)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        TVIEW.setCentralWidget(self.centralwidget)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT * FROM TWOHOUR WHERE SHIFT = '%s' AND DATE = '%s'"%(self.d,self.shift))
        r=cursor1.rowcount
        if r==0:
            self.uip = Dialog(17)
            self.uip.show()
            self.cancel()
        else:
            self.tableWidget.setRowCount(r)
            data = cursor1.fetchall()
            n=0
            for ro in data:
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                self.tableWidget.setItem(n, 3, item)
                item = QtGui.QTableWidgetItem()
                item.setText(ro[0])
                self.tableWidget.setItem(n, 4, item)
                item = QtGui.QTableWidgetItem()
                item.setText(ro[1])
                self.tableWidget.setItem(n, 5, item)
                item = QtGui.QTableWidgetItem()
                item.setText(ro[2])
                self.tableWidget.setItem(n, 6, item)
                item = QtGui.QTableWidgetItem()
                item.setText(ro[3])
                self.tableWidget.setItem(n, 7, item)
                item.setText(ro[4])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 8, item)
                item.setText(ro[5])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 9, item)
                item.setText(ro[6])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 10, item)
                item.setText(ro[7])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 11, item)
                item.setText(ro[8])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 12, item)
                item.setText(ro[9])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 13, item)
                item.setText(ro[10])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 14, item)
                item.setText(ro[11])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 15, item)
                item.setText(ro[12])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 16, item)
                item.setText(ro[13])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 17, item)
                item.setText(ro[14])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 18, item)
                item.setText(ro[15])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 19, item)
                item.setText(ro[16])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 20, item)
                item.setText(ro[17])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 0, item)
                item.setText(ro[18])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 1, item)
                item.setText(ro[19])
                item = QtGui.QTableWidgetItem()
                self.tableWidget.setItem(n, 2, item)
                item.setText(ro[20])
                if n==r:
                    break
                else:
                    n+=1
            self.tableWidget.setRowCount(r)
            self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
            self.pushButton.clicked.connect(self.insert)
            self.pushButton_2.clicked.connect(self.cancel)
        self.retranslateUi(TVIEW)
        QtCore.QMetaObject.connectSlotsByName(TVIEW)

    def cancel(self):
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def insert(self):
        allRows = self.tableWidget.rowCount()
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("DELETE FROM project.TWOHOUR WHERE SHIFT = '%s' AND DATE = '%s'"%(self.shift,self.dt))
        for row in xrange (0,allRows):
            a = self.tableWidget.item(row,0).text()
            b = self.tableWidget.item(row,1).text()
            c = self.tableWidget.item(row,2).text()
            d = self.tableWidget.item(row,3).text()
            e = self.tableWidget.item(row,4).text()
            f = self.tableWidget.item(row,5).text()
            g = self.tableWidget.item(row,5).text()
            h = self.tableWidget.item(row,6).text()
            i = self.tableWidget.item(row,7).text()
            j = self.tableWidget.item(row,8).text()
            k = self.tableWidget.item(row,9).text()
            l = self.tableWidget.item(row,10).text()
            m = self.tableWidget.item(row,11).text()
            n = self.tableWidget.item(row,12).text()
            o = self.tableWidget.item(row,13).text()
            pp = self.tableWidget.item(row,14).text()
            q = self.tableWidget.item(row,15).text()
            r = self.tableWidget.item(row,16).text()
            s=self.tableWidget.item(row,17).text()
            t=self.tableWidget.verticalHeaderItem(row).text()
            cursor1.execute ("INSERT INTO project.TWOHOUR(`CPU-EAPP1`, `CPU-EAPP2`, `CPU-EDB1`, `CPU-EDB2`, `CPU-PAPP1`, `CPU-PAPP2`, `CPU-PFOIS1`, `CPU-PFOIS2`, `LOADAVG-PAPP1`, `LOADAVG-PAPP2`, `LOADAVG-PFOIS1`, `LOADAVG-PFOIS2`, `MEMQ-PAPP1`, `MEMQ-PAPP2`, `DISKQ-PAPP1`, `DISKQ-PAPP2`, `USER-RMS`, `USER-TMS`,`TIME`, `DATE`, SHIFT)VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(a,b,c,d,e,f,g,h,i,j,k,l,n,o,pp,q,r,s,t,p,self.shift))
            self.tableWidget.insertRow(allRows+1)
        db1.commit()
        self.uip = Dialog(6)
        self.uip.show()
        self.cancel()

    def retranslateUi(self, TVIEW):
        TVIEW.setWindowTitle( "View Two Hour")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText( "TIME")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText( "DATE")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText( "SHIFT")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText( "CPU - EAPP1")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText( "CPU - EAPP2")
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText( "CPU - EDB2")
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText( "CPU - EDB1")
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText( "CPU - PAPP1")
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText( "CPU - PAPP2")
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText( "CPU - PFOIS1")
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText( "CPU - PFOIS2")
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText( "Load Average - PAPP1")
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText( "Load Average - PAPP2")
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText( "Load Average - PFOIS1")
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText( "Load Average - PFOIS2")
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText( "Memory Queue - PAPP1")
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText( "Memory Queue - PAPP2")
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText( "Disk Queue - PAPP1")
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText( "Disk Queue - PAPP2")
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText( "Connected User - RMS")
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText( "Connected User - TMS")
        self.pushButton_2.setText( "Cancel")
        self.pushButton.setText( "Insert")

class TVIEW(QtGui.QMainWindow, Ui_TVIEW):

    def __init__(self,dob,text, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.d=dob
        self.shift=text
        self.setupUi(self)

class Ui_CU(object):

    def setupUi(self, CU):
        self.centralwidget = QtGui.QWidget(CU)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_7, 1, 4, 1, 2)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_3, 3, 0, 1, 1)
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.gridLayout.addWidget(self.toolButton, 3, 1, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_4, 3, 2, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setCalendarPopup(True)
        self.gridLayout.addWidget(self.dateEdit, 3, 4, 1, 1)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_11, 6, 4, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.gridLayout.addWidget(self.checkBox, 5, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_6, 5, 2, 1, 1)
        self.dateEdit_2 = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit_2.setCalendarPopup(True)
        self.gridLayout.addWidget(self.dateEdit_2, 5, 4, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_5, 7, 0, 1, 3)
        self.dateEdit_3 = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit_3.setCalendarPopup(True)
        self.gridLayout.addWidget(self.dateEdit_3, 7, 4, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 9, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_3, 9, 5, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_9, 2, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_7, 0, 4, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_10, 4, 4, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_6, 4, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 9, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 9, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 9, 3, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 9, 4, 1, 1)
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Password)
        self.dateEdit_2.setDisplayFormat( "d/M/yyyy")
        self.dateEdit_2.setDate(datetime.datetime.strptime(p, "%d-%m-%Y"))
        self.dateEdit.setDisplayFormat( "d/M/yyyy")
        self.dateEdit.setDate(datetime.datetime.strptime(p, "%d-%m-%Y"))
        self.dateEdit_3.setDisplayFormat( "d/M/yyyy")
        self.dateEdit_3.setDate(datetime.datetime.strptime(p, "%d-%m-%Y"))
        CU.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.adduser)
        self.pushButton_3.clicked.connect(self.cancel)
        self.toolButton.pressed.connect(self.pas)
        self.toolButton.released.connect(self.ps)
        self.retranslateUi(CU)
        QtCore.QMetaObject.connectSlotsByName(CU)

    def pas(self):
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Normal)

    def ps(self):
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Password)

    def retranslateUi(self, CU):
        CU.setWindowTitle("Create User")
        self.pushButton.setText("Add User")
        self.pushButton_3.setText("Back")
        self.dateEdit_3.setDisplayFormat("d/M/yy")
        self.label_11.setText("Date Of Last Promotion")
        self.label_9.setText("Date Of Birth")
        self.dateEdit_2.setDisplayFormat("d/M/yy")
        self.checkBox.setText("CheckBox")
        self.label_3.setText("Password")
        self.label_2.setText("User Name")
        self.label_7.setText("Department")
        self.label_5.setText("Employee ID")
        self.label_10.setText("Date Of Joining")
        self.label_6.setText("Designation")
        self.label_8.setText("Admin")
        self.label_4.setText("Address")
        self.dateEdit.setDisplayFormat("d/M/yy")
        self.label.setText("Name")
        self.toolButton.setText("Show")

    def adduser(self):
        uname = self.lineEdit_2.text()
        password =self.lineEdit_3.text()
        name = self.lineEdit.text()
        empid =self.lineEdit_4.text()
        address = self.lineEdit_5.text()
        designation =self.lineEdit_6.text()
        dob = str(self.dateEdit.date().toPyDate())
        doj =str(self.dateEdit_2.date().toPyDate())
        dop =str(self.dateEdit_3.date().toPyDate())
        dept=self.lineEdit_7.text()
        db2=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor2 = db2.cursor()

        if self.checkBox.isChecked():
            admin = 'YES'
        else:
            admin = 'NO'
        cursor2.execute(" INSERT INTO USER(USERNAME,PASSWORD,ADDRESS,ADMIN,EMPID,DESIN,NAME,DOB,DOJ,DOP,DEPT)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(uname, password, address, admin, empid, designation,name,dob,doj,dop,dept))
        db2.commit()
        self.uip = Dialog(7)
        self.uip.show()
        self.cancel()

    def cancel(self):
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

class CU(QtGui.QMainWindow, Ui_CU):

    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_MU(object):

    def setupUi(self, MU):
        self.centralwidget = QtGui.QWidget(MU)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_6, 4, 2, 1, 2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 2)
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_7, 1, 5, 1, 2)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_3, 3, 0, 1, 1)
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.gridLayout.addWidget(self.toolButton, 3, 1, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_4, 3, 2, 1, 2)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setCalendarPopup(True)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.gridLayout.addWidget(self.checkBox, 5, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_6, 5, 2, 1, 2)
        self.dateEdit_2 = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit_2.setCalendarPopup(True)
        self.gridLayout.addWidget(self.dateEdit_2, 5, 5, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_5, 8, 0, 1, 4)
        self.dateEdit_3 = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit_3.setCalendarPopup(True)
        self.gridLayout.addWidget(self.dateEdit_3, 8, 5, 1, 1)
        self.gridLayout.addWidget(self.dateEdit, 3, 5, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 10, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 10, 5, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_3, 10, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_7, 0, 5, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 10, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 2)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_11, 6, 5, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 10, 6, 1, 1)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_10, 4, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_9, 2, 5, 1, 1)
        self.dateEdit_2.setDisplayFormat( "d/M/yyyy")
        self.dateEdit_2.setDate(datetime.datetime.strptime(p, "%d-%m-%Y"))
        self.dateEdit.setDisplayFormat( "d/M/yyyy")
        self.dateEdit.setDate(datetime.datetime.strptime(p, "%d-%m-%Y"))
        self.dateEdit_3.setDisplayFormat( "d/M/yyyy")
        self.dateEdit_3.setDate(datetime.datetime.strptime(p, "%d-%m-%Y"))
        self.comboBox.addItem("")
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Password)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 8, 4, 1, 1)
        MU.setCentralWidget(self.centralwidget)
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT USERNAME FROM USER")
        data1 = cursor1.fetchall()
        for row in data1:
            self.comboBox.addItem(row[0])
        self.comboBox.activated[str].connect(self.prn)
        self.pushButton_3.clicked.connect(self.dele)
        self.pushButton.clicked.connect(self.mod)
        self.pushButton_2.clicked.connect(self.cancel)
        self.toolButton.pressed.connect(self.pas)
        self.toolButton.released.connect(self.ps)
        self.retranslateUi(MU)
        QtCore.QMetaObject.connectSlotsByName(MU)

    def retranslateUi(self, MU):
        MU.setWindowTitle("MainWindow")
        self.label_6.setText("Designation")
        self.label_4.setText("Address")
        self.label.setText("User Name")
        self.label_3.setText("Password")
        self.label_8.setText("Admin")
        self.pushButton_3.setText("Delete")
        self.label_7.setText("Department")
        self.pushButton.setText("Modify User")
        self.label_2.setText("Name")
        self.label_11.setText("Date Of Last Promotion")
        self.checkBox.setText("CheckBox")
        self.label_5.setText("Employee ID")
        self.pushButton_2.setText("Cancel")
        self.dateEdit_2.setDisplayFormat("d/M/yyyy")
        self.label_10.setText("Date Of Joining")
        self.label_9.setText("Date Of Birth")
        self.dateEdit_3.setDisplayFormat("d/M/yyyy")
        self.dateEdit.setDisplayFormat("d/M/yyyy")
        self.toolButton.setText("Show")

    def pas(self):
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Normal)

    def ps(self):
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Password)

    def prn(self):
        text = str(self.comboBox.currentText())
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT * FROM USER WHERE USERNAME='%s'" % (text))
        data1 = cursor1.fetchall()
        for row in data1:
            self.lineEdit_2.setText(row[2])
            self.lineEdit_3.setText(row[1])
            self.lineEdit_4.setText(row[4])
            self.lineEdit_5.setText(row[3])
            self.lineEdit_6.setText(row[6])
            if row[5] == "YES":
                self.checkBox.setChecked(1)
            else :
                self.checkBox.setChecked(0)
            self.lineEdit_7.setText(row[10])
            self.dateEdit.setDate(datetime.datetime.strptime(row[7], "%Y-%m-%d"))
            self.dateEdit_2.setDate(datetime.datetime.strptime(row[8], "%Y-%m-%d"))
            self.dateEdit_3.setDate(datetime.datetime.strptime(row[9], "%Y-%m-%d"))

    def mod(self):
        us = str(self.comboBox.currentText())
        na = self.lineEdit_2.text()
        pa = self.lineEdit_3.text()
        em = self.lineEdit_4.text()
        des = self.lineEdit_6.text()
        ad = self.lineEdit_5.text()
        dob = str(self.dateEdit.date().toPyDate())
        doj = str(self.dateEdit_2.date().toPyDate())
        dop = str(self.dateEdit_3.date().toPyDate())
        dept=self.lineEdit_7.text()
        if self.checkBox.isChecked():
            admin = 'YES'
        else:
            admin = 'NO'
        db2=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor2 = db2.cursor()
        cursor2.execute("UPDATE project.USER SET DEPT='%s', DOP='%s' ,DOB='%s', DOJ='%s', PASSWORD='%s', NAME='%s', ADDRESS='%s', EMPID='%s', ADMIN='%s', DESIN='%s' WHERE USERNAME='%s'" % (dept,dop,dob,doj,pa, na, ad, em, admin, des, us))
        db2.commit()
        self.uip = Dialog(5)
        self.uip.show()
        self.cancel()

    def dele(self):
        text = str(self.comboBox.currentText())
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("DELETE FROM USER WHERE USERNAME='%s'" % (text))
        db1.commit()
        self.uip = Dialog(4)
        self.uip.show()
        self.cancel()

    def cancel(self):
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

class MU(QtGui.QMainWindow, Ui_MU):

    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_Dialog(object):
    n = None

    def setupUi(self, Dialog, p):
        self.n = p
        Dialog.resize(240, 131)
        self.modifiedlabel = QtGui.QLabel(Dialog)
        self.modifiedlabel.setGeometry(QtCore.QRect(60, 40, 121, 16))
        self.okButton = QtGui.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(60, 90, 85, 27))
        self.retranslateUi(Dialog)
        self.okButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Dialog")
        if self.n == 3:
            self.modifiedlabel.setText("Wrong Credentials")
        elif self.n == 2:
            self.modifiedlabel.setText("Wrong Credentials")
        elif self.n == 5:
            self.modifiedlabel.setText("User Modified")
        elif self.n == 1:
            self.modifiedlabel.setText("Login Successful")
        elif self.n == 6:
            self.modifiedlabel.setText("Saved")
        elif self.n == 4:
            self.modifiedlabel.setText("User Deleted")
        elif self.n == 7:
            self.modifiedlabel.setText("User Created")
        elif self.n == 8:
            self.modifiedlabel.setText("Incorrect Entry")
        elif self.n==9:
            self.modifiedlabel.setText("Task Created")
        elif self.n==10:
            self.modifiedlabel.setText("Task Modified")
        elif self.n==11:
            self.modifiedlabel.setText("Data Modified")
        elif self.n==12:
            self.modifiedlabel.setText("Export Complete")
        elif self.n==13:
            self.modifiedlabel.setText("You Were Not In Shift!")
        elif self.n==14:
            self.modifiedlabel.setText("Password changed")
        elif self.n==15:
            self.modifiedlabel.setText("No Task Available")
        elif self.n==17:
            self.modifiedlabel.setText("Task not completed")
        elif self.n==18:
            self.modifiedlabel.setText("No Case Log Available")
        elif self.n==16:
            self.modifiedlabel.setText("Task Deleted")
        elif self.n==20:
            self.modifiedlabel.setText("Changed")
        self.okButton.setText("Ok")

class Dialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, n, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)
        self.setupUi(self, n)

class Ui_MainWindow_1(object):

    def setupUi(self, MainWindow_1):
        datecheck()
        self.centralwidget = QtGui.QWidget(MainWindow_1)
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.admbutton = QtGui.QPushButton(self.centralwidget)
        if u1.admin == "NO":
            self.admbutton.setEnabled(False)
        self.gridLayout_2.addWidget(self.admbutton, 0, 1, 1, 1)
        self.mbutton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.mbutton, 1, 1, 1, 1)
        self.ebutton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.ebutton, 2, 1, 1, 1)
        self.nbutton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.nbutton, 3, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.pushButton, 4, 1, 1, 1)
        self.logoutbutton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.logoutbutton, 5, 0, 1, 1)
        self.quitbutton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.quitbutton, 5, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 5, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 4, 2, 1, 1)
        MainWindow_1.setCentralWidget(self.centralwidget)
        if now.hour < 7 or now.hour >= 21:
            self.ebutton.setEnabled(False)
            self.mbutton.setEnabled(False)
        elif now.hour >= 14 and now.hour < 21:
            self.nbutton.setEnabled(False)
            self.mbutton.setEnabled(False)
        elif now.hour < 14 and now.hour >= 7:
            self.nbutton.setEnabled(False)
            self.ebutton.setEnabled(False)
        self.menubar = QtGui.QMenuBar(MainWindow_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menu1 = QtGui.QMenu(self.menubar)
        MainWindow_1.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow_1)
        MainWindow_1.setStatusBar(self.statusbar)
        self.actionLogout = QtGui.QAction(MainWindow_1)
        self.actionExit = QtGui.QAction(MainWindow_1)
        self.actionEdit_Host = QtGui.QAction(MainWindow_1)
        self.actionExport = QtGui.QAction(MainWindow_1)
        self.menu1.addAction(self.actionLogout)
        self.menu1.addAction(self.actionExit)
        self.menubar.addAction(self.menu1.menuAction())
        self.actionLogout.triggered.connect(self.logout)
        self.actionExit.triggered.connect(MainWindow.close)
        self.logoutbutton.clicked.connect(self.logout)
        self.quitbutton.clicked.connect(MainWindow.close)
        self.mbutton.clicked.connect(self.do)
        self.nbutton.clicked.connect(self.do)
        self.ebutton.clicked.connect(self.do)
        self.pushButton.clicked.connect(self.prntt)
        self.admbutton.clicked.connect(self.adm)
        self.retranslateUi(MainWindow_1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_1)

    def retranslateUi(self, MainWindow_1):
        MainWindow_1.setWindowTitle( "MainWindow")
        self.admbutton.setText( "Admin")
        self.mbutton.setText( "Morning")
        self.ebutton.setText( "Evening")
        self.nbutton.setText( "Night")
        self.pushButton.setText( "Print")
        self.logoutbutton.setText( "Logout")
        self.quitbutton.setText( "Quit")
        self.menu1.setTitle( "File")
        self.actionLogout.setText( "Logout")
        self.actionExit.setText( "Exit")
        self.actionEdit_Host.setText( "Edit Host")
        self.actionExport.setText( "Export")


    def do(self):
        db1=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT FLAG FROM USERLOG WHERE `DATE`='%s' AND SHIFT='%s' AND UNAME='%s'"%(p,u1.shift,u1.name))
        data = cursor1.fetchall()
        k=cursor1.rowcount
        t=0
        for row in data:
            if row[0]=="1":
                t=1
        if t==0 and u1.admin!="YES":
            self.uip = Shiftdial()
            self.uip.show()
            self.close()
        else:
            self.ui = Ui_Shift()
            self.ui.setupUi(MainWindow)
            MainWindow.show()

    def adm(self):
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def logout(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def prntt(self):
        self.ui = Ui_Printwindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

class MainWindow_1(QtGui.QMainWindow, Ui_MainWindow_1):

    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 1, 1, 1)
        self.uedit_2 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.uedit_2, 2, 1, 1, 1)
        self.pedit_2 = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.pedit_2, 4, 1, 1, 1)
        self.plabel_2 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.plabel_2, 3, 1, 1, 1)
        self.quitbutton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.quitbutton_2, 7, 1, 1, 1)
        self.loginbutton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.loginbutton_2, 6, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 1)
        self.ulabel_2 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.ulabel_2, 1, 1, 1, 1)
        self.pedit_2.setEchoMode(QtGui.QLineEdit.Password)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.loginbutton_2.clicked.connect(self.check)
        self.pedit_2.returnPressed.connect(self.check)
        self.quitbutton_2.clicked.connect(MainWindow.close)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle( "Login")
        self.plabel_2.setText( "Enter Password")
        self.quitbutton_2.setText( "Quit")
        self.loginbutton_2.setText( "Login")
        self.ulabel_2.setText( "Enter Username")

    def check(self):
        uname = self.uedit_2.text()
        password = self.pedit_2.text()
        cursor1.execute("SELECT * FROM USER")
        data = cursor1.fetchall()
        n = 0
        for row in data:
            if uname == row[0] and password != row[1]:
                n = 2
            elif uname != row[0]:
                n = 3
            elif uname == row[0] and password == row[1]:
                n = 1
                break
        if n == 1:
            self.uip = Dialog(n)
            self.uip.show()
            u1.username = uname
            u1.getdata()
            db2=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
            cursor2 = db2.cursor()
            cursor2.execute(" INSERT INTO USERLOG(UNAME,`DATE`,`TIME`,SHIFT)VALUES('%s','%s','%s','%s')" % (u1.name, p, t, u1.shift))
            db2.commit()
            self.ui1 = Ui_MainWindow_1()
            self.ui1.setupUi(MainWindow)
            MainWindow.show()
        elif n == 2:
            self.uip = Dialog(n)
            self.uip.show()
        elif n == 3:
            self.uip = Dialog(n)
            self.uip.show()

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        MainWindow.setWindowState(QtCore.Qt.WindowMaximized)
        self.setupUi(self)

class Ui_Shiftdial(object):

    def setupUi(self, Shiftdial):
        Shiftdial.resize(320, 189)
        self.label = QtGui.QLabel(Shiftdial)
        self.label.setGeometry(QtCore.QRect(80, 70, 191, 20))
        self.pushButton = QtGui.QPushButton(Shiftdial)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 85, 28))
        self.pushButton_2 = QtGui.QPushButton(Shiftdial)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 140, 85, 28))
        self.retranslateUi(Shiftdial)
        QtCore.QMetaObject.connectSlotsByName(Shiftdial)
        self.pushButton.clicked.connect(self.yes)
        self.pushButton_2.clicked.connect(self.no)

    def retranslateUi(self, Shiftdial):
        Shiftdial.setWindowTitle( "Shift")
        self.label.setText( "Are You In Shift")
        self.pushButton.setText( "Yes")
        self.pushButton_2.setText( "No")

    def yes(self):
        db2=MySQLdb.Connect(host=host, port=port, user=userd, passwd=passwdd, db=dbb)
        cursor2 = db2.cursor()
        cursor2.execute("UPDATE project.USERLOG SET FLAG='1' WHERE UNAME='%s' AND DATE='%s' AND SHIFT='%s'" % (u1.name, p,u1.shift))
        db2.commit()
        self.ui = Ui_Shift()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

    def no(self):
        self.ui = Ui_Shift()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.close()

class Shiftdial(QtGui.QDialog, Ui_Shiftdial):

    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)
        self.setupUi(self)

if __name__ == "__main__":
    getdb()
    setdt()
    datecheck()
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
