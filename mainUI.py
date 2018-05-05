'''This is the main user interface. It uses objects from backend files.
Names of some constants and methods are vague not to show anything confidential'''

import tkinter as tk, paramiko, backEnd, backEnd2, codecs, sys, os, time
from tkinter import ttk, filedialog, messagebox
LARGE_FONT = ("Verdana", 12)

def onvaioff2(metodi):
   remote.checkConnection()
   if remote.tila == 'on':
    metodi()
   else:
    messagebox.showinfo('Connection', 'Connection terminated')

#Load backend functionality
serverit = backEnd2.serverlist()
remote = backEnd.connection()
cliui = backEnd2.clientit()

def restart():
   python = sys.executable
   os.execl(python, python, * sys.argv)

#Method for updating remote list of remote servers
def lahremoteServerit():
   if 'Listaa ei löydy' in serverit.servertable2:
    print('Huono lista')
    return
   counter = 0
   while True:
    try:
     lahetettava = serverit.cryptaa()
     lahetettava = codecs.encode(lahetettava, 'hex')
     lahetettava = lahetettava.decode('utf-8')
     remote.openSSH('some ip', 'some password')
     komento = 'some command' % (lahetettava)
     a = remote.sshCommand(komento)
     remote.closeSSH()
     break
    except Exception as e:
     print(e)
     time.sleep(2)
     counter += 1
     if counter == 5:
        break

#Method of retrieving remote list of remote servers
def fetchServerit():
   b = 'Listaa ei löydy;x;x;x;x;x;x;x;x;x;x;x;x;x;x;x;End of line marker'
   try:
    remote.openSSH('some ip', 'some password')
    a = remote.sshCommand('some command')
    remote.closeSSH()
    a = bytes(a, encoding = 'utf8')
    a = codecs.decode(a, 'hex')
    a = serverit.avaa(a)
    if 'Anonymous' in a:
     return a
    else:
     remote.customer = 'Listaa ei löydy'
     return b
   except:
    remote.customer = 'Listaa ei löydy'
    return b

#Initialize server information
serverit.lookServers2(fetchServerit())

#Algorithm for frame rotations is taken from sentdex YouTube channel
class mainWindow(tk.Tk):
 def __init__(self, *args, **kwargs):
  tk.Tk.__init__(self, *args, **kwargs)
  tk.Tk.wm_title(self, "some title")

  container = tk.Frame(self)
  container.pack(side = 'top', fill = 'both', expand = True)
  container.grid_rowconfigure(0, weight = 1)
  container.grid_columnconfigure(0, weight = 1)
  self.frames = {}

  for F in (customreList, someDataControl, valinnat, lisaaServer, naytapw):
   frame = F(container, self)
   self.frames[F] = frame
   frame.grid(row = 0, column = 0, sticky = 'nsew')
  self.show_frame(customreList)

 def show_frame(self, cont):
  frame = self.frames[cont]
  frame.tkraise()

