from tkinter import *
from tkinter import ttk
import math

ndegs=12
cent=(110,110)
encols=('red','green','red','green')
data_all=[]
for j in range(0, 4):
    data_all.append(dict())


def save_deg_data():
    global ndegs
    dm=dict()
    dm[12]=30
    dm[8]=45
    dm[4]=90
    for i in range(1, ndegs+1):
      str_deg=str(i * dm[ndegs])
      for j in range(0, 4):
        data_all[j][str_deg]=degs_ent[j][i - 1].get()


def st30(*args):
    try:
       global ndegs
       save_deg_data()
       ndegs=12
       for i in range(1, ndegs+1):
         str_deg=str(i * 30)
         degs[i - 1].set(str_deg)
         for j in range(0,4):
          degs_ent[j][i - 1].config(state="normal")
          degs_ent[j][i - 1].delete(0, END)
          degs_ent[j][i - 1].insert(0,data_all[j].get(str_deg,0))

    except ValueError:
        pass
def st45(*args):
    try:
     global ndegs
     save_deg_data()
     ndegs=8
     for i in range(1, 13):
            degs[i - 1].set("")
            for j in range(0, 4):
                degs_ent[j][i-1].config(state="disabled")
     for i in range(1, 9):
                str_deg = str(i * 45)
                degs[i - 1].set(str_deg)
                for j in range(0, 4):
                    degs_ent[j][i - 1].config(state="normal")
                    degs_ent[j][i - 1].delete(0, END)
                    degs_ent[j][i - 1].insert(0,data_all[j].get(str_deg,0))
    except ValueError:
        pass
def st90(*args):
    try:
        global ndegs
        save_deg_data()
        ndegs=4
        for i in range(1, 13):
            degs[i - 1].set("")
            for j in range(0, 4):
                degs_ent[j][i - 1].config(state="disabled")
        for i in range(1, 5):
                str_deg = str(i * 90)
                degs[i - 1].set(str_deg)
                for j in range(0, 4):
                    degs_ent[j][i - 1].config(state="normal")
                    degs_ent[j][i - 1].delete(0, END)
                    degs_ent[j][i - 1].insert(0,data_all[j].get(str_deg,0))
    except ValueError:
        pass

def calc_left(*args):
    global ndegs
    try:
      leye = Canvas(mainframe, width=220, height=220)
      leye.grid(column=5, row=1, sticky=(W, E), columnspan=5, rowspan=5)
      leye.create_oval(10, 10, 210, 210)
      reye = Canvas(mainframe, width=220, height=220)
      reye.grid(column=10, row=1, sticky=(W, E), columnspan=5, rowspan=5)
      reye.create_oval(10, 10, 210, 210)
      for j in range(0, 4):
        s=0.0
        for i in range (0,ndegs-1):
            vi = int (degs_ent[j][i].get())
            vi1= int (degs_ent[j][i+1].get())
            ang_i=math.radians(float(degs[i].get()))
            ang_i1=math.radians(float(degs[i+1].get()))
            xi=math.cos(ang_i)*vi+cent[0]
            yi=math.sin(ang_i)*vi+cent[0]
            xi1=math.cos(ang_i1)*vi1+cent[0]
            yi1=math.sin(ang_i1)*vi1+cent[0]
            s=s+vi*vi1*math.sin(ang_i1-ang_i)/2.
            leye.create_line(cent[0],cent[0], math.cos(ang_i1)*100+cent[0], math.sin(ang_i1)*100+cent[0])
            reye.create_line(cent[0],cent[0], math.cos(ang_i1)*100+cent[0], math.sin(ang_i1)*100+cent[0])
            if(j<2):
             leye.create_line(xi,yi,xi1,yi1,fill=encols[j])
            else:
             reye.create_line(xi, yi, xi1, yi1,fill=encols[j])
        vi = int(degs_ent[j][0].get())
        vi1 = int(degs_ent[j][ndegs-1].get())
        ang_i = math.radians(float(degs[0].get()))
        ang_i1 = math.radians(float(degs[ndegs-1].get()))
        xi = math.cos(ang_i) * vi + cent[0]
        yi = math.sin(ang_i) * vi + cent[0]
        xi1 = math.cos(ang_i1) * vi1 + cent[0]
        yi1 = math.sin(ang_i1) * vi1 + cent[0]
        s = s + vi * vi1 * math.sin(math.radians(float(degs[1].get())) - math.radians(float(degs[0].get()))) / 2.
        leye.create_line(cent[0], cent[0], math.cos(ang_i) * 100 + cent[0], math.sin(ang_i) * 100 + cent[0])
        reye.create_line(cent[0], cent[0], math.cos(ang_i) * 100 + cent[0], math.sin(ang_i) * 100 + cent[0])
        leye.create_line(cent[0], cent[0], math.cos(ang_i1) * 100 + cent[0], math.sin(ang_i1) * 100 + cent[0])
        reye.create_line(cent[0], cent[0], math.cos(ang_i1) * 100 + cent[0], math.sin(ang_i1) * 100 + cent[0])
        if (j < 2):
            leye.create_line(xi, yi, xi1, yi1, fill=encols[j])
        else:
            reye.create_line(xi, yi, xi1, yi1, fill=encols[j])
        plosh[j].set(str(int(s)))
    except ValueError:
        pass

