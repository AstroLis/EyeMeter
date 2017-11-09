import tkinter as tk
from tkinter import *
from tkinter import ttk
import math

class MeterWindow(tk.Toplevel):
    def save_deg_data(self):
        dm=dict()
        dm[12]=30
        dm[8]=45
        dm[4]=90
        for i in range(1, self.ndegs+1):
          str_deg=str(i * dm[self.ndegs])
          for j in range(0, 4):
            self.data_all[j][str_deg]=self.degs_ent[j][i - 1].get()


    def st30(self,*args):
        try:
           self.save_deg_data()
           self.ndegs=12
           for i in range(1, self.ndegs+1):
             str_deg=str(i * 30)
             self.degs[i - 1].set(str_deg)
             for j in range(0,4):
              self.degs_ent[j][i - 1].config(state="normal")
              self.degs_ent[j][i - 1].delete(0, END)
              self.degs_ent[j][i - 1].insert(0,self.data_all[j].get(str_deg,0))

        except ValueError:
            pass
    def st45(self,*args):
        try:
         self.save_deg_data()
         self.ndegs=8
         for i in range(1, 13):
                self.degs[i - 1].set("")
                for j in range(0, 4):
                    self.degs_ent[j][i-1].config(state="disabled")
         for i in range(1, 9):
                    str_deg = str(i * 45)
                    self.degs[i - 1].set(str_deg)
                    for j in range(0, 4):
                        self.degs_ent[j][i - 1].config(state="normal")
                        self.degs_ent[j][i - 1].delete(0, END)
                        self.degs_ent[j][i - 1].insert(0,self.data_all[j].get(str_deg,0))
        except ValueError:
            pass
    def st90(self,*args):
        try:
            self.save_deg_data()
            self.ndegs=4
            for i in range(1, 13):
                self.degs[i - 1].set("")
                for j in range(0, 4):
                    self.degs_ent[j][i - 1].config(state="disabled")
            for i in range(1, 5):
                    str_deg = str(i * 90)
                    self.degs[i - 1].set(str_deg)
                    for j in range(0, 4):
                        self.degs_ent[j][i - 1].config(state="normal")
                        self.degs_ent[j][i - 1].delete(0, END)
                        self.degs_ent[j][i - 1].insert(0,self.data_all[j].get(str_deg,0))
        except ValueError:
            pass

    def calc_left(self,*args):
        cent = (110, 110)
        try:
          leye = Canvas(self, width=220, height=220)
          leye.grid(column=5, row=1, sticky=(W, E), columnspan=5, rowspan=5)
          leye.create_oval(10, 10, 210, 210)
          reye = Canvas(self, width=220, height=220)
          reye.grid(column=10, row=1, sticky=(W, E), columnspan=5, rowspan=5)
          reye.create_oval(10, 10, 210, 210)
          for j in range(0, 4):
            s=0.0
            for i in range (0,self.ndegs-1):
                vi = int (self.degs_ent[j][i].get())
                vi1= int (self.degs_ent[j][i+1].get())
                ang_i=math.radians(float(self.degs[i].get()))
                ang_i1=math.radians(float(self.degs[i+1].get()))
                xi=math.cos(ang_i)*vi+cent[0]
                yi=-math.sin(ang_i)*vi+cent[0]
                xi1=math.cos(ang_i1)*vi1+cent[0]
                yi1=-math.sin(ang_i1)*vi1+cent[0]
                s=s+vi*vi1*math.sin(ang_i1-ang_i)/2.
                leye.create_line(cent[0],cent[0], math.cos(ang_i1)*100+cent[0], -math.sin(ang_i1)*100+cent[0])
                reye.create_line(cent[0],cent[0], math.cos(ang_i1)*100+cent[0], -math.sin(ang_i1)*100+cent[0])
                if(j<2):
                 leye.create_line(xi,yi,xi1,yi1,fill=self.encols[j])
                else:
                 reye.create_line(xi, yi, xi1, yi1,fill=self.encols[j])
            vi = int(self.degs_ent[j][0].get())
            vi1 = int(self.degs_ent[j][self.ndegs-1].get())
            ang_i = math.radians(float(self.degs[0].get()))
            ang_i1 = math.radians(float(self.degs[self.ndegs-1].get()))
            xi = math.cos(ang_i) * vi + cent[0]
            yi = -math.sin(ang_i) * vi + cent[0]
            xi1 = math.cos(ang_i1) * vi1 + cent[0]
            yi1 = -math.sin(ang_i1) * vi1 + cent[0]
            s = s + vi * vi1 * math.sin(math.radians(float(self.degs[1].get())) - math.radians(float(self.degs[0].get()))) / 2.
            leye.create_line(cent[0], cent[0], math.cos(ang_i) * 100 + cent[0], -math.sin(ang_i) * 100 + cent[0])
            reye.create_line(cent[0], cent[0], math.cos(ang_i) * 100 + cent[0], -math.sin(ang_i) * 100 + cent[0])
            leye.create_line(cent[0], cent[0], math.cos(ang_i1) * 100 + cent[0], -math.sin(ang_i1) * 100 + cent[0])
            reye.create_line(cent[0], cent[0], math.cos(ang_i1) * 100 + cent[0], -math.sin(ang_i1) * 100 + cent[0])
            if (j < 2):
                leye.create_line(xi, yi, xi1, yi1, fill=self.encols[j])
            else:
                reye.create_line(xi, yi, xi1, yi1, fill=self.encols[j])
            self.plosh[j].set(str(int(s)))
        except ValueError:
            pass

    def  save_all(self,*args):
      nf=open('numb.dat')
      fnum=nf.read()
      nf.close()
      resf=open(fnum+'_'+str(self.ndegs)+'.txt','w')
      resf.write("#FIO : "+self.fio_entry.get()+"\n")
      self.fio_entry.delete(0,END)
      resf.write("#AGE : "+self.age_entry.get() + "\n")
      self.age_entry.delete(0,END)
      resf.write("#POL : " + self.pol_entry.get() + "\n")
      self.pol_entry.delete(0,END)
      resf.write("#TRUD: " + self.trud_entry.get() + "\n")
      self.trud_entry.delete(0,END)
      resf.write("#S: " + self.plosh[0].get()+ " "+self.plosh[1].get()+ " "+self.plosh[2].get()+ " "+self.plosh[3].get()+ "\n")
      for i in range(0,4):
          self.plosh[i].set('')
      resf.write("#Lmax/Rmax: " + self.lmax_entry.get() +' '+self.rmax_entry.get()+ "\n")
      self.lmax_entry.delete(0,END)
      self.rmax_entry.delete(0,END)
      resf.write(str(self.degs[self.ndegs-1].get()) + "   ")
      for j in range(0, 4):
          resf.write(str(self.degs_ent[j][self.ndegs-1].get()) + "    ")
      resf.write("\n")
      for i in range(0,self.ndegs):
          resf.write(str(self.degs[i].get())+ "   ")
          for j in range(0,4):
              resf.write(str(self.degs_ent[j][i].get())+ "    ")
              self.degs_ent[j][i].delete(0,END)
          resf.write("\n")
      resf.close()
      self.fname_saved.set('Saved as:'+fnum+'_'+str(self.ndegs)+'.txt')
      nf = open('numb.dat', 'w')
      nf.write(str(int(fnum) + 1))
      nf.close()
    def __init__(self, *args, **kwargs):
        self.ndegs = 12
        self.encols = ('red', 'green', 'red', 'green')
        self.data_all = []
        for j in range(0, 4):
            self.data_all.append(dict())
        tk.Toplevel.__init__(self, *args, **kwargs)

        #mainframe = tk.Toplevel(root, padding="3 3 12 12")
        mainframe = self
        #mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        self.fio = StringVar()
        self.age = StringVar()
        self.rmax = StringVar()
        self.lmax = StringVar()
        self.pol = StringVar()
        self.trud= StringVar()
        self.fname_saved = StringVar()
        self.degs=[]
        self.degs_ent=[]
        self.plosh=[]
        for i in range(0, 12):
            self.degs.append(StringVar())
        for j in range(0,4):
         self.degs_ent.append([])
         self.plosh.append(StringVar())

        #    degs_v.append(StringVar())
        #    degs_vr.append(StringVar())

        self.fio_entry = ttk.Entry(mainframe, width=20, textvariable=self.fio)
        self.fio_entry.grid(column=2, row=1, sticky=(W, E), columnspan = 3)
        ttk.Label(mainframe, text="ФИО").grid(column=1, row=1, sticky=W)

        self.age_entry = ttk.Entry(mainframe, width=5, textvariable=self.age)
        self.age_entry.grid(column=2, row=2, sticky=(W, E))
        ttk.Label(mainframe, text="Возраст").grid(column=1, row=2, sticky=W)

        self.pol_entry = ttk.Entry(mainframe, width=5, textvariable=self.pol)
        self.pol_entry.grid(column=2, row=3, sticky=(W, E))
        ttk.Label(mainframe, text="Пол").grid(column=1, row=3, sticky=W)

        self.trud_entry = ttk.Entry(mainframe, width=20, textvariable=self.trud)
        self.trud_entry.grid(column=2, row=4, sticky=(W, E), columnspan = 3)
        ttk.Label(mainframe, text="Труд").grid(column=1, row=4, sticky=W)

        #ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
        #ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text=" ШАГ ").grid(column=1, row=5, sticky=(W))
        ttk.Button(mainframe, text="30", command=self.st30, width = 4).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text="45", command=self.st45, width = 4).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text="90", command=self.st90, width = 4).grid(column=4, row=5, sticky=W)
        ttk.Label(mainframe, text=" Левый ").grid(column=2, row=6, sticky=(W,E), columnspan = 2)
        ttk.Label(mainframe, text=" Правый ").grid(column=4, row=6, sticky=(W,E), columnspan = 2)

        for i in range(1,13):
            ttk.Label(mainframe, textvariable=self.degs[i-1]).grid(column=1, row=6+i, sticky=W)
            self.degs[i - 1].set(str(i * 30))
        for j in range(0,4):
            Label(mainframe, width=10, textvariable=self.plosh[j], bg=self.encols[j]).grid(column=6 + j*2, row=6, sticky=(W), columnspan = 2)
            for i in range(1, 13):
             self.degs_ent[j].append(Entry(mainframe,width = 4, bg=self.encols[j]))
             self.degs_ent[j][i - 1].grid(column=2+j, row=6+i, sticky=(W))

        self.lmax_entry = ttk.Entry(mainframe, width=5, textvariable=self.lmax)
        self.lmax_entry.grid(column=2, row=6+13, sticky=(W, E))
        self.rmax_entry = ttk.Entry(mainframe, width=5, textvariable=self.rmax)
        self.rmax_entry.grid(column=4, row=6+13, sticky=(W, E))
        ttk.Label(mainframe, text="MAX:").grid(column=1, row=6 + 13, sticky=W)
        #ttk.Label(mainframe, text="Возраст").grid(column=1, row=2, sticky=W)


        leye =Canvas(mainframe,width=220, height=220)
        leye.grid(column=5, row=1, sticky=(W, E), columnspan = 5,rowspan = 5)
        leye.create_oval(10,10,210,210)
        reye =Canvas(mainframe,width=220, height=220)
        reye.grid(column=10, row=1, sticky=(W, E), columnspan = 5,rowspan = 5)
        reye.create_oval(10,10,210,210)

        ttk.Button(mainframe, text="Проверка", command=self.calc_left, width = 13).grid(column=8, row=7, sticky=W,columnspan = 3)
        ttk.Button(mainframe, text="Сохранение", command=self.save_all, width = 13).grid(column=8, row=8, sticky=W,columnspan = 3)
        ttk.Label(mainframe, textvariable=self.fname_saved,width=13).grid(column=8, row=9, sticky=(W,E), columnspan = 3)

        ttk.Label(mainframe, text="лет").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        self.fio_entry.focus()
        #root.bind('<Return>', calculate)

        #root.mainloop()



class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Create new window",
                                command=self.create_window)
        self.button.pack(side="top")

    def create_window(self):
        self.counter += 1
        t = MeterWindow(self)
        #t.wm_title("Window #%s" % self.counter)
        #l = tk.Label(t, text="This is window #%s" % self.counter)
        #l.pack(side="top", fill="both", expand=True, padx=600, pady=600)

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()