# Window for automated tasks after the connection is established
class valinnat(tk.Frame):
 def __init__(self, parent, controller):
  tk.Frame.__init__(self, parent)
  label = tk.Label(self, text='Toiminnot', font = LARGE_FONT)
  label.pack(pady = 10, padx = 10)
  def labelconfig():
     uusi = remote.customer.title() + ' ' + remote.versio.title() + ' ' + remote.trueversio
     label.configure(text = uusi)
     self.after(300, labelconfig)
  labelconfig()

  labelconfig()
  button6 = ttk.Button(self, text = 'Open Putty',  command = lambda: onvaioff2(remote.openPutty), width = 30)
  button6.pack()
  button1 = ttk.Button(self, text = 'Open cliui',  command = lambda: onvaioff2(avaacliui), width = 30)
  button1.pack()
  button2 = ttk.Button(self, text = 'Open x3',  command = lambda: onvaioff2(openx3), width = 30)
  button2.pack()
  button3 = ttk.Button(self, text = 'Device Listing', command = lambda: onvaioff2(remote.formDevList), width = 30)
  button3.pack()
  button4 = ttk.Button(self, text = 'Some data control', command = lambda: controller.show_frame(someDataControl), width = 30)
  button4.pack()

  def puttyy():
   remote.openPutty()

  button7 = ttk.Button(self, text = 'Service report', command = lambda: onvaioff2(remote.serverReport), width = 30)
  button7.pack()
  tyhjaa = tk.Label(self, text='').pack()
  button8 = ttk.Button(self, text = 'Show pw', command = lambda: naytaS(), width = 30)
  button8.pack()
  tyhjaa = tk.Label(self, text='').pack()
  tyhjaa = tk.Label(self, text='').pack()
  button5 = ttk.Button(self, text = 'Back', command = lambda: [remote.closeSSH(), controller.show_frame(customerList)], width = 30)
  button5.pack()
  def naytaS():
    remote.rotaatio = 'on'
    time.sleep(0.3)
    controller.show_frame(naytapw)

  def avaacliui():
     cliui.oikversio = remote.trueversio
     polku = cliui.haePolku() + '\\' + cliui.oikversio[:5]
     if not os.path.isdir(polku):
        eiloydy = 'Instruction for the case'
        messagebox.showinfo('Not found', eiloydy)
        return

     if cliui.oikversio[:5] not in cliui.cliversiot:
        eituettu = 'Not supported'
        messagebox.showinfo('support', 'no support')
        return

     remote.openPutty2()
     cliui.freePort = remote.freePort
     cliui.cliuser = serverit.servertable2[remote.customer][3]
     cliui.buildA
     c = 'start ' + cliui.startPath()
     os.system(c)

  def openx3():
     if remote.versio == 'x3':
        remote.openLatest()
        c = 'start "" https://localhost:%s/#/login' % (remote.freePort)
        os.system(c)
     else:
        messagebox.showinfo(remote.trueversio, 'Not x3')

# Window for adding data to the server or removing data. Adding from file or manually
class someDataControl(tk.Frame):
 def __init__(self, parent, controller):
  tk.Frame.__init__(self, parent)
  label = tk.Label(self, text='DataControl', font = LARGE_FONT)
  label.pack(pady = 10, padx = 10)
  button2 = ttk.Button(self, text = 'Show', command = lambda: onvaioff2(remote.tulostaXt), width = 30)
  button2.pack()
  button2 = ttk.Button(self, text = 'Transfer (.csv)', command = lambda: siirtotiedosto(), width = 30)
  button2.pack()
  def siirtotiedosto():
     tk.filename = filedialog.askopenfilename(initialdir = "/",title = "Valitse Xtiedosto",filetypes = (("Xtiedosto","*.csv"),("kaikki tiedostot","*.*")))
     try:
      remote.siirraXt(tk.filename)
     except UnicodeDecodeError:
      messagebox.showinfo('Huono tiedosto', 'Huono Xtiedosto')
      return
     except FileNotFoundError:
      print('File not found')
      return
     except:
      print('Unknown error')

  tyhjaa = tk.Label(self, text='').pack()
  XB = tk.Label(self, text='Xnro: ').pack()
  XR = tk.Entry(self, text = tk.StringVar(self, value=''))
  XR.pack()
  XL = tk.Label(self, text='X: ').pack()
  Xrivi = tk.Entry(self, text = tk.StringVar(self, value=''))
  Xrivi.pack()
  button2 = ttk.Button(self, text = 'Transfer previous', command = lambda: siirraEdMainittu(), width = 30)
  button2.pack()
  def siirraEdMainittu():
   try:
    data = int(tunrivi.get())
    X = int(Xrivi.get())
   except:
    messagebox.showinfo('No good', 'bad X')
    return
   try:
    remote.transfer2(tunniste, X)
   except Exception as e:
    print(e)
  button7 = ttk.Button(self, text = 'Remove previous', command = lambda: poistaEdMainittu(), width = 30)
  button7.pack()
  def poistaEdMainittu():
   try:
    Y = int(tunrivi.get())
    X = int(Xrivi.get())
   except:
    messagebox.showinfo('not ok', 'not ok')
    return
   try:
    remote.deleteSomething(tunniste, X)
   except Exception as e:
    print(e)
  tyhjaa = tk.Label(self, text='').pack()
  tyhjaa = tk.Label(self, text='').pack()
  tyhjaa = tk.Label(self, text='').pack()
  button5 = ttk.Button(self, text = 'Back to selection',  command = lambda: controller.show_frame(valinnat), width = 30)
  button5.pack()

