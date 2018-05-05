''' This is a backend class.
    I had to leave out exact database commands and use some vague names for variables and methods to make sure no confidential information is present'''

import socket, psutil, paramiko, warnings, listing, backEnd2, sys, re, os, time, datetime, string, openpyxl, pysftp, paramiko291monkeypatch
from contextlib import closing

# Class for establishing SSH connections and running tasks through established connections
class connection:
 def __init__(self, *args, **kwargs):
  self.versio = '0'
  self.trueversio = '0'
  self.kvalitiedosto = 'X_valitiedosto' + '.tmp'
  self.tila = 'off'
  self.tyhjaa = '101010101'
  self.vapaaportti = 1234
  self.rotaatio = 'off'
  warnings.simplefilter("ignore")
  self.customer = 'Anonymous'
  self.cliauki = 'off'

# Method for opening SSH session
 def openSSH(self, IP, PW):
   self.IP = IP
   self.PW = PW
   self.ssh = paramiko.SSHClient()
   self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

   try:
    self.ssh.connect(self.IP, username='user', password=self.PW, timeout = 8)
    self.tila = 'on'
   except Exception as e:
    print('Connection does not open')
    time.sleep(2)
    self.tila = 'off'
   if self.tila == 'on':
    self.versio = self.checkVersio()
    self.trueversio = self.trueVersio()
   if self.versio == '0' and self.tila == 'on':
    print('Unknown version')
    self.tila = 'off'
    self.closeSSH()

# Method for closing SSH session
 def closeSSH(self):
  try:
   self.ssh.close()
   self.tila = 'on'
   self.cliauki = 'off'
  except:
   self.checkConnection()

# Method for running SSH command
 def sshCommand(self, komento):
    stdin,stdout,stderr = self.ssh.exec_command(komento)
    while stdout.channel.recv_ready():
     pass
    tulos = ''
    try:
     for item in stdout.readlines():
         tulos += str(item, 'utf-8')
     return tulos.strip()
    except:
     for item in stdout.readlines():
         tulos += str(item)
     return tulos.strip()

 def sshCommandNoUTF(self, komento):
   stdin,stdout,stderr = self.ssh.exec_command(komento)
   while stdout.channel.recv_ready():
    pass
   return stdout.readlines(), stderr.readlines()

# Method for checking that connection is open
 def checkConnection(self):
   try:
    stdin,stdout,stderr = self.ssh.exec_command('whoami')
   except Exception as e:
    print ('Connection broken')
    self.tila = 'off'

 def checkConnection2(self):
   try:
    stdin,stdout,stderr = self.ssh.exec_command('whoami')
   except:
    pass

# Method for checking server version
 def checkVersion(self):
   xVersion = "0"
   x1Versiontesti = "'secret command'"
   x1Versiontesti = self.sshCommand(x1Versiontesti)
   if len(x1Versiontesti) > 1:
    xVersion = 'x1'
   x2Versiontesti = "'secret command'"
   x2Versiontesti = self.sshCommand(x2Versiontesti)
   if len(x2Versiontesti) > 1:
    xVersion = 'x2'
   x3Versiontesti = 'secret command'"
   x3Versiontesti = self.sshCommand(x3Versiontesti)
   if len(x3Versiontesti) > 1:
    xVersion = 'x3'
   return xVersion

 def trueVersio(self):
   trueversio = 'secret command'"
   regexp = re.compile(r'[q]\d.+')
   trueversio = self.sshCommand(trueversio)
   trueversio = regexp.findall(trueversio)
   if trueversio:
    return trueversio[0]
   else:
    return 'Unknown'

# Method for opening putty.exe with portforwarding
 def openPutty(self):
  if self.versio == 'x3':
   portti = 5678
   portti2 = 1234
   c = 'start putty.exe -ssh userX@%s -L %s:localhost:%s -L %s:localhost:%s -pw %s' % (self.IP, portti, portti, portti2, portti2, self.PW)
   os.system(c)
  elif self.versio == 'x2':
   portti = 1234
   c = 'start putty.exe -ssh userX@%s -L %s:localhost:%s -pw %s' % (self.IP, portti, portti, self.PW)
   os.system(c)
  else:
   portti = 91011
   c = 'start putty.exe -ssh userX@%s -L %s:localhost:%s -pw %s' % (self.IP, portti, portti, self.PW)
   os.system(c)

 def openPutty2(self):
   if self.versio == 'x3' or self.versio == 'x2':
    etaportti = 1234
   else:
    etaportti = 91011
   self.freePort()
   c = 'start /min putty.exe -N -ssh userX@%s -L %s:localhost:%s -pw %s' % (self.IP, self.vapaaportti, etaportti, self.PW)
   os.system(c)

 def openLatest(self):
   etaportti = 5678
   self.freePort()
   c = 'start /min putty.exe -N -ssh userX@%s -L %s:localhost:%s -pw %s' % (self.IP, self.vapaaportti, etaportti, self.PW)
   os.system(c)

