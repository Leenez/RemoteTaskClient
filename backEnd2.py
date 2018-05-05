'''This is the "second backend" containing larger tables and objects I wanted to work separately.
SQL commands removed and some names changed to hide anything possibly confidential.'''

from Cryptodome.Cipher import DES3
import os

commond = [
#List of system specific sql commands.
]

x3d = [
#List of system specific sql commands.
]

x2d = [
#List of system specific sql commands.
]

x1d = [
#List of system specific sql commands.
]

x1A = []#Array of rows for building a file

x2A = []#Array of rows for building a file

#This class operates different userclients
class clientit:
  def __init__(self):
    self.cliversiot = ('tuple')#Tuple containing all different versions)
    self.oikversio = 'defaul'
    self.cliuser = 'default'
    self.vapaaportti = '91011'

  def getPath(self):
    return os.getcwd()

  #Build the conf file each time client launches
  def buildA(self):
    valipolku = self.getPath() + '\\' + self.oikversio[:5]
    if self.oikversio[1] == 'x1':
      file = valipolku + 'some path'
      taulu = x1A
      taulu[1] = '#String for manipulating rows'
      taulu[4] = '#String for manipulating rows'
      taulu[5] = '#String for manipulating rows'
      taulu[6] = '#String for manipulating rows'

    elif self.oikversio[1] == 'x2':
      file = 'some path'
      taulu = x2A
      taulu[1] = '#String for manipulating rows'
      taulu[3] = '#String for manipulating rows'

    with open(file, 'w') as f:
      for item in taulu:
        f.write(item)

  #Define conf file path each time before client launches. (Different Windows users have different paths due to different login names)
  def startPath(self):
      polku = self.getPath()
      p2 = 'some path'
      if self.oikversio[1] == 'x1':
       p = polku + '\\' + self.oikversio[:5]
       p = p + p2
       A = ' /A=' + polku + '\\' + self.oikversio[:5] + 'some path'
       ini = 'some path' + polku + '\\' + self.oikversio[:5] + 'some path' + self.cliuser
      elif self.oikversio[1] == 'x2':
       p = polku + '\\' + self.oikversio[:5]
       p = p + p2
       A = ' /A=' + polku + '\\' + self.oikversio[:5] + 'some path'
       ini = ' some path' + polku + '\\' + self.oikversio[:5] + 'some path ' + self.cliuser
      return p + A + ini

#Class for handling server information and encryption
class serverlist(object):
 def __init__(self):
  self.servertable2 = {}
  self.key = b'1234567890123456'
  self.des = DES3.new(self.key, DES3.MODE_ECB)
  self.otsikkotable = ('headers')#tuple containing headers

 def lineServers(self):
  serverjono = ''
  for key in self.servertable2:
      serverjono += key
      serverjono += ';'
      for item in self.servertable2[key]:
       serverjono += item
       serverjono += ';'
      serverjono += 'End of line marker'
  return serverjono[:-11]

 def lookServers2(self, jono):
     jonotable = jono.split(';End of line marker')
     jonotable = sorted(jonotable, reverse=True)
     data = []
     for item in jonotable:
      if item:
       a = item.split(';')
       servernimi = a[0]
       for i in range(1,len(a)):
        data.append(a[i])
       self.servertable2[servernimi] = tuple(data)
       data = []

 def addServer(self, customer, *args):
  if customer in self.servertable2:
      self.removeServer(customer)
  lisattava = args
  self.servertable2[customer] = lisattava

 def removeServer(self, customer):
   if customer == 'Anonymous':
    print('Anonymous ei voi poistaa')
    return
   else:
    del self.servertable2[customer]


 def namesAlphabet(self):
  return sorted(self.servertable2, reverse=True)

 def showAlphabet(self, customer):
  lista = ('customer information')#Tuple containing customer information
  rivi1 = customer + '\n\n'
  palauta = rivi1
  for a,b in zip(lista, self.servertable2[customer]):
   m = a + ' ' + b
   if a == 'cli:' or a == 'x3 usr: ' or a == 'vp:' or a == 'other:':
       palauta += '\n'
   palauta += m
   palauta += '\n'
  return palauta

 def tulosta(self, customer):
     tuloste = self.showAlphabet(customer)
     filenimi = 'some' + customer + 'txt'
     while(True):
          try:
              f = open(filenimi,'a')
              f.write(tuloste)
              f.close()
              komento ='start notepad.exe %s' % (filenimi)
              os.system(komento)
              break
          except:
              print('Close the file\n')
              time.sleep(0.5)

#Pad for encryption
 def pad(self, text):
  text = bytes(text, encoding='utf-8')
  while len(text) % 8 != 0:
   text += bytes(' ', encoding='utf-8')
  return text

 def cryptaa(self):
  o = self.pad(self.lineServers())
  encrypted_text = self.des.encrypt(o)
  return encrypted_text

 def avaa(self, text):
  d = self.des.decrypt(text)
  return str(d, 'utf-8').strip()