# The main Window presenting a list of customers
class customreList(tk.Frame):
 def __init__(self, parent, controller):
  tk.Frame.__init__(self, parent)
  label = tk.Label(self, text='SSH-connections', font = LARGE_FONT)
  label.grid(row = 0, column=1)
  button3 = ttk.Button(self, text = 'Open SSH',  command = lambda: selector(), width = 15)
  button5 = ttk.Button(self, text = 'Add new',  command = lambda: controller.show_frame(lisaaServer), width = 15)
  button6 = ttk.Button(self, text = 'Delete',  command = lambda: poistaja(), width = 15)
  button1 = ttk.Button(self, text = 'Show pw',  command = lambda: selector2(), width = 15)

  lb = tk.Listbox(self, height = 22, width = 40)
  for key in serverit.namesAlphabet():
      lb.insert(0, key)
  yscroll = tk.Scrollbar(self, orient='vertical')
  yscroll.config(command=lb.yview)
  lb.grid(row=0, column=1, rowspan=2, sticky='nsew')
  yscroll.grid(row=0, column=1, rowspan=2, sticky='ens')
  button3.grid(row=14,column=1, sticky='w')
  button1.grid(row=15,column=1, sticky='w')
  button5.grid(row=14,column=1, sticky='e')
  button6.grid(row=15,column=1, sticky='e')
  lb.bind('<Double-1>', lambda x: button3.invoke())

  def selector():
   try:
    value = str(lb.get(lb.curselection()))
    remote.cliauki = 'on'
    remote.customer = value
    remote.openSSH(str(serverit.servertable2[value][0]),str(serverit.servertable2[value][1]))
    if remote.tila == 'on':
     controller.show_frame(valinnat)
    else:
     messagebox.showinfo('connection', 'Does not open')
   except:
     messagebox.showinfo('Selection', 'Select something')

  def poistaja():
     serverit.lookServers2(fetchServerit())
     try:
      value = str(lb.get(lb.curselection()))
      serverit.removeServer(value)
     except:
      messagebox.showinfo('Selection', 'Select something')
      return
     if value:
       lahremoteServerit()
       restart()

  def selector2():
    try:
     remote.rotaatio = 'on'
     value = str(lb.get(lb.curselection()))
     remote.customer = value
     time.sleep(0.3)
     controller.show_frame(naytapw)
    except:
     messagebox.showinfo('Selection', 'Select something')