# Get a list of all free local ports
 def check(self, portti):
  tarkistettava = 'port=' + str(portti)
  porttilista = psutil.net_connections()
  for item in porttilista:
   for item2 in item:
    if tarkistettava in str(item2):
     return True
  return False

# Find the next unused local port
 def freePort(self):
    while(True):
     if self.check(self.vapaaportti):
      self.vapaaportti += 1
     else:
      break

# Method for sending a file to the server
 def sendFile(self, file):
  cnopts = pysftp.CnOpts()
  cnopts.hostkeys = None
  c = pysftp.Connection(host=self.IP, username='userX', password=self.PW, cnopts=cnopts)
  kohde = 'path' + file
  c.put(file, kohde)
  c.close()

# Method for receiving a file from the server
 def fetchFile(self, file):
  cnopts = pysftp.CnOpts()
  cnopts.hostkeys = None
  c = pysftp.Connection(host=self.IP, username='userX', password=self.PW, cnopts=cnopts)
  lahde = 'path' + file
  c.get(lahde, file)
  command = 'rm %s' % (lahde)
  stdin,stdout,stderr = self.ssh.exec_command(command)
  c.close()

# Method for opening certain data in excel
 def tulostaXt(self):
  ajettavakomento = 'secret command'
  if self.versio == 'x3':
   c = 'base -D databaseX -e %s > /path/%s' % (ajettavakomento, self.kvalitiedosto)
  else:
   c = 'base -e %s > /path/%s' % (ajettavakomento, self.kvalitiedosto)
  self.sshCommand(c)
  while(True):
   try:
    self.fetchFile(self.kvalitiedosto)
    os.system('start excel.exe %s' % self.kvalitiedosto)
    break
   except:
    print('close file')

# Method for inserting data to the database
 def siirraXt(self, file):
  errortable = []
  regexp = re.compile(r'\d+[o]\d+')
  f = open(file, 'r')

  for line in f.readlines():
   if len(line) > 2:
    line = line.strip()
    hyvaline = regexp.findall(line)
    try:
     hyvaline = hyvaline[0].split(';')
    except Exception as e:
     errortable.append(e)
     continue
    if self.versio == 'x1' or self.versio == 'x2':
     c = 'secret command' % (hyvaline[0], hyvaline[1])
    else:
     c = 'secret command (%s, %s, %s, %s, \'Value\')\'' % (hyvaline[0], hyvaline[0], hyvaline[1], '\"valueX\"')
    output, errors = self.sshCommandNoUTF(c)
    if errors:
        print(hyvaline[0] + ' ' + hyvaline[1] + ' ' + 'error')
        errortable.append(errors)
    else:
        print(hyvaline[0] + ' ' + hyvaline[1] + ' ' + 'success')
  f.close()
  if errortable:
      try:
          f = open('errors.txt', 'a')
      except:
          f = open('errors.txt', 'w')
      f.write(self.IP + '\n')
      time = datetime.datetime.now()
      time = str(time)
      f.write(time + '\n')
      f.write('\n' + 'VIRHEET:' + '\n\n')
      for item in errortable:
        f.write(str(item) + '\n')
      f.write('\n')
      f.close()
      print('\nCheck errors from: errors.txt')
  print('\nCompleted')

# Method2 for inserting data
 def transfer2(self, XX, YY):
    #This is very similar to the previous method so I just mention it exists
    pass

# Method for deleting from the database
 def deleteSomething(self, ZZ, LL):
    if self.versio == 'x1' or self.versio == 'x2':
     c = 'secret command' % (ZZ, LL)
    else:
     c = 'secret command' % (ZZ, LL)
    output, errors = self.sshCommandNoUTF(c)
    if errors:
      print('some error')
      print('errors in errors.txt')
      try:
          f = open('errors.txt', 'a')
      except:
          f = open('errors.txt', 'w')
      f.write(self.IP + '\n')
      time = datetime.datetime.now()
      time = str(time)
      f.write(time + '\n')
      f.write('\n' + 'errors:' + '\n\n' + str(errors[0]))
      f.write('\n\n')
      f.close()
    else:
      print('What was removed')

