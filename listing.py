import re
def keraysKatalogi(list1, list2):
 
 pattern = re.compile(r'\d{2,3}')
 valmis = []
 list2 = list2.split()
 
 for a in list2:
     if int(a[1]) == 5:
         valmis.append(int(a[-2] + a[-1]))
     elif int(a[1]) == 6:
         valmis.append(int('1' + a[-2] + a[-1]))
     elif int(a[1]) == 7:
         valmis.append(int('2' + a[-2] + a[-1]))
 valmis = set(valmis)
 valmis = list(valmis)
      
 katalogi = []
 aloitus = False
 pattern1 = re.compile(r'\d{2,4}')
 pattern2 = re.compile(r'[A-Ba-B]{5}.+')
 pattern3 = re.compile(r'[\[].+[\]]')
 for item in list1:
     rivi = str(item.strip())
     if "Some string" in rivi:
        aloitus = True
     if aloitus == True:
         item = rivi.split('mark')
         b = pattern1.findall(item[0])
         try:
          b = b[0]
         except:
          b = 987654321
         for luku in valmis:
          if int(b) == int(luku):
           tulostettava = pattern2.findall(item[1])
           katalogi.append(tulostettava[0])
           break
                 
 valmis = ''
 for item in katalogi:
     valmis += str(item) + ' , '
 return valmis