#Window for adding new server to the list
class lisaaServer(tk.Frame):
 def __init__(self, parent, controller):
  tk.Frame.__init__(self, parent)
  pituus = 26
  label = tk.Label(self, text='New connection:')
  label.grid(row=0, column=0, columnspan = 2, sticky='w')

  label1 = tk.Label(self, text='customer:').grid(row=1, column=0, sticky='w')
  entry1 = tk.Entry(self, text = tk.StringVar(self, value=''), width = pituus)
  entry1.grid(row=1, column=1, sticky='w')
  label2 = tk.Label(self, text='IP:').grid(row=2, column=0, sticky='w')
  entry2 = tk.Entry(self, text = tk.StringVar(self, value=''), width = pituus)
  entry2.grid(row=2, column=1, sticky='w')
  label3 = tk.Label(self, text='usr pw:').grid(row=3, column=0, sticky='w')
  entry3 = tk.Entry(self, text = tk.StringVar(self, value=''), width = pituus)
  entry3.grid(row=3, column=1, sticky='w')
  label4 = tk.Label(self, text='usr2 pw:').grid(row=4, column=0, sticky='w')
  entry4 = tk.Entry(self, text = tk.StringVar(self, value=''), width = pituus)
  entry4.grid(row=4, column=1, sticky='w')
  label5 = tk.Label(self, text='usr3:').grid(row=5, column=0, sticky='w')
  entry5 = tk.Entry(self, text = tk.StringVar(self, value=''), width = pituus)
  entry5.grid(row=5, column=1, sticky='w')
  label6 = tk.Label(self, text='usr3 pw:').grid(row=6, column=0, sticky='w')
  entry6 = tk.Entry(self, text = tk.StringVar(self, value=''), width = pituus)
  entry6.grid(row=6, column=1, sticky='w')
  label7 = tk.Label(self, text='usr4:').grid(row=7, column=0, sticky='w')
  entry7 = tk.Entry(self, text = tk.StringVar(self, value=''), width = pituus)
  entry7.grid(row=7, column=1, sticky='w')
  label8 = tk.Label(self, text='usr4pw:').grid(row=8, column=0, sticky='w')
  entry8 = tk.Entry(self, text = tk.StringVar(self, value=''), width = pituus)
  entry8.grid(row=8, column=1, sticky='w')
  label9 = tk.Label(self, text='vpn:').grid(row=9, column=0, sticky='w')
  entry9 = tk.Entry(self, text = tk.StringVar(self, value=''), width = pituus)
  entry9.grid(row=9, column=1, sticky='w')
  label10 = tk.Label(self, text='vpn data:').grid(row=10, column=0, sticky='w')
  entry10 = tk.Entry(self, text = tk.StringVar(self, value=''), width = pituus)
  entry10.grid(row=10, column=1, sticky='w')
  label11 = tk.Label(self, text='other info:').grid(row=11, column=0, sticky='w')
  Te = tk.Text(self, height=9, width=30)
  Te.grid(row = 12, column=0, columnspan=2)
  button1 = ttk.Button(self, text = 'Add', command = lambda: [lisataanServer(), lahremoteServerit(), restart()], width = 11)
  button1.grid(row=14, column=0, sticky='w')
  button2 = ttk.Button(self, text = 'Back', command = lambda: controller.show_frame(customreList), width = 11)
  button2.grid(row=14, column=1, sticky='e')
  def lisataanServer():
   if not entry1.get(): {entry1.insert(0, 'Ei_määritelty')}
   if not entry2.get(): {entry2.insert(0, 'Ei_määritelty')}
   if not entry3.get(): {entry3.insert(0, 'Ei_määritelty')}
   if not entry4.get(): {entry4.insert(0, 'Ei_määritelty')}
   if not entry5.get(): {entry5.insert(0, 'Ei_määritelty')}
   if not entry6.get(): {entry6.insert(0, 'Ei_määritelty')}
   if not entry7.get(): {entry7.insert(0, 'Ei_määritelty')}
   if not entry8.get(): {entry8.insert(0, 'Ei_määritelty')}
   if not entry9.get(): {entry9.insert(0, 'Ei_määritelty')}
   if not entry10.get(): {entry10.insert(0, 'Ei_määritelty')}
   if len(Te.get('1.0',tk.END)) == 0: {Te.insert('1.0', 'Ei_määritelty')}
   serverit.lookServers2(fetchServerit())
   serverit.lisaaServeri(entry1.get().title(), entry2.get(), entry3.get(), entry4.get(),
                         entry5.get(), entry6.get(), entry7.get(), entry8.get(), entry9.get(),
                         entry10.get(),Te.get('1.0',tk.END))

# Window for viewing the server information
class naytapw(tk.Frame):
 def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    T = tk.Text(self, height=24, width=300)
    T.pack()
    abc = serverit.showAlphabet(remote.customer)
    T.insert('1.0', abc)
    def updter():
      if remote.rotaatio == 'on':
       T.delete('1.0',tk.END)
       abc = serverit.showAlphabet(remote.customer)
       T.insert('1.0', abc)
       remote.rotaatio = 'off'
      else:
       pass
      self.after(300, updter)
    updter()
    button1 = ttk.Button(self, text = 'Back', command = lambda: mikalista(), width = 11)
    button1.pack()
    def mikalista():
       if remote.cliauki == 'off':
          controller.show_frame(customreList)
       if remote.cliauki == 'on':
          controller.show_frame(valinnat)
    def tulosta():
       serverit.tulosta(remote.customer)

app = mainWindow()
app.geometry("325x530")
app.mainloop()