# Method for creating a device listing
 def formDevList(self):
  devicetypes = {'\tkey\t':'\tvalue\t'} #Dictionary for modifying the final presentation of the data}
  if self.versio == 'x3':
      listacommand = '\'secret command\''
      c = 'command' % (listacommand)
  elif self.versio == 'x2':
      listacommand = '\'secret command\''
      c = 'command' % (listacommand)
  else:
      self.sendFile('x1devlist.asc')
      c = 'command'
  self.sshCommand(c)
  while(True):
   try:
      open('devlist.xlxs', 'w').close()
      while (os.path.getsize('devlist.xlxs') < 1):
       time.sleep(0.1)
       self.fetchFile('devlist.xlxs')
       if self.versio == 'database' or self.versio == 'x2':
           f = open('devlist.xlxs', 'r')
           a = f.read()
           f.close()
           for key in devicetypes:
            a = a.replace(key, devicetypes[key])
           f = open('devlist.xlxs', 'w')
           f.write(a)
           f.close()
      os.system('start excel.exe devlist.xlxs')
      break
   except:
       print('Close Excel first')
       time.sleep(0.5)

# Method for collecting data from the Server
 def serverReport(self):
    d = []
    tulostettavat = []
 ########### Fetch the data (try three times max) #######################
    def yritaKolmesti(komento):
        laskuri = 0
        while laskuri < 3:
         X = self.sshCommand(komento)
         if X:
          return X
          break
         else:
          time.sleep(1)
          laskuri += 1
        return self.tyhjaa

    for item in backEnd2.commond:
        d.append(yritaKolmesti(item))

    if self.versio == 'x1':
        for item in backEnd2.databased:
            d.append(yritaKolmesti(item))

    elif self.versio == 'x2':
        for item in backEnd2.x2d:
            d.append(yritaKolmesti(item))
    else:
        for item in backEnd2.x1d:
            d.append(yritaKolmesti(item))

 ############ Get information from the data #######################
    data1=''
    if int(d[8]) > 1:
        data1 = 'data1=' + d[8]
    data2 = ''
    if int(d[1]) > 1 and int(d[9]) > 1:
        data2 = 'data2=' + d[9]
    data3 = ''
    if int(d[10]) > 1 and int(d[11]) > 1:
        data3 = 'data3=' + d[10]
    data4 = ''
    if 'some string' in d[6]:
        data4 = 'data4 käytössä'
    data5 = ''
    if 'some string' in d[6]:
        data5 = 'm käytössä'
        data1WM = data1+' '+data3+' '+data2+' '+data4+' '+data5

    data6 = 'Ei'
    if int(d[3]) > 1 and int(d[13]) > 1:
        data6 = 'data6=' + d[13]

    data7 = 'Ei'
    if int(d[2]) > 1 and int(d[12]) > 1:
        data7 = 'data7=' + d[12]
    if int(d[2]) == 0 and int(d[12]) > 1:
        data7 = 'EI, mutta poikkeus: ' + d[12]

    Xdata2 = 'Ei'
    if len(d[0]) > 2:
        Xdata2 = 'Käytössä'

    data9 = 'Ei'
    if 'some string' in d[6] and int(d[4]) > 1:
        data9 = 'Käytössä'

    data10 = d[14]

    Vdata2 = 'data'
    if 'some string' in d[5]:
        Vdata2 = 'data'

    regexp = re.compile(r'\A[A-Ba-b]{2}.+\d{5}')
    data12 = regexp.findall(d[7])
    try:
     data12 = data12[0]
    except:
     data12 = d[7]
    data2K = data12


    data14  = 'Ei'
    if 'some string' in d[6] or 'some string 2' in d[6]:
        data14 = 'Käytössä'

 ######## Handling transfers ##########################

    if d[0] == self.tyhjaa:
      data15 = 'Ei'
    else:
      servercollections, virheet = self.sshCommandNoUTF('secret command')
      data15 = listing.keraysKatalogi(servercollections, d[0])


 ######### Print to Excel document #######################
    ekarivi = 'Column header1\theader2\t' #First row in excel / column headers
    tulostettavat.append(self.customer)
    tulostettavat.append(self.versio)
    tulostettavat.append(self.trueversio)
    tulostettavat.append(self.IP)
    tulostettavat.append(data1data1M)
    tulostettavat.append(data6)
    tulostettavat.append(data7)
    tulostettavat.append(Hdata2)
    tulostettavat.append(data9)
    tulostettavat.append(data10)
    tulostettavat.append('???')
    tulostettavat.append('\t\t')
    tulostettavat.append(Vdata2)
    tulostettavat.append(data2K)
    tulostettavat.append('\t\t\t\t\t')
    tulostettavat.append(data14)
    tulostettavat.append(data15)
    tulostettavat.append(time.strftime('%d.%m.%Y'))

    while(True):
          try:
              f = open('listaus.xlxs','a')
              if os.path.getsize('listaus.xlxs') < 1:
                 f.write(ekarivi)
              for item in tulostettavat:
                 f.write(str(item) + '\t')
              f.write('\n')
              f.close()
              os.system('start excel.exe listaus.xlxs')
              break
          except:
              print('Sulje ensin tiedosto\n')
              time.sleep(0.5)