def  save_all(*args):
  nf=open('numb.dat')
  fnum=nf.read()
  nf.close()
  resf=open(fnum+'_'+str(ndegs)+'.txt','w')
  resf.write("#FIO : "+fio_entry.get()+"\n")
  fio_entry.delete(0,END)
  resf.write("#AGE : "+age_entry.get() + "\n")
  age_entry.delete(0,END)
  resf.write("#POL : " + pol_entry.get() + "\n")
  pol_entry.delete(0,END)
  resf.write("#TRUD: " + trud_entry.get() + "\n")
  trud_entry.delete(0,END)
  resf.write("#S: " + plosh[0].get()+ " "+plosh[1].get()+ " "+plosh[2].get()+ " "+plosh[3].get()+ "\n")
  for i in range(0,4):
   plosh[i].set('')
  resf.write("#Lmax/Rmax: " + lmax_entry.get() +' '+rmax_entry.get()+ "\n")
  lmax_entry.delete(0,END)
  rmax_entry.delete(0,END)
  resf.write(str(degs[ndegs-1].get()) + "   ")
  for j in range(0, 4):
      resf.write(str(degs_ent[j][ndegs-1].get()) + "    ")
  resf.write("\n")
  for i in range(0,ndegs):
      resf.write(str(degs[i].get())+ "   ")
      for j in range(0,4):
          resf.write(str(degs_ent[j][i].get())+ "    ")
          degs_ent[j][i].delete(0,END)
      resf.write("\n")
  resf.close()
  fname_saved.set('Saved as:'+fnum+'_'+str(ndegs)+'.txt')
  nf = open('numb.dat', 'w')
  nf.write(str(int(fnum) + 1))
  nf.close()

root = Tk()
root.title("EyeMeter")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

fio = StringVar()
age = StringVar()
rmax = StringVar()
lmax = StringVar()
pol = StringVar()
trud= StringVar()
meters = StringVar()
fname_saved = StringVar()
degs=[]
degs_ent=[]
plosh=[]
#degs_entr=[]
#degs_v=[]
#degs_vr=[]
tt= StringVar()
for i in range(0, 12):
    degs.append(StringVar())
for j in range(0,4):
 degs_ent.append([])
 plosh.append(StringVar())

#    degs_v.append(StringVar())
#    degs_vr.append(StringVar())

fio_entry = ttk.Entry(mainframe, width=20, textvariable=fio)
fio_entry.grid(column=2, row=1, sticky=(W, E), columnspan = 3)
ttk.Label(mainframe, text="ФИО").grid(column=1, row=1, sticky=W)

age_entry = ttk.Entry(mainframe, width=5, textvariable=age)
age_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Возраст").grid(column=1, row=2, sticky=W)

pol_entry = ttk.Entry(mainframe, width=5, textvariable=pol)
pol_entry.grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Пол").grid(column=1, row=3, sticky=W)

trud_entry = ttk.Entry(mainframe, width=20, textvariable=trud)
trud_entry.grid(column=2, row=4, sticky=(W, E), columnspan = 3)
ttk.Label(mainframe, text="Труд").grid(column=1, row=4, sticky=W)

#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
#ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text=" ШАГ ").grid(column=1, row=5, sticky=(W))
ttk.Button(mainframe, text="30", command=st30, width = 4).grid(column=2, row=5, sticky=W)
ttk.Button(mainframe, text="45", command=st45, width = 4).grid(column=3, row=5, sticky=W)
ttk.Button(mainframe, text="90", command=st90, width = 4).grid(column=4, row=5, sticky=W)
ttk.Label(mainframe, text=" Левый ").grid(column=2, row=6, sticky=(W,E), columnspan = 2)
ttk.Label(mainframe, text=" Правый ").grid(column=4, row=6, sticky=(W,E), columnspan = 2)

for i in range(1,13):
    ttk.Label(mainframe, textvariable=degs[i-1]).grid(column=1, row=6+i, sticky=W)
    degs[i - 1].set(str(i * 30))
for j in range(0,4):
    Label(mainframe, width=10, textvariable=plosh[j], bg=encols[j]).grid(column=6 + j*2, row=6, sticky=(W), columnspan = 2)
    for i in range(1, 13):
     degs_ent[j].append(Entry(mainframe,width = 4, bg=encols[j]))
     degs_ent[j][i - 1].grid(column=2+j, row=6+i, sticky=(W))

lmax_entry = ttk.Entry(mainframe, width=5, textvariable=lmax)
lmax_entry.grid(column=2, row=6+13, sticky=(W, E))
rmax_entry = ttk.Entry(mainframe, width=5, textvariable=rmax)
rmax_entry.grid(column=4, row=6+13, sticky=(W, E))
ttk.Label(mainframe, text="MAX:").grid(column=1, row=6 + 13, sticky=W)
#ttk.Label(mainframe, text="Возраст").grid(column=1, row=2, sticky=W)


leye =Canvas(mainframe,width=220, height=220)
leye.grid(column=5, row=1, sticky=(W, E), columnspan = 5,rowspan = 5)
leye.create_oval(10,10,210,210)
reye =Canvas(mainframe,width=220, height=220)
reye.grid(column=10, row=1, sticky=(W, E), columnspan = 5,rowspan = 5)
reye.create_oval(10,10,210,210)

ttk.Button(mainframe, text="Проверка", command=calc_left, width = 13).grid(column=8, row=7, sticky=W,columnspan = 3)
ttk.Button(mainframe, text="Сохранение", command=save_all, width = 13).grid(column=8, row=8, sticky=W,columnspan = 3)
ttk.Label(mainframe, textvariable=fname_saved,width=13).grid(column=8, row=9, sticky=(W,E), columnspan = 3)

ttk.Label(mainframe, text="лет").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

fio_entry.focus()
#root.bind('<Return>', calculate)

root.mainloop